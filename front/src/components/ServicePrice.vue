<template>
    <div class="service_container">
        <div class="title_texts">
            <span>{{ $t('interface.serviceprice.title') }}</span>

        </div>
        <div class="texts">
            <span v-html="$t('interface.serviceprice.sub_title')" class="description">
                    
            </span>
        </div>

        <h1>{{ $t('interface.serviceprice.service') }}</h1>
        <div v-if="responseData === null" class="loaders">
            <div class="loader"></div>
        </div>
        <div v-else class="pricing-container">
            <div class="pricing highlight" v-for="item in responseData" :key="item.id">
                <h1>{{ $i18n.locale == 'ru-RU' ? item.title_ru : item.title_en }}</h1>
                <!-- <small class="green">Most Popular</small> -->
                <h2>${{ $i18n.locale == 'ru-RU' ? item.price_ru : item.price_en }}</h2>
                <ul>
                    <li v-html="getLocaleText(item)"></li>
                </ul>
                <div class="service_form reverse">
                    <input :data-modal-target="item.id + 'forms_modal'" :data-modal-toggle="item.id + 'forms_modal'"
                        type="submit" :value="getTranslatedHTML('interface.form.button_text')">
                </div>
                <TempModal :id="item.id" :data="item"></TempModal>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import TempModal from './TempModal.vue';
export default {
    name: 'ServicePrice',
    props: {
        id: Number,
        data: Object
    },
    components: {
        TempModal
    },
    data() {

        return {
            responseData: null,
        };

    },
    mounted() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            axios.get('https://vladicusa.com/api/service/')
                .then(response => {
                    this.responseData = response.data;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        },
        getTranslatedHTML(translationKey) {
            const translatedText = this.$t(translationKey);
            return translatedText;
        },
        getLocaleText(item) {
            return this.$i18n.locale == 'ru-RU' ? this.$t(item.text_ru) : this.$t(item.text_en)
            
    }
    }
}
</script>
<style scoped>
.service_form {
    display: flex;
    justify-content: center;
    align-items: center;
}

.service_form input {
    background-color: rgb(108, 168, 62);
    border: 0px solid;
    border-radius: 10px;
    color: white;
    padding: 15px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
    margin-bottom: 30px;
}

.title_texts {
    display: flex;
    justify-content: center;
    font-size: 20px;
    margin-top: 30px;
}

.loaders {
    display: flex;
    justify-content: center;
}

.loader {
    border: 8px solid #f3f3f3;
    border-radius: 50%;
    border-top: 8px solid rgb(108, 168, 62);
    width: 60px;
    height: 60px;
    -webkit-animation: spin 5s linear infinite;
    /* Safari */
    animation: spin .5s linear infinite;
    margin: 10px 0px 20px 0px;
}

/* Safari */
@-webkit-keyframes spin {
    0% {
        -webkit-transform: rotate(0deg);
    }

    100% {
        -webkit-transform: rotate(360deg);
    }
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.service_container {
    margin: 0px 10px;
    max-width: 1700px;
    margin: auto;
}

* {
    box-sizing: border-box;
}

.texts {
    max-width: 1300px;
    margin: auto;
    text-align: left;
    font-size: 20px;
    /* margin-top: 30px; */
}

.description {
    margin: auto;
    flex-direction: column;
}

body {
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Roboto', sans-serif;
    margin-bottom: 60px;
}

.pricing-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 10px 0px;

}

.pricing input {
    transition: transform .1s;

}

.pricing input:hover {
    transform: scale(1.07);
}

.pricing {
    background-color: #fff;
    border: 1px solid #eee;
    margin: 10px;
    text-align: center;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
}

.pricing.highlight {
    border-top: 2px solid #50BC01;
    box-shadow: 0 0 30px 10px rgba(0, 0, 0, 0.1);
}

.pricing h1 {
    color: rgb(108, 168, 62);
    margin: 30px 0 0;
}

.pricing small.green+h1 {
    margin-top: 10px;
}

.pricing small {
    color: #777;
}

.pricing ul {
    list-style-type: none;
    padding: 0;
    margin: 0px 0px 40px 0px;
    font-size: 20px;
}

.pricing ul li {
    margin: 0px 30px;
    max-width: 250px;
}

.pricing input {
    background-color: rgb(108, 168, 62);
    border: 0;
    border-radius: 2px;
    color: #fff;
    padding: 12px 20px;
    margin-bottom: 30px;
    font-size: 20px;
}



@media (max-width: 480px)  {

    .social-panel-container.visible {
        transform: translateX(0px);
    }

    .floating-btn {
        right: 10px;
    }
    .texts {
        margin: 0px 20px;
    }

}
</style>