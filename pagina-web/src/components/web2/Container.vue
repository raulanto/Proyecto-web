<template>
    <section class="relative  min-h-screen min-w-full max-h-screen">
        <Navbar></Navbar>
        <Header></Header>
        <NavCard></NavCard>
        <ContainerCard></ContainerCard>
    </section>
</template>


<script lang="ts" setup>
    import Navbar from './Navbar.vue';
    import Header from './Header.vue';
    import NavCard from './Navcard.vue';
    import ContainerCard from './ContainerCard.vue';
</script>