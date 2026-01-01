<template>
    <div v-if="data" class="container-fluid">
        <h2 class="header">{{ data.address }}</h2>
        <div class="row">
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

<style scoped>
    .header {
        text-align: center;
    }
</style>
