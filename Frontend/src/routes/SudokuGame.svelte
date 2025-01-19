<!-- # This code was written by Andreas Mohr. -->
<!-- # Last change 17.01.2025. -->
<!-- # This Svelte component represents the Sudoku game page, allowing players to interact with the board, track progress, and see game results. -->

<script>
    import { onMount } from "svelte";
    import Throbber from "./Throbber.svelte";

    //----------------------------------------------------------
    // Configuration: Please set your local IP address below
    // Replace the placeholder with your local IP address
    // Example: const localIP = "192.168.0.100";
    //----------------------------------------------------------
    const localIP = ""; // Change this to your local IP address
    //----------------------------------------------------------

    let board = [];
    let editable = [];
    let errorStates = [];
    let sessionId = "";
    let player = "";
    let websocket;
    let errorCount = 0;
    let isWinner = false;
    let isLoser = false;
    let progress = 0;
    let timer = 0;
    let gameStarted = false;
    let filledCellsAtStart = 0;
    let readyButtonClicked = false;

    function SetFilledCellsAtStart() {
        filledCellsAtStart = board
            .flat()
            .filter((cell) => cell !== 0 && cell !== null).length;
    }

    function calculateProgress() {
        const totalCells = 81;
        const filledCells = board
            .flat()
            .filter((cell) => cell !== 0 && cell !== null).length;
        progress =
            100 -
            Math.round(
                ((totalCells - filledCells) /
                    (totalCells - filledCellsAtStart)) *
                    100,
            );
    }

    let timerInterval;
    function startTimer() {
        timerInterval = setInterval(() => {
            timer += 1;
        }, 1000);
    }

    function formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
    }

    function validateKeypress(e) {
        const allowedKeys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        if (!allowedKeys.includes(e.key)) {
            e.preventDefault();
        }
    }

    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        sessionId = params.get("session_id");
        player = params.get("player");

        if (sessionId && player) {
            connectToWebsocket(sessionId, player);
        }
    });

    function connectToWebsocket(sessionId, player) {
        const websocketUrl = `ws://${localIP}:8000/ws/${sessionId}?player=${player}`;
        websocket = new WebSocket(websocketUrl);

        websocket.onopen = () => {
            console.log("WebSocket connected!");
        };

        websocket.onmessage = (event) => {
            const data = JSON.parse(event.data);

            if (data.action === "start") {
                gameStarted = true;
                startTimer();
            } else if (data.action === "init") {
                if (player === "1") {
                    board = data.board_1;
                    editable = data.board_1.map((row) =>
                        row.map((cell) => cell === 0 || cell === null),
                    );
                    errorStates = board.map((row) => row.map(() => false));
                } else {
                    board = data.board_2;
                    editable = data.board_2.map((row) =>
                        row.map((cell) => cell === 0 || cell === null),
                    );
                    errorStates = board.map((row) => row.map(() => false));
                }
                SetFilledCellsAtStart();
                calculateProgress();
            } else if (data.action === "update") {
                if (player === "1") {
                    board = data.board_1;
                    editable = board.map((row) =>
                        row.map((cell) => cell === 0 || cell === null),
                    );

                    errorStates = board.map((row, rowIndex) =>
                        row.map((cell, colIndex) => {
                            return editable[rowIndex][colIndex]
                                ? errorStates[rowIndex][colIndex]
                                : false;
                        }),
                    );
                } else {
                    board = data.board_2;
                    editable = board.map((row) =>
                        row.map((cell) => cell === 0 || cell === null),
                    );

                    errorStates = board.map((row, rowIndex) =>
                        row.map((cell, colIndex) => {
                            return editable[rowIndex][colIndex]
                                ? errorStates[rowIndex][colIndex]
                                : false;
                        }),
                    );
                }

                calculateProgress();
            } else if (data.action === "error") {
                if (data.error_player === player) {
                    const { row, col } = data;
                    errorStates[row][col] = true;
                    errorCount++;
                }
            } else if (data.action === "winner") {
                isWinner = data.player_win === player;
                isLoser = !isWinner;
                clearInterval(timerInterval);
            }
        };

        websocket.onclose = () => {
            console.log("WebSocket connection closed.");
        };
    }

    function ready() {
        readyButtonClicked = true;
        websocket.send(
            JSON.stringify({
                action: "ready",
            }),
        );
    }

    function handleInput(row, col, value) {
        if (!editable[row][col]) {
            return;
        }

        const parsedValue = parseInt(value);
        if (!isNaN(parsedValue) && parsedValue >= 1 && parsedValue <= 9) {
            websocket.send(
                JSON.stringify({
                    action: "input",
                    row,
                    col,
                    value: parsedValue,
                    player: player,
                }),
            );
            errorStates[row][col] = false;
        } else {
            board[row][col] = "";
            errorStates[row][col] = false;
        }
    }
</script>

