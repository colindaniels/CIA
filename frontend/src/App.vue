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

h3 {
  font-size: 35px;
  color: var(--primary-color);
  margin: 0;
  margin-bottom: 25px;
}
h4 {
  font-size: 20px;
  margin: 0;
}

.groups {
  display: flex;
  flex-direction: column;
  gap: 40px;
  height: 100%;
}


.group {
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
}

.side {
  display: flex;
  height: 100%;
  gap: 40px;
}

.img-box {
  max-height: 80%;
  max-width: 100%;
}

.img-box img {
  width: 100%;
  height: 100%;
  max-height: 500px;
}

.img-box.long img {
  width: unset;
}

.img-box.medium {
  width: 50%;
}



</style>
