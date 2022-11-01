<template>
    <div class="content">
        <MabboxMap/>
    </div>
    <div class="btn-box">
        <router-link :to="`/slides?slide=${active}`" class="neon-button">Slides</router-link>
    </div>
</template>

<script>
import MabboxMap from '@/components/MapboxMap.vue'
export default {
    components: {
        MabboxMap,

    },
    data() {
        return {
            active: Number(this.$route.query.storage)
        }
    }
}

</script>

<style scoped>
.neon-button {
    font-size: 1.5rem;

    display: inline-block;
    cursor: pointer;
    text-decoration: none;
    color: var(--primary-color);
    border: var(--primary-color) 0.125em solid;
    padding: 0.25em 1em;
    border-radius: 0.25em;

    text-shadow: 0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.45em currentColor;

    box-shadow: inset 0 0 0.5em 0 var(--primary-color), 0 0 0.5em 0 var(--primary-color);

    position: relative;
}
.neon-button::before {
  pointer-events: none;
  content: "";
  position: absolute;
  background: var(--primary-color);
  top: 120%;
  left: 0;
  width: 100%;
  height: 100%;

  transform: perspective(1em) rotateX(40deg) scale(1, 0.35);
  filter: blur(1em);
  opacity: 0.7;
}

.neon-button::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  box-shadow: 0 0 2em 0.5em var(--primary-color);
  opacity: 0;
  background-color: var(--primary-color);
  z-index: -1;
  transition: opacity 100ms linear;
}

.neon-button:hover {
  color: var(--bg-color);
  text-shadow: none;
}


.neon-button:hover::before {
  opacity: 1;
}
.neon-button:hover::after {
  opacity: 1;
}

.btn-box {
    display: flex;
    justify-content: center;
    position: absolute;
    bottom: 0;
    left: 14%;
}



</style>