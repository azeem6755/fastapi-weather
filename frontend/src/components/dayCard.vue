<template>
    <div class="day-card">
        <p>Temperature {{ convertToCelcius(weatherData.temp) }}&deg;C</p>
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
    }
</style>
