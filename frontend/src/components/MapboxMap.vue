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

            console.log({
'type': 'FeatureCollection',
'features': [
{
'type': 'Feature',
'properties': {
'description':
'<strong>Make it Mount Pleasant</strong><p><a href="http://www.mtpleasantdc.com/makeitmtpleasant" target="_blank" title="Opens in a new window">Make it Mount Pleasant</a> is a handmade and vintage market and afternoon of live entertainment and kids activities. 12:00-6:00 p.m.</p>',
'icon': 'theatre-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.038659, 38.931567]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Mad Men Season Five Finale Watch Party</strong><p>Head to Lounge 201 (201 Massachusetts Avenue NE) Sunday for a <a href="http://madmens5finale.eventbrite.com/" target="_blank" title="Opens in a new window">Mad Men Season Five Finale Watch Party</a>, complete with 60s costume contest, Mad Men trivia, and retro food and drink. 8:00-11:00 p.m. $10 general admission, $20 admission and two hour open bar.</p>',
'icon': 'theatre-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.003168, 38.894651]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Big Backyard Beach Bash and Wine Fest</strong><p>EatBar (2761 Washington Boulevard Arlington VA) is throwing a <a href="http://tallulaeatbar.ticketleap.com/2012beachblanket/" target="_blank" title="Opens in a new window">Big Backyard Beach Bash and Wine Fest</a> on Saturday, serving up conch fritters, fish tacos and crab sliders, and Red Apron hot dogs. 12:00-3:00 p.m. $25.grill hot dogs.</p>',
'icon': 'bar-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.090372, 38.881189]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Ballston Arts & Crafts Market</strong><p>The <a href="http://ballstonarts-craftsmarket.blogspot.com/" target="_blank" title="Opens in a new window">Ballston Arts & Crafts Market</a> sets up shop next to the Ballston metro this Saturday for the first of five dates this summer. Nearly 35 artists and crafters will be on hand selling their wares. 10:00-4:00 p.m.</p>',
'icon': 'art-gallery-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.111561, 38.882342]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Seersucker Bike Ride and Social</strong><p>Feeling dandy? Get fancy, grab your bike, and take part in this year\'s <a href="http://dandiesandquaintrelles.com/2012/04/the-seersucker-social-is-set-for-june-9th-save-the-date-and-start-planning-your-look/" target="_blank" title="Opens in a new window">Seersucker Social</a> bike ride from Dandies and Quaintrelles. After the ride enjoy a lawn party at Hillwood with jazz, cocktails, paper hat-making, and more. 11:00-7:00 p.m.</p>',
'icon': 'bicycle-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.052477, 38.943951]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Capital Pride Parade</strong><p>The annual <a href="http://www.capitalpride.org/parade" target="_blank" title="Opens in a new window">Capital Pride Parade</a> makes its way through Dupont this Saturday. 4:30 p.m. Free.</p>',
'icon': 'rocket-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.043444, 38.909664]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Muhsinah</strong><p>Jazz-influenced hip hop artist <a href="http://www.muhsinah.com" target="_blank" title="Opens in a new window">Muhsinah</a> plays the <a href="http://www.blackcatdc.com">Black Cat</a> (1811 14th Street NW) tonight with <a href="http://www.exitclov.com" target="_blank" title="Opens in a new window">Exit Clov</a> and <a href="http://godsilla.bandcamp.com" target="_blank" title="Opens in a new window">Gods’illa</a>. 9:00 p.m. $12.</p>',
'icon': 'music-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.031706, 38.914581]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>A Little Night Music</strong><p>The Arlington Players\' production of Stephen Sondheim\'s  <a href="http://www.thearlingtonplayers.org/drupal-6.20/node/4661/show" target="_blank" title="Opens in a new window"><em>A Little Night Music</em></a> comes to the Kogod Cradle at The Mead Center for American Theater (1101 6th Street SW) this weekend and next. 8:00 p.m.</p>',
'icon': 'music-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.020945, 38.878241]
}
},
{
'type': 'Feature',
'properties': {
'description':
'<strong>Truckeroo</strong><p><a href="http://www.truckeroodc.com/www/" target="_blank">Truckeroo</a> brings dozens of food trucks, live music, and games to half and M Street SE (across from Navy Yard Metro Station) today from 11:00 a.m. to 11:00 p.m.</p>',
'icon': 'music-15'
},
'geometry': {
'type': 'Point',
'coordinates': [-77.007481, 38.876516]
}
}
]
})

            map.addSource('places', {
                'type': 'geojson',
                'data': data

            })

            map.addLayer({
                'id': 'places',
                'type': 'circle',
                'source': 'places',
                'paint': {
                    'circle-radius': 6,
                    'circle-color': '#B42222'
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