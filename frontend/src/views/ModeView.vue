<script setup lang="ts">
    
</script>

<template>
    <div class="mode-select">
        <RouterLink class="manager-mode" to="/manager">
            <span>Режим учёта</span>
        </RouterLink>
        <RouterLink class="editor-mode" to="/editor">
            <span>Режим редактирования</span>
        </RouterLink>
    </div>
</template>

<style>
    .mode-select {
        display: flex;
        flex-direction: row;
        width: 100vw;
        height: 100vh;
    }

    .manager-mode {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 50vw;
        height: 100vh;
        background-color: #0f7bb9;
        transition: all 0.3s ease-out;
        cursor: pointer;
    }
    
    .manager-mode:hover {
        opacity: 0.8;
        transition: all 0.3s ease-out;
    }

    .manager-mode span {
        color: #E4ECF3;
    }

    .editor-mode {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 50vw;
        height: 100vh;
        background-color: #E4ECF3;
        transform: all 0.3s ease-out;
        cursor: pointer;
    }

    .editor-mode:hover {
        opacity: 0.8;
        transform: all 0.3s ease-out;
    }

    .editor-mode span {
        color: #0f7bb9;
    }

    span {
        color: white;
        font-size: 54px;
    }
</style>