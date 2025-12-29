<template>
    <div v-if="data">
        <p>{{ data }}</p>
    </div>
</template>

<script setup>
    const props = defineProps({
        data: {
            type: Object,
            required: true
        }
    })
</script>