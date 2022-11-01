<template>
    <div class="container">
        <div class="horz">
            <div class="weather-slider">
                <label>Min Temp</label>
                <input type="range" v-model="min_value" min="-20.0" max="45.0">
                <div class="number">{{ min_value }}°C</div>
            </div>
            <div class="weather-slider">
                <label>Max Temp</label>
                <input type="range" v-model="max_value" min="-20.0" max="45.0">
                <div class="number">{{ max_value }}°C</div>
            </div>
            <div class="map-box">
                <div class="head">Assault Crime In Chicago Based on Month and Temperature</div>
                <div id="map" class="map-container">
                    <div class="count">Count: {{ assault_count }}</div>
                </div>
                <div>
                    <div class="month-box">Month</div>
                    <div class="month-selector">
                        <div @click="clickMonth('all')" :class="{ selected: month == 'all' }">ALL</div>
                        <div @click="clickMonth('01')" :class="{ selected: month == '01' }">Jan</div>
                        <div @click="clickMonth('02')" :class="{ selected: month == '02' }">Feb</div>
                        <div @click="clickMonth('03')" :class="{ selected: month == '03' }">Mar</div>
                        <div @click="clickMonth('04')" :class="{ selected: month == '04' }">Apr</div>
                        <div @click="clickMonth('05')" :class="{ selected: month == '05' }">May</div>
                        <div @click="clickMonth('06')" :class="{ selected: month == '06' }">Jun</div>
                        <div @click="clickMonth('07')" :class="{ selected: month == '07' }">Jul</div>
                        <div @click="clickMonth('08')" :class="{ selected: month == '08' }">Aug</div>
                        <div @click="clickMonth('09')" :class="{ selected: month == '09' }">Sep</div>
                        <div @click="clickMonth('10')" :class="{ selected: month == '10' }">Oct</div>
                        <div @click="clickMonth('11')" :class="{ selected: month == '11' }">Nov</div>
                        <div @click="clickMonth('12')" :class="{ selected: month == '12' }">Dec</div>
                    </div>
                </div>

            </div>
        </div>



    </div>
</template>


<script>
import 'mapbox-gl/dist/mapbox-gl.css';

import axios from 'axios';
var data = null;
var map_data = null;

// requests
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

axios({
    url: 'https://raw.githubusercontent.com/colindaniels/CIA/main/chicago_map.geojson',
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8'
    }
}).then((res) => {
    if (res.status == 200 && res.data) {
        map_data = res.data
    }
})

import mapboxgl from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"



export default {
    methods: {
        clickMonth(month) {
            //const layer = document.getElementById('layer');
            this.month = month
            this.global_map.setFilter('crime', this.map_filter());
            this.global_map.setFilter('crime_point', this.map_filter());
            this.refreshCount()
        },

        map_filter() {
            var filter = [
                'all',
                ['>=', 'Max Temp', Number(this.min_value)],
                ['<=', 'Max Temp', Number(this.max_value)]
            ]
            if (this.month != 'all') {
                filter.push(['==', 'Month', String(Number(this.month))])
            }
            return filter
        },
        refreshCount() {
            this.assault_count = this.global_map.queryRenderedFeatures().length
        }

    },
    data() {
        return {
            global_map: "",
            month: 'all',
            min_value: -20,
            max_value: 45,
            assault_count: 0
        }
    },

    watch: {
        min_value: function () {
            this.global_map.setFilter('crime', this.map_filter());
            this.global_map.setFilter('crime_point', this.map_filter());


        },
        max_value: function () {
            this.global_map.setFilter('crime', this.map_filter());
            this.global_map.setFilter('crime_point', this.map_filter());
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

            this.assault_count = data.features.length

            console.log(data)
            console.log(map_data)

            map.addSource('crime', {
                'type': 'geojson',
                'data': data

            })

            map.addSource('borders', {
                'type': 'geojson',
                'data': map_data

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
                    'heatmap-radius': 10,
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




            map.addLayer({
                'id': 'borders',
                'source': 'borders',
                "type": "fill",
                "paint": {
                    "fill-color": "rgb(128, 128, 128)",
                    'fill-outline-color': 'red',
                    'fill-opacity': 0.5
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
    width: 90%;
}

.map-container {
    width: 100%;
    height: 80vh;
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

.weather-slider {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    width: 10%;
    position: relative;

}

.weather-slider .number {
    background-color: white;
    color: var(--bg-color);
    font-size: 20px;
    font-size: 900;
    width: 80%;
    border-radius: 5px;
    position: relative;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
}

.weather-slider input[type="range"] {
    -webkit-appearance: none;
    height: 5px;
    position: relative;
    background-color: white;
    border-radius: 5px;
    outline: none;
    transform: rotate(-90deg);
    width: 350px;
}

.weather-slider input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    background-color: var(--primary-color);
    height: 40px;
    width: 25px;
    cursor: pointer;
}

.weather-slider input[type="range"]::-webkit-slider-thumb:hover {
    background-color: var(--primary-color);
    filter: brightness(80%);
}


.number::before {
    position: absolute;
    content: "";
    width: 0;
    height: 0;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    border-bottom: 10px solid white;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
}


.horz {
    display: flex;
    width: 80%;
    gap: 30px;
}

.weather-slider label {
    text-align: center;
    position: absolute;
    top: calc(69.5px + 5%);
    font-size: 18px;
    font-weight: 600;
}

.weather-slider .number {
    bottom: calc(69.5px + 5%);
}

.head {
    font-size: 24px;
    font-weight: 600;
    letter-spacing: 0.5px;
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 54.5px;
    /* keep to center */
    margin-bottom: 15px;
}


.count {
    position: absolute;
    z-index: 999;
    right: 0;
    background-color: rgb(0, 0, 0, 0.5);
    width: 20%;
    height: 40px;
    font-size: 22px;
    display: flex;
    align-items: center;
    padding: 0 5px;
}
</style>