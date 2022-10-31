<template>
  <div id="main">
    <router-view id="router-view" />
  </div>
</template>

<script>

</script>

<style>


:root {
  --primary-color: #6FA4FF;
  --bg-color: rgb(14, 28, 41);
}

@font-face {
  font-family: "Colombo";
  src: local("Colombo"),   url(./assets/fonts/Colombo\ Sans\ Font.ttf) format("truetype");
}

#app {
  font-family: Helvetica;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  position: relative;
  float: left;
  width: 100%;
  height: 100%;

}

body {
  margin: 0;
  background-color: var(--bg-color);
}
span {
  color: var(--primary-color);
}

</style>
