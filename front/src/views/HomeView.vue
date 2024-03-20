<template>
  <div class="home">
    <Section1 :backgroundImage="imageUrl" :msg="$t('interface.home.slide')" />
    <!-- <Section2 /> -->
    <Section2Test />
    <Section3 />
    <Section4 />
    <Section5 />
    <Section6 />
  </div>
</template>
<style></style>
<script>
// @ is an alias to /src
import Section1 from '@/components/Section1.vue';
import Section2 from '@/components/Section2.vue';
import Section2Test from '@/components/Section2Test.vue'
import Section3 from '@/components/Section3.vue';
import Section4 from '@/components/Section4.vue';
import Section5 from '@/components/Section5.vue';
import Section6 from '@/components/Section6.vue';

export default {
  name: 'HomeView',
  components: {
    Section1,
    Section2,
    Section2Test,
    Section3,
    Section4,
    Section5,
    Section6
  },
  data() {
    return {
      imageUrl: new URL('/src/assets/sshas.jpg', import.meta.url),
      backgroundImageUrl: './assets/sshas.jpg;', // Replace with the actual image URL
    };

  }
}
</script>
