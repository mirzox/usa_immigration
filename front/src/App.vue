<template>
  <div class="app">
    <Navigate />
    <router-view />
  </div>
</template>
<script>
// @ is an alias to /src
import Navigate from '@/components/Navigate.vue'

export default {
  components: {
    Navigate,
  }
}
</script>
<style>
body {
  margin: 0px;
  padding: 0px;
  background-color: #fff !important;

}
@font-face {
  font-family: vladfonts;
  src: url(../src/assets/fonts/Playfair-VariableFont_opsz\,wdth\,wght.ttf);
}
#app {
  font-family: vladfonts !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  font-family: vladfonts !important;
}
</style>
