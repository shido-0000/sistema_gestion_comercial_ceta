<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Inicio from "@/components/paginas/inicio/inicio.vue";

const isLoggedIn = false; // Cambia esto a true cuando el usuario inicie sesión
</script>

<template>
 <!-- <div class="container">-->
  <div>
    <header>

      <!--     <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
       <div class="wrapper">
           <HelloWorld msg="You did it!" />
           <nav>
             <RouterLink to="/">Home</RouterLink>
             <RouterLink to="/about">About</RouterLink>
           </nav>
         </div> -->
    </header>
    <!--<inicio></inicio>-->

    <!--  <router-view v-if="isLoggedIn" />  Esto mostrará el RouterView solo si el usuario está autenticado -->
    <!--
        <inicio v-if="!isLoggedIn"></inicio> Esto mostrará el componente Inicio solo si el usuario NO está autenticado -->

    <RouterView />
  </div>


  <!--
  <style scoped>
    .container {
      display: block;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin-right: auto;

    }


    header {
      line-height: 1.5;
      /* max-height: 100vh; */
    }

    .logo {
      display: block;
      margin: 0 auto 2rem;
    }

    .wrapper {
      display: flex;
      place-items: flex-start;
      flex-wrap: wrap;
    }

    nav {
      width: 100%;
      font-size: 12px;
      text-align: right;
      margin-top: 2rem;
    }

    nav a.router-link-exact-active {
      color: var(--color-text);
    }

    nav a.router-link-exact-active:hover {
      background-color: transparent;
    }

    nav a {
      display: inline-block;
      padding: 0 1rem;
      border-left: 1px solid var(--color-border);
    }

    nav a:first-of-type {
      border: 0;
    }

    @media (min-width: 1024px) {
      header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
      }

      header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
      }

      nav {
        text-align: left;
        margin-left: 0rem;
        font-size: 1rem;
        padding: 1rem 0;
        margin-top: 0rem;
      }
    }
  </style>-->

</template>


