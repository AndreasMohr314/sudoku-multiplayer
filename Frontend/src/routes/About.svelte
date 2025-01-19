<!-- # This code was written by Andreas Mohr. -->
<!-- # Last change 17.01.2025. -->
<!-- # This Svelte component represents the About page of the Multi Sudoku application, including navigation, content about the app, and styling. -->

<script>
    // Logic and content for the About page
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
            <a href="/rules" class="nav-link">Rules</a>
        </li>
        <li class="nav-item">
            <a href="/about" class="nav-link active">About</a>
        </li>
    </ul>
</header>
<main>
    <div class="container py-5">
        <h1>About Us</h1>
        <p>
            This project is a non-commercial initiative designed purely for
            educational purposes.
        </p>
        <p>
            It does not collect or store any persistent data in the database. I
            created this multiplayer Sudoku app as a practice project to enhance
            my skills in Python, Redis, and Svelte, while integrating the
            experience with mobile devices. This application serves as a
            hands-on exploration of combining modern web technologies with
            interactive gameplay.
        </p>
    </div>
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
</style>
