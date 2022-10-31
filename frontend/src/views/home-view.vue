<template>
    <div class="content">
        <div class="text-holder">
            <div class="head">
                <div class="big">Windy City <span>Crime</span></div>
                <div class="line"></div>
                <div class="sub-bottom">
                    By: Colin, Irene, and Andrea
                </div>
                <div class="rel">
                    <router-link to="/map" class="neon-button">START</router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.content {
    height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.text-holder {
    width: 100%;
    position: relative;
    margin-top: 200px;
    height: 200px;
}

.head {
    white-space: nowrap;
    animation: swipeInLeft 1s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
    position: absolute;
}

.head .big {
    font-family: Colombo;
    font-size: 72px;
    font-weight: 500;
}

.head .line {
    width: 100%;
    height: 3px;
    background-color: white;
    width: 0;
    animation: width100 1s cubic-bezier(0, 0, 0.1, 1) forwards;
    animation-delay: 1.1s;
}

.sub-bottom {
    position: absolute;
    font-size: 30px;
    color: rgb(190, 190, 190);
    left: 200%;
    animation: swipeInRight 1s cubic-bezier(0, 0, 0.1, 1) forwards;
    animation-delay: 1.1s;
    font-weight: 800;
    white-space: nowrap;
    opacity: 0;
    top: 100px;
}

.rel {
    margin-top: 100px;
}

.neon-button {
    font-size: 2rem;

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
    opacity: 0;
    animation: fadeIn 1s ease-in-out forwards;
    animation-delay: 2.1s;
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

.neon-button:hover,
.neon-button:focus {
  color: var(--bg-color);
  text-shadow: none;
}

.neon-button:hover::before,
.neon-button:focus::before {
  opacity: 1;
}
.neon-button:hover::after,
.neon-button:focus::after {
  opacity: 1;
}



@keyframes swipeInLeft {
    0% {
        right: 100%;
    }

    100% {
        right: 50%;
        transform: translateX(50%);
    }
}

@keyframes fadeIn {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 100%;
    }
}

@keyframes width100 {
    0% {
        width: 0%;
    }

    100% {
        width: 100%;
    }
}

@keyframes swipeInRight {
    0% {
        left: 200%;
    }

    50% {
        opacity: 1;
    }

    100% {
        opacity: 1;
        left: 0;
    }
}
</style>