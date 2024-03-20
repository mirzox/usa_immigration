<template>
    <Section1 :backgroundImage="imageUrl" :msg="$t('interface.another_services.service')" />
    <Form />
    <ServiceInfo />
    <Section6 />
</template>

<script>
import Section1 from '@/components/Section1.vue';
import Section6 from '@/components/Section6.vue';
import ServiceInfo from '@/components/ServiceInfo.vue';
import Form from '@/components/Form.vue';

export default {
    name: 'AnotherServices',
    components: {
        Section1,
        ServiceInfo,
        Section6,
        Form
    },
    data() {
        return {
            imageUrl: new URL('/src/assets/sshas.jpg', import.meta.url),
            backgroundImageUrl: './assets/sshas.jpg;', // Replace with the actual image URL,
        };

    },
}
</script>