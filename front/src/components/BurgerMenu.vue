<template>
    <div class="links">
        <Slide right :closeOnNavigation="true">
            <div class="lang">
                <a href="" @click.prevent="setLocale('en-EN')">EN</a>
                <a href="" @click.prevent="setLocale('ru-RU')">RU</a>
            </div>
            <router-link to="/familyservices">{{ $t('interface.navigate.service.family') }}</router-link>
            <router-link to="/anotherservices">{{ $t('interface.navigate.service.another') }}</router-link>
            <router-link to="/checkforms">{{ $t('interface.navigate.service.check_form') }}</router-link>

            <router-link :to="{ path: '/', hash: '#section3_container' }">{{ $t('interface.navigate.case') }}</router-link>

            <a href="tel:(480) 465 2531">(480) 465 2531</a>

        </Slide>
    </div>
</template>

<script>
import { Slide } from 'vue3-burger-menu'  // import the CSS transitions you wish to use, in this case we are using `Slide`


export default {
    components: {
        Slide, // Register your component


    },
    methods: {
        setLocale(locale) {
            localStorage.setItem('locale', locale);
            this.$i18n.locale = locale
        }
    }
}
</script>
<style scoped>
.links a {
    color: white;
    white-space: nowrap;
}

.lang a:last-child {
    margin-left: 10px;
}
</style>