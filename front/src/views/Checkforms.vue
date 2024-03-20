<template>
    <Section1 :backgroundImage="imageUrl" :msg="$t('interface.check_forms.service')" />
    <ServicePrice />
    <Section6 />
</template>

<script>
import Section1 from '@/components/Section1.vue';
import ServicePrice from '@/components/ServicePrice.vue'
import Section6 from '@/components/Section6.vue';
export default {
    name: 'Checkforms',
    components: {
        Section1,
        ServicePrice,
        Section6
    },
    data() {
        return {
            imageUrl: new URL('/src/assets/sshas.jpg', import.meta.url),
            backgroundImageUrl: './assets/sshas.jpg;', // Replace with the actual image URL,
        };

    },
}
</script>
<style scoped></style>