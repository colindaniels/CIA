<template>
    <div class="present-box">
        <div class="present">
            <Slide0 v-if="active == 0"/>
            <Slide1 v-if="active == 1"/>
            <Slide2 v-if="active == 2"/>
            <Slide3 v-if="active == 3"/>
            <Slide4 v-if="active == 4"/>
            <Slide5 v-if="active == 5"/>
            <Slide6 v-if="active == 6"/>
            <Slide7 v-if="active == 7"/>
            <Slide8 v-if="active == 8"/>
            <Slide9 v-if="active == 9"/>
            <Slide10 v-if="active == 10"/>
            <Slide11 v-if="active == 11"/>
            <Slide12 v-if="active == 12"/>
        </div>
        <div class="btns">
            <router-link v-if="active > 0" to="#" @click="back" class="neon-button">Back</router-link>
            <router-link v-if="active < total_slides" to="#" @click="next" class="neon-button">Next</router-link>
            <router-link :to="`/map?storage=${active}`" class="neon-button">Map</router-link>
        </div>


    </div>



</template>

<script>
import Slide0 from '@/components/Slide-0.vue'
import Slide1 from '@/components/Slide-1.vue'
import Slide2 from '@/components/Slide-2.vue'
import Slide3 from '@/components/Slide-3.vue'
import Slide4 from '@/components/Slide-4.vue'
import Slide5 from '@/components/Slide-5.vue'
import Slide6 from '@/components/Slide-6.vue'
import Slide7 from '@/components/Slide-7.vue'
import Slide8 from '@/components/Slide-8.vue'
import Slide9 from '@/components/Slide-9.vue'
import Slide10 from '@/components/Slide-10.vue'
import Slide11 from '@/components/Slide-11.vue'
import Slide12 from '@/components/Slide-12.vue'
export default {
    components: {
        Slide0,
        Slide1,
        Slide2,
        Slide3,
        Slide4,
        Slide5,
        Slide6,
        Slide7,
        Slide8,
        Slide9,
        Slide10,
        Slide11,
        Slide12
    },
    methods: {
        back() {
            this.active -= 1
            this.$router.push({ query: {'slide': this.active} }).then(() => {
                this.$router.go()
            })
        },
        next() {
            
            this.active += 1
            this.$router.push({ query: {'slide': this.active} })
        }
    },
    data() {
        return {
            active: Number(this.$route.query.slide),
            total_slides: 12
        }
    }
}

</script>

<style scoped>


.present-box {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    padding: 50px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 30px;
    max-width: 1500px;
}

.present {
    border: 5px solid white;
    padding: 30px;
    box-sizing: border-box;
}

.btns {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
    position: relative;
}

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

</style>