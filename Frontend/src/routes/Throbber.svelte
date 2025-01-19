<!-- # This code was written by Andreas Mohr. -->
<!-- # Last change 17.01.2025. -->
<!-- # This Svelte component displays a customizable loading spinner with optional text. -->

<script>
    export let size = "md"; // Options: 'sm', 'md', 'lg'
    export let color = "primary"; // Bootstrap colors: 'primary', 'secondary', 'success', etc.
    export let message = "Loading..."; // Optional loading text
</script>

<div class="d-flex flex-column align-items-center">
    <div
        class="spinner-border text-{color}"
        role="status"
        style="width: {size === 'sm'
            ? '1.5rem'
            : size === 'lg'
              ? '3rem'
              : '2rem'}; height: {size === 'sm'
            ? '1.5rem'
            : size === 'lg'
              ? '3rem'
              : '2rem'};"
    >
        <span class="visually-hidden">Loading...</span>
    </div>
    {#if message}
        <div class="mt-2 text-{color}">{message}</div>
    {/if}
</div>

<style>
    .spinner-border {
        display: inline-block;
    }
</style>
