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
        <div class="map-box">
            <div id="map" class="map-container">
            </div>
            <div>
                <div class="month-box">Month</div>
                <div class="month-selector">
                    <div @click="clickMonth('all')" :class="{ selected: selected == 'all' }">ALL</div>
                    <div @click="clickMonth('01')" :class="{ selected: selected == '01' }">Jan</div>
                    <div @click="clickMonth('02')" :class="{ selected: selected == '02' }">Feb</div>
                    <div @click="clickMonth('03')" :class="{ selected: selected == '03' }">Mar</div>
                    <div @click="clickMonth('04')" :class="{ selected: selected == '04' }">Apr</div>
                    <div @click="clickMonth('05')" :class="{ selected: selected == '05' }">May</div>
                    <div @click="clickMonth('06')" :class="{ selected: selected == '06' }">Jun</div>
                    <div @click="clickMonth('07')" :class="{ selected: selected == '07' }">Jul</div>
                    <div @click="clickMonth('08')" :class="{ selected: selected == '08' }">Aug</div>
                    <div @click="clickMonth('09')" :class="{ selected: selected == '09' }">Sep</div>
                    <div @click="clickMonth('10')" :class="{ selected: selected == '10' }">Oct</div>
                    <div @click="clickMonth('11')" :class="{ selected: selected == '11' }">Nov</div>
                    <div @click="clickMonth('12')" :class="{ selected: selected == '12' }">Dec</div>
                </div>
            </div>

        </div>


    </div>
</template>


<script>
import 'mapbox-gl/dist/mapbox-gl.css';

import axios from 'axios';
var data = null;
axios({
    url: 'https://raw.githubusercontent.com/colindaniels/CIA/main/assaults.geojson',
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
    methods: {
        clickMonth(month) {
            //const layer = document.getElementById('layer');
            this.selected = month
            if (month == 'all') {
                this.global_map.setFilter('crime', ['!=', 'Month', '.....']);
                this.global_map.setFilter('crime_point', ['!=', 'Month', '.....']);
            }
            else {
                this.global_map.setFilter('crime', ['==', 'Month', String(Number(month))]);
                this.global_map.setFilter('crime_point', ['==', 'Month', String(Number(month))]);
            }
        }
    },
    data() {
        return {
            global_map: "",
            selected: 'all'
        }
    },
    mounted() {
        mapboxgl.accessToken = 'pk.eyJ1IjoiZWNvbW1ldCIsImEiOiJja3V0YXpmMzgwc3J1MnJueTNrazhhejEyIn0.KkudRz1R4_glQLTiEKtKeQ';
        const map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/streets-v11', // style URL
            center: [-87.623177, 41.881832], // starting position [lng, lat]
            zoom: 11, // starting zoom
            projection: 'globe' // display the map as a 3D globe
        });
        map.on('style.load', () => {
            map.setFog({}); // Set the default atmosphere style
        });
        this.global_map = map

        map.on('load', () => {

            console.log(data)

            map.addSource('crime', {
                'type': 'geojson',
                'data': data

            })

            map.addLayer({
                'id': 'crime',
                'type': 'heatmap',
                'source': 'crime',

                paint: {
                    // increase weight as diameter breast height increases
                    'heatmap-weight': {
                        property: 'dbh',
                        type: 'exponential',
                        stops: [
                            [1, 0],
                            [62, 1]
                        ]
                    },
                    // increase intensity as zoom level increases
                    'heatmap-intensity': {
                        stops: [
                            [11, 1],
                            [15, 3]
                        ]
                    },
                    // assign color values be applied to points depending on their density
                    'heatmap-color': [
                        'interpolate',
                        ['linear'],
                        ['heatmap-density'],
                        0,
                        'rgba(236,222,239,0)',
                        0.4,
                        'green',
                        0.6,
                        'yellow',
                        0.8,
                        'rgb(235, 102, 49)',
                        1,
                        'rgb(235, 49, 49)'
                    ],
                    // increase radius as zoom increases
                    'heatmap-radius': 8,
                    // decrease opacity to transition into the circle layer
                    'heatmap-opacity': {
                        default: 1,
                        stops: [
                            [14, 1],
                            [15, 0]
                        ]
                    },
                }




            });
            map.addLayer({
                'id': 'crime_point',
                'type': 'circle',
                'source': 'crime',
                'minzoom': 14,
                paint: {
                    'circle-color': 'rgb(111, 164, 255)',
                    'circle-stroke-color': 'white',
                    'circle-radius': {
                        'base': 1.75,
                        'stops': [
                            [15, 10],
                            [22, 180]
                        ]
                    },
                    'circle-stroke-width': 2,
                    'circle-opacity': {
                        'stops': [
                            [14, 0],
                            [15, 1]
                        ]
                    }
                }
            },
            'waterway-label'
            )


            map.on('click', 'crime_point', (event) => {
                new mapboxgl.Popup()
                .setLngLat(event.features[0].geometry.coordinates)
                .setHTML(`
                <div class="c-pop">
                    <div>Date: <span>${event.features[0].properties.Date}</span></div>
                    </div>Block: <span>${event.features[0].properties.Block}</span></div>
                    <div>Description: <span>${event.features[0].properties.Description}</span></div>
                    <div>Date: <span>${event.features[0].properties.Date}</span></div>
                    <div>Location: <span>${event.features[0].properties['Location Description']}</span></div>
                    <div>Arrest?: <span>${event.features[0].properties.Arrest}</span></div>
                    <div>Domestic?: <span>${event.features[0].properties.Domestic}</span></div>
                    <div>Clouds: <span>${event.features[0].properties.Clouds}%</span></div>
                    <div>Max Temp: <span>${event.features[0].properties['Max Temp']} C</span></div>
                    <div>Min Temp: <span>${event.features[0].properties['Min Temp']} C</span></div>
                    <div>Wind Speed: <span>${event.features[0].properties['Max Wind Speed']} MPH</span></div>
                    <div>Precipitation: <span>${event.features[0].properties.Precipitation}%</span></div>  
                </div>
                `)
                .addTo(map)
            })

        })


        // remove watermarks
        document.querySelector('.mapboxgl-ctrl-bottom-left').remove()
        document.querySelector('.mapboxgl-ctrl-bottom-right').remove()


    }
}


</script>

<style>
.mapboxgl-popup-content {
    color: black;
}
.mapboxgl-popup-content span {
    font-weight: 700;
    color: black;
}

.mapboxgl-popup-content .c-pop {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

</style>

<style scoped>
.container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.map-box {
    width: 1000px;
    height: 500px;
}

.map-container {
    width: 100%;
    height: 100%;
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

.month-box {
    margin-top: 20px;
    font-size: 20px;
    color: white;
    font-weight: 800;
    margin-bottom: 10px;
}

.month-selector {
    font-size: 18px;
    display: flex;
    font-weight: 600;
    justify-content: space-between;
}

.month-selector>div {
    position: relative;
    cursor: pointer;
    width: 100%;
    padding-top: 5px;
    padding-bottom: 5px;
    border: 3px solid transparent;
    display: flex;
    justify-content: center;
}

.month-selector:last-child {
    border-right: 3px solid transparent;
}

.month-selector>div:hover,
.month-selector>div.selected {
    border: 3px solid white;
    background-color: rgb(255, 255, 255, 0.3);
}

.mapboxgl-popup {
    color: black !important;
}

</style>