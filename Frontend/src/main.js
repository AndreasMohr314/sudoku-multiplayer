// # This code was written by Andreas Mohr.
// # Last change 17.01.2025.
// # This JavaScript file serves as the entry point for the Sudoku application, importing Bootstrap for styling and initializing the main Svelte application.

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;