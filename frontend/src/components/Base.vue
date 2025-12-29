<template>
    <input-section @weather-data-submitted="getWeatherData"/>
    <div v-if="isLoading">
        Loading data...
    </div>
    <div v-else-if="weatherResponse">
        <outputSection :data="weatherResponse"/>
    </div>
    <div v-else>

    </div>
</template>

<script scoped>
    import inputSection from './inputSection.vue';
    import outputSection from './outputSection.vue';

    export default {
        name: 'Base',
        components: {
            inputSection,
            outputSection
        },
        data () {
            return {
                weatherResponse: null,
                isLoading: false
            }
        },
        methods: {
            getWeatherData(data) {
                this.isLoading = true;
                const urlParams = new URLSearchParams()
                var url = new URL('http://localhost:8000/get-weather-data')
                urlParams.set('location', data.inputLocation);
                urlParams.set('start_date', data.startDate);
                urlParams.set('end_date', data.endDate);
                const queryString = urlParams.toString();
                url = url + '?' + queryString

                fetch(url).then(response => {
                    if (!response.ok) {
                        throw new Error("Error fetching weather data.");
                    }
                    return response.json();
                })
                .then(data => {
                    this.isLoading = false;
                    this.weatherResponse = data.data
                })
            },
        }
    }
</script>