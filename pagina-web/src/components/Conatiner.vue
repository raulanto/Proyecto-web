<script setup lang="ts">
// import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue' 
   import Header from './Header.vue';
   import Navbar from './Navbar.vue';
   import Blog from './Blog.vue';
</script>



<template>
   
    <main class="relative  min-h-screen min-w-full max-h-screen"> 
        <Navbar></Navbar>
        <Header></Header>
        <Blog></Blog>
    </main>
</template>