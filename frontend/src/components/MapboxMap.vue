<template>
    <div class="container">
        <!--
        <div class="map-key">
            
            <div>
                <div class="k assult"></div>
                <div class="v"></div>
            </div>
            <div>
                <div class="k battery"></div>
                <div class="v"></div>
            </div>
            <div>
                <div class="k petty"></div>
                <div class="v"></div>
            </div>
       
        </div>
        -->
        <div id="map" class="map-container">
        </div>

    </div>
</template>


<script>
import 'mapbox-gl/dist/mapbox-gl.css';

import axios from 'axios';
var data = null;
axios({
    url: 'https://raw.githubusercontent.com/colindaniels/CIA/main/assults.geojson',
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8'
    }
}).then((res) => {
    if (res.status == 200 && res.data) {
        data = res.data
    }
})

import mapboxgl from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"




export default {
    mounted() {
        mapboxgl.accessToken = 'pk.eyJ1IjoiZWNvbW1ldCIsImEiOiJja3V0YXpmMzgwc3J1MnJueTNrazhhejEyIn0.KkudRz1R4_glQLTiEKtKeQ';
        const map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/streets-v11', // style URL
            center: [-87.623177, 41.881832], // starting position [lng, lat]
            zoom: 9, // starting zoom
            projection: 'globe' // display the map as a 3D globe
        });
        map.on('style.load', () => {
            map.setFog({}); // Set the default atmosphere style
        });

        map.on('load', () => {
            console.log(data)
            map.addSource('places', {
                'type': 'geojson',
                'data': data

            })

            map.addLayer({
                'id': 'places',
                'type': 'symbol',
                'source': 'places',
                'layout': {
                    'icon-image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAX-6lgj3uY4ItnfDjZteAPUcvIKeN4pHdVvneC50nyg&s',
                    'icon-allow-overlap': true
                }
            });

        })

        // remove watermarks
        document.querySelector('.mapboxgl-ctrl-bottom-left').remove()
        document.querySelector('.mapboxgl-ctrl-bottom-right').remove()


    }
}


</script>

<style scoped>
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.map-container {
    width: 1000px;
    height: 500px;
}


.map-key {
    width: 200px;
    border: 5px solid white;
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 10px;
    box-sizing: border-box;
}

.map-key>div {
    display: flex;
}

.map-key .k {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    border: 3px solid white;
}

.map-key .k.assult {
    background-color: rgb(251, 172, 116);
}

.map-key .k.battery {
    background-color: rgb(203, 203, 0);
}

.map-key .k.petty {
    background-color: rgb(126, 214, 126);
}
</style>