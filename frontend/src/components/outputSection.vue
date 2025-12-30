<template>
    <div v-if="data">
        <h2>{{ data.address }}</h2>
        <div style="display: flex">
            <day-card v-for="item in data.days" :weather-data="item" />
        </div>
    </div>
</template>

<script setup>
    import dayCard from './dayCard.vue';

    const props = defineProps({
        data: {
            type: Object,
            required: true
        }
    })
</script>