<main class="main-container">
    <header class="header">
        <span class="header-title">Multi Sudoku</span>
    </header>

    {#if !gameStarted}
        <div class="content-container">
            <div class="text-center mb-3">
                {#if !readyButtonClicked}
                    <p class="fs-4">Hello Player {player}</p>
                {:else}
                    <p class="fs-4">Player {player} is ready</p>
                {/if}
            </div>
            <div class="mb-3">
                <button
                    class="btn btn-outline-danger btn-hover{readyButtonClicked ===
                    true
                        ? '-active'
                        : ''}"
                    on:click={() => ready()}
                >
                    Start
                </button>
            </div>
            {#if readyButtonClicked}
                <div class="mt-3">
                    <Throbber
                        size="lg"
                        color="danger"
                        message="Please wait..."
                    />
                </div>
            {/if}
        </div>
    {:else}
        <div class="info-bar">
            <div>Time: {formatTime(timer)}</div>
            <div>Errors: {errorCount}</div>
        </div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress}%"></div>
        </div>
        <div class="sudoku-container">
            <div class="sudoku-board">
                {#each board as row, rowIndex}
                    {#each row as cell, colIndex}
                        <input
                            type="text"
                            maxlength="1"
                            value={cell || ""}
                            pattern="[1-9]"
                            inputmode="numeric"
                            disabled={!editable[rowIndex][colIndex]}
                            class:error={errorStates[rowIndex]?.[colIndex]}
                            on:keypress={(e) => validateKeypress(e)}
                            on:input={(e) =>
                                handleInput(rowIndex, colIndex, e.target.value)}
                        />
                    {/each}
                {/each}
            </div>
        </div>
    {/if}
    {#if isWinner}
        <div class="winner-popup">Winner!</div>
    {/if}
    {#if isLoser}
        <div class="loser-popup">Game Over</div>
    {/if}
</main>

<style>
    .main-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        min-height: 100vh;
        background-color: #f9f9f9;
    }

    .header {
        width: 100%;
        background-color: #dc3545;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
        padding: 0.5rem 0;
        border-bottom: 2px solid #b12828;
    }

    .header-title {
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }

    @media (min-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
    }

    .content-container {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin-bottom: 0px;
    }

    .fs-4 {
        font-size: 1.5rem;
    }

    @media (min-width: 768px) {
        .fs-4 {
            font-size: 2rem;
        }

        .btn {
            padding: 1rem 2rem;
            font-size: 1.25rem;
        }
    }

    .info-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        max-width: 360px;
        margin: 2px;
        padding: 5px 10px;
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    .progress-container {
        margin-bottom: 2px;
        padding: 0;
        width: 100%;
        max-width: 360px;
        height: 20px;
        background-color: #ddd;
        border: 1px solid #aaa;
        border-radius: 5px;
        overflow: hidden;
    }

    .progress-bar {
        height: 100%;
        background-color: #b12828b3;
        transition: width 0.3s ease;
    }

    .sudoku-container {
        margin-top: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex: 0.5;
        width: 100%;
    }

    .sudoku-board {
        margin-top: 2px;
        padding: 0;
        display: grid;
        grid-template-rows: repeat(9, 1fr);
        grid-template-columns: repeat(9, 1fr);
        gap: 0;
        width: 90vw;
        max-width: 360px;
        height: 90vw;
        max-height: 360px;
        border: 3px solid black;
    }

    .btn-hover-active {
        background-color: #4b0707 !important;
        border-color: #4b0707;
        color: white;
    }

    input {
        width: 100%;
        height: 100%;
        text-align: center;
        font-size: clamp(14px, 2.5vw, 18px);
        border: 1px solid #000;
        box-sizing: border-box;
    }

    /* Styling für 3x3-Blockstructur */
    /* left line */
    input:nth-child(3n) {
        border-right: 3px solid black;
    }

    input:nth-child(4) {
        border-left: 3px solid black;
    }

    input:nth-child(9n + 4) {
        border-left: 3px solid black;
    }

    /* rigth-line */
    input:nth-child(6n) {
        border-right: 3px solid black;
    }

    input:nth-child(7) {
        border-left: 3px solid black;
    }

    input:nth-child(9n + 7) {
        border-left: 3px solid black;
    }

    /* first-horizontal-line */
    input:nth-child(n + 19):nth-child(-n + 27) {
        border-bottom: 3px solid black;
    }

    input:nth-child(n + 28):nth-child(-n + 36) {
        border-top: 3px solid black;
    }

    /* second-horizontal-line */
    input:nth-child(n + 46):nth-child(-n + 54) {
        border-bottom: 3px solid black;
    }

    input:nth-child(n + 55):nth-child(-n + 63) {
        border-top: 3px solid black;
    }

    input:disabled {
        color: #000;
    }

    input.error {
        color: red !important;
    }

    input.error:focus {
        color: red !important;
        background-color: lightblue;
        outline: none;
        box-shadow: 0 0 5px rgba(255, 0, 0, 0.5);
    }
    input:focus {
        background-color: lightblue;
        outline: none;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }

    input.error:focus {
        box-shadow: 0 0 5px rgba(255, 0, 0, 0.5);
    }

    .winner-popup {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        border: 2px solid green;
        padding: 20px;
        text-align: center;
    }

    @media (max-width: 768px) {
        .sudoku-board {
            width: 100vw;
            height: 100vw;
            max-width: none;
            max-height: none;
        }

        input {
            font-size: 4vw;
        }

        .sudoku-container {
            padding: 0;
        }
    }
</style>
