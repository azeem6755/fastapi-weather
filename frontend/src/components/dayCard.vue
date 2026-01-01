<template>
    <div class="day-card col-sm" align="center">
        <div v-if="weatherData.icon==='clear-day'">
            <img class="weather-status" src="../../public/sun.png"/>
        </div>
        <div v-else-if="weatherData.icon==='partly-cloudy-day' || weatherData.icon==='cloudy'">
            <img class="weather-status" src="../../public/cloudy-day.png"/>
        </div>
        <div v-else-if="weatherData.icon==='rain'">
            <img class="weather-status" src="../../public/rainy.png"/>
        </div>
        <div v-else-if="weatherData.icon==='partly-cloudy-day'">
            <img class="weather-status" src="../../public/cloudy-day.png"/>
        </div>
        <div v-else-if="weatherData.icon==='snow'">
            <img class="weather-status" src="../../public/snowy.png"/>
        </div>
        <p>{{ weatherData.datetime }}</p>
        <p>Temperature {{ convertToCelcius(weatherData.temp) }}&deg;C</p>
        <p>Range: {{ convertToCelcius(weatherData.tempmin) }}&deg;C - {{ convertToCelcius(weatherData.tempmax) }}&deg;C</p>
        <p>{{ weatherData.description }}</p>
    </div>
</template>


<script setup>
    const props = defineProps({
        weatherData: {
            type: Object,
            required: true
        }
    })
    
    function convertToCelcius(temperature) {
        return ((temperature - 32) * (5/9)).toFixed(2);
    }
</script>

<style scoped>

    .weather-card-parent {
        display: flex;
        flex-direction: row;
    }

    .day-card {
        border: 1px solid red;
        padding: 1em 0 1em 0.5em;
        justify-content: center;
        align-items: center;
    }

    p {
        text-align:center;
    }

    .weather-status {
        height: 5em;
        width: auto;
    }
</style>
