<template>
    <div>
        <div class="input-area">
            <label for="input-location">Location</label>
            <input id="input-location" type="text" v-model="inputLocation" placeholder="Enter Location" />
            <label for="start-date">Start Date</label>
            <input id="start-date" type="text" v-model="startDate" placeholder="Enter Start Date" />
            <label for="end-date">End Date</label>
            <input id="end-date" type="text" v-model="endDate" placeholder="Enter End Date" />

            <button @click="submitInput">Submit</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'inputSection',
        data () {
            return {
                inputLocation: '',
                startDate: '',
                endDate: ''
            }
        },
        methods: {
            submitInput() {
                var inputWeatherData = {
                    "inputLocation": this.inputLocation,
                    "startDate": this.startDate,
                    "endDate": this.endDate
                }
                this.$emit('weather-data-submitted', inputWeatherData)
            }
        }
    }
</script>

<style scoped>

</style>