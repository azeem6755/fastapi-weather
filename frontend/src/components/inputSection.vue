<template>
    <div>
        <div class="input-area">
            <div class="input-group mb-3 input-item">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-default">Location</span>
                </div>
                <input id="input-location" class="form-control" type="text" v-model="inputLocation"/>
            </div>
            <div class="input-group mb-3 input-item">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-default">Start Date</span>
                </div>
                <input id="start-location" class="form-control" type="date" v-model="startDate" />
            </div>
            <div class="input-group mb-3 input-item">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-default">End Date</span>
                </div> 
                <input id="end-date" class="form-control" type="date" v-model="endDate" />
            </div>

            <button class="btn btn-outline-primary btn-lg submit-btn" @click="submitInput" type="submit">Submit</button>
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
    .input-area {
        border: 2px solid yellow;
        padding: 1em;
        display: flex;
        margin: 1em 0 1em 0;
        justify-content: space-evenly;
    }

    .input-item {
        flex: 1;
        margin: 0 1%
    }

    .submit-btn {
        padding: 0 2em;
    }

</style>