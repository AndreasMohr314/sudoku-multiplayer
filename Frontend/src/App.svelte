<!-- # This code was written by Andreas Mohr. -->
<!-- # Last change 17.01.2025. -->
<!-- # This Svelte component sets up the main router for the Sudoku app, defining routes for different pages such as Home, Join Session, Sudoku Game, Rules, and About. -->

<script>
	import { Router, Route } from "svelte-routing";
	import SudokuGame from "./routes/SudokuGame.svelte";
	import Home from "./routes/Home.svelte";
	import Rules from "./routes/Rules.svelte";
	import About from "./routes/About.svelte";
</script>

<Router>
	<Route path="/" component={Home} />
	<Route path="/sudoku-game" component={SudokuGame} />
	<Route path="/rules" component={Rules} />
	<Route path="/about" component={About} />
</Router>
