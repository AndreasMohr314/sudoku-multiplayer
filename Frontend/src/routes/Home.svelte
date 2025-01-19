<!-- # This code was written by Andreas Mohr. -->
<!-- # Last change 17.01.2025. -->
<!-- # This Svelte component represents the Home page of the Multi Sudoku app, allowing users to create a new game session and select difficulty levels. -->

<script>
    let sessionId = ""; // Session ID, initially empty
    let qrCodePath = ""; // QR code path, initially empty
    let difficultLevel = "normal";

    function setDifficulty(level) {
        difficultLevel = level;
    }

    async function createSession() {
        const response = await fetch(
            `http://localhost:8000/create-${difficultLevel}-session`,
            {
                method: "POST",
            },
        );
        const data = await response.json(); // Fetch data from the backend

        if (data.session_id && data.qr_code) {
            sessionId = data.session_id;
            qrCodePath = data.qr_code; // URL of the QR code
        } else {
            console.error("Invalid response from backend:", data);
        }
    }
</script>

<header class="bg-danger d-flex justify-content-center py-3 mb-4 border-bottom">
    <a
        href="/"
        class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none"
    >
        <span class="fs-4 text-white">Multi Sudoku</span>
    </a>

    <ul class="nav nav-pills">
        <li class="nav-item">
            <a href="/" class="nav-link active" aria-current="page">Home</a>
        </li>
        <li class="nav-item">
            <a href="/rules" class="nav-link">Rules</a>
        </li>
        <li class="nav-item">
            <a href="/about" class="nav-link">About</a>
        </li>
    </ul>
</header>

<main>
    <div class="d-flex justify-content-center align-items-center vh-10">
        <div class="container text-center">
            <!-- Difficulty Selection -->
            <div
                class="btn-group mb-3"
                role="group"
                aria-label="Difficulty Levels"
            >
                <button
                    type="button"
                    class="btn btn-secondary btn-color-hover{difficultLevel ===
                    'easy'
                        ? '-active'
                        : ''}"
                    on:click={() => setDifficulty("easy")}
                >
                    Easy
                </button>
                <button
                    type="button"
                    class="btn btn-secondary btn-color-hover{difficultLevel ===
                    'normal'
                        ? '-active'
                        : ''}"
                    on:click={() => setDifficulty("normal")}
                >
                    Normal
                </button>
                <button
                    type="button"
                    class="btn btn-secondary btn-color-hover{difficultLevel ===
                    'difficult'
                        ? '-active'
                        : ''}"
                    on:click={() => setDifficulty("difficult")}
                >
                    Difficult
                </button>
            </div>

            <!-- Create Session -->
            <div>
                <button class="btn btn-outline-danger" on:click={createSession}>
                    Create New Session
                </button>
            </div>
        </div>
    </div>

    {#if qrCodePath.length > 0}
        <div class="container">
            <div class="row justify-content-center">
                <div
                    class="col-md-4 text-center d-flex flex-column align-items-center qr-container"
                >
                    <h2 class="player-title">Player 1:</h2>
                    <img
                        class="qr-square"
                        src={`http://localhost:8000${qrCodePath[0]}`}
                        alt="QR Code for Player 1"
                    />
                    <a
                        href={`http://localhost:5000/sudoku-game?session_id=${sessionId}&player=1`}
                        target="_blank"
                        rel="noopener noreferrer"
                        class="mt-3"
                    >
                        Link to session
                    </a>
                </div>

                <div
                    class="col-md-4 text-center d-flex flex-column align-items-center qr-container"
                >
                    <h2 class="player-title">Player 2:</h2>
                    <img
                        class="qr-square"
                        src={`http://localhost:8000${qrCodePath[1]}`}
                        alt="QR Code for Player 2"
                    />
                    <a
                        href={`http://localhost:5000/sudoku-game?session_id=${sessionId}&player=2`}
                        target="_blank"
                        rel="noopener noreferrer"
                        class="mt-3"
                    >
                        Link to session
                    </a>
                </div>
            </div>
        </div>
    {/if}
</main>

<footer class="bg-danger text-white text-center py-3">
    <p class="mb-0">© 2025 Multi Sudoku</p>
</footer>

<style>
    .player-title {
        font-size: 1.5rem;
        margin-bottom: 5px;
    }

    .qr-square {
        width: 100%;
        max-width: 200px;
        height: auto;
    }

    .qr-container {
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    @media (min-width: 768px) {
        .qr-square {
            max-width: 250px;
        }
        .qr-container {
            min-height: 400px;
        }
    }

    @media (min-width: 1200px) {
        .qr-square {
            max-width: 300px;
        }
        .qr-container {
            min-height: 500px;
        }
    }

    a {
        display: inline-block;
        margin-top: 10px;
        padding: 10px 20px;
        background-color: #b12828b3;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        max-width: 200px;
        max-height: 200px;
    }

    a:hover {
        background-color: #4b0707;
    }

    .btn-color-hover {
        background-color: #b12828b3 !important;
        color: white !important;
        border-color: #b12828b3 !important;
    }

    .btn-color-hover:hover {
        background-color: #4b0707 !important;
    }

    .btn-color-hover-active {
        background-color: #4b0707 !important;
        border-color: #4b0707;
    }
</style>
