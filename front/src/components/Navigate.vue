<template>
    <nav>
        <div class="navigate">
            <div class="nav_logo">
                <router-link to="/">
                    <div class="logo_image" id="logo_image"><img src="../assets/log.png" alt=""></div>
                </router-link>
            </div>
            <div class="nav_text">
                <div class="dropdown">
                    <router-link class="dropbtn" :to="{path:'/', hash: '#section5_container'}">{{$t('interface.navigate.service.title')}}</router-link>
                    <div class="dropdown-content">
                        <router-link to="/familyservices">{{$t('interface.navigate.service.family')}}</router-link>
                        <router-link to="/anotherservices">{{$t('interface.navigate.service.another')}}</router-link>
                        <router-link to="/checkforms">{{$t('interface.navigate.service.check_form')}}</router-link>

                    </div>
                </div>
                <div>

                    <router-link :to="{path:'/', hash: '#section3_container'}">{{$t('interface.navigate.case')}}</router-link>
                </div>
                <div class="tests">
                    <Contact />
                </div>
                <div>
                    <a href="" @click.prevent="setLocale('en-EN')">EN</a>
                    <a href="" @click.prevent="setLocale('ru-RU')">RU</a>
                </div>
                <div>

                </div>
                <div>
                    <a href="tel:(480)4652531">(480) 465 2531</a>
                </div>
            </div>
            <div class="nav_burger">
                <BurgerMenu />
            </div>

        </div>
    </nav>
</template>
<script>
import BurgerMenu from './BurgerMenu.vue';
import Contact from './Contact.vue';
export default {
    name: 'Navigate',
    components: {
        BurgerMenu,
        Contact
    },
    methods:{
        setLocale(locale) {
            localStorage.setItem('locale',locale);
            this.$i18n.locale = locale
        }
    }
}
</script>
<style scoped>

.work_with_case {
    white-space: nowrap;
}
.dropbtn {
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown a {
    font-size: 1.1vw;
}

.dropdown-content a {
    margin-left: 0px !important;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #6E6C78;
    min-width: 180px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-content a {
    color: white;
    padding: 12px 6px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #dddddd7e;
}

.dropdown:hover .dropdown-content {
    display: block;
}


nav {
    background-color: #6E6C78;
    padding: 15px 0px;
}

.navigate {
    display: flex;
    justify-content: space-between;
    max-width: 1600px;
    margin: auto;
    text-align: center;
    align-items: center;
    padding: 0px 120px;
}

.nav_logo a {
    width: 230px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;

}

.nav_logo img {
    max-width: 100%;
    height: auto;
    width: auto\9;
    /* margin: 10px; */
    /* ie8 */
}

.logo_border {
    height: 50px;
    border: 1px solid;
    margin: 0px 5px;
}

.logo_text {
    /* border-left: 1px solid; */
    /* padding: 10px; */
    text-align: left;
    font-size: 23px;
}

nav a {
    text-decoration: none;
    color: white;
    /* font-size: 18px; */
    font-size: 1.1vw;

}
nav a:hover {
    text-decoration: underline;

}
.nav_text {
    display: flex;

}


.nav_text a:nth-child(-n+5) {
    margin-left: 30px;
}

.nav_text a:last-child {
    margin-left: 20px;
}

.nav_burger {
    display: none;
}


@media (max-width: 1100px) {
    .navigate {
        padding: 0px 70px;
    }
}

@media (max-width: 750px) {
    .nav_text {
        display: none;
    }

    .nav_burger {
        display: block;
        padding-right: 50px
    }

    .navigate {
        padding: 0px;
    }

    .nav_logo {
        padding-left: 10px;
    }
}
@media (max-width: 300px) {
.nav_logo a {
    width: 180px;
}
}
</style>
  