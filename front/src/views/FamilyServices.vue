<template>
    <Section1 :backgroundImage="imageUrl" :msg="$t('interface.family_immigration.service')" />
    <FamilyInfo />
    <Section6 />
</template>

<script>
import Section1 from '@/components/Section1.vue';
import Section6 from '@/components/Section6.vue';
import FamilyInfo from '@/components/FamilyInfo.vue';


export default {
    name: 'AnotherServices',
    components: {
        Section1,
        FamilyInfo,
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