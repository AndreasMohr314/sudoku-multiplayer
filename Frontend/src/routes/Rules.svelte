<script>
    // Hier kannst du beliebige Logik oder Inhalte hinzufügen
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
            <a href="/" class="nav-link" aria-current="page">Home</a>
        </li>
        <li class="nav-item">
            <a href="/rules" class="nav-link active">Rules</a>
        </li>
        <li class="nav-item">
            <a href="/about" class="nav-link">About</a>
        </li>
    </ul>
</header>
<main class="container my-5 scale-down">
    <h1 class="text-center mb-4">Rules</h1>

    <section>
        <h2>1. Start the Game</h2>
        <ol class="list-group list-group-numbered">
            <li class="list-group-item">
                On the <strong>Home/Start</strong> page, you can select the
                difficulty level for your Sudoku game: Easy, Normal, or
                Difficult.
                <div class="ratio ratio-16x9 my-3">
                    <video src="./videos/Levels.mp4" autoplay loop muted
                    ></video>
                </div>
            </li>
            <li class="list-group-item">
                Once the difficulty is set, click the <strong
                    >Create New Session</strong
                >
                button.
                <div class="ratio ratio-16x9 my-3">
                    <video src="/videos/Create.mp4" autoplay loop muted></video>
                </div>
            </li>
            <li class="list-group-item">
                A QR code will be generated for each player, along with a link
                that opens a new browser tab for the respective player. Players
                can either scan the QR code with their mobile devices or click
                the link.
                <div class="ratio ratio-16x9 my-3">
                    <video src="/videos/Link.mp4" autoplay loop muted></video>
                </div>
            </li>
        </ol>
    </section>

    <section class="mt-4">
        <h2>2. Get Ready to Play</h2>
        <ol class="list-group list-group-numbered">
            <li class="list-group-item">
                After scanning the QR code or clicking the link, players must
                confirm they are ready by pressing the <strong>Ready</strong>
                button.
                <div class="ratio ratio-16x9 my-3">
                    <video src="/videos/Ready.mp4" autoplay loop muted></video>
                </div>
            </li>
            <li class="list-group-item">
                Once both players have confirmed, the Sudoku game will start
                simultaneously with a timer.
                <div class="ratio ratio-16x9 my-3">
                    <video src="/videos/Game.mp4" autoplay loop muted></video>
                </div>
            </li>
            <li class="list-group-item">
                Solve the Sudoku puzzle as quickly as possible. The first player
                to complete it wins!
                <div class="ratio ratio-16x9 my-3">
                    <video src="/videos/Winner.mp4" autoplay loop muted></video>
                </div>
            </li>
        </ol>
    </section>
</main>

<footer class="bg-danger text-white text-center py-3">
    <p class="mb-0">© 2025 Multi Sudoku</p>
</footer>

<style>
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

    .scale-down {
        transform: scale(0.9);
        transform-origin: top center;
        max-width: 800px;
        margin: 0 auto;
    }

    .list-group-item {
        font-size: 1.2rem;
    }
</style>
