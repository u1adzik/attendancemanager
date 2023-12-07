<script setup>

</script>

<template>
    <RouterLink to="/" class="backarrow">
        <span>&#8592;</span>
    </RouterLink>
</template>

<style>
.backarrow {
    display: block;
    position: absolute;
    height: 100vh;
    background-color: #000;
    opacity: 0.5;
    width: 100px;
}

.backarrow span {
    display: inline;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    font-size: 35px;
    margin-top: 20px;
    transition: all 0.3s ease-out;
}

.backarrow:hover {
    opacity: 0.55;
    transition: all 0.3s ease-out;
}
</style>