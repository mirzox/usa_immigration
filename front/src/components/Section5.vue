<template>
    <div class="section5_container" id="section5_container">
        <div class="section5">
            <div class="service_label">
                {{ $t('interface.section5.title') }}
            </div>
            <div class="services">
                <router-link to="/familyservices">

                    <div class="service">
                        <div class="service_image"><img src="../assets/sv1.png" alt="" srcset=""></div>
                        <div class="service_text">
                            <div class="service_title">
                                <h1>{{ $t('interface.section5.service.title.family') }}</h1>
                            </div>
                            <div class="service_description">{{ $t('interface.section5.service.description.family') }}</div>
                        </div>
                    </div>
                </router-link>
                <router-link to="/anotherservices">
                    <div class="service">
                        <div class="service_image"><img src="../assets/sv2.jpg" alt="" srcset=""></div>
                        <div class="service_text">
                            <div class="service_title">
                                <h1>{{ $t('interface.section5.service.title.another') }}</h1>
                            </div>
                            <div class="service_description">{{ $t('interface.section5.service.description.another') }}</div>
                        </div>
                    </div>
                </router-link>
                <router-link to="/checkforms">
                    <div class="service">
                        <div class="service_image"><img src="../assets/sv3.jpg" alt="" srcset=""></div>
                        <div class="service_text">
                            <div class="service_title">
                                <h1>{{ $t('interface.section5.service.title.check_forms') }}</h1>
                            </div>
                            <div class="service_description">{{ $t('interface.section5.service.description.check_forms') }}
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
            <div class="service_form">
                <input type="submit" :data-modal-target="id + 'form-modal'" :data-modal-toggle="id + 'form-modal'"
                    :value="getTranslatedHTML('interface.form.button_text')">
            </div>
        </div>
    </div>
    <Form :id="id" :data="data"></Form>
</template>


<script>
import Form from './Form.vue';
export default {
    props: {
        id: Number,
        data: Object
    },
    components: {
        Form
    },
    methods: {
        getTranslatedHTML(translationKey) {
            const translatedText = this.$t(translationKey);
            return translatedText;
        },
    }

}
</script>



<style scoped>
a {
    text-decoration: none;
    color: black;
}

.section5 {
    max-width: 1600px;
    display: flex;
    justify-content: center;
    margin: auto;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

.service_label {
    font-weight: 900;
    font-size: 50px;
    text-align: left;
    display: flex;
    justify-content: left;
    align-items: center;
    margin: 15px;
}

.service_image img:hover {
    transform: scale(1.07);
}

.services {
    display: flex;
    justify-content: center;
    /* align-items: center; */

}

.service {
    /* width: 25vw; */
    max-width: 500px;
    text-align: left;
}

.service div {
    margin: 0px 10px;
}

.service_image img {
    width: 100%;
    border-radius: 30px;
    transition: transform .2s;

}

.service_form {
    margin: 15px 0px;

}

.service_form input {
    background-color: #6E6C78;
    border: 0px solid;
    border-radius: 10px;
    color: white;
    padding: 15px;
    font-size: 20px;
    cursor: pointer;
    transition: 0.3s;

}

.service_description {
    max-width: 500px;
    font-size: 26px;
}

.service_form input:hover {
    background-color: rgb(108, 168, 62);
}


@media (max-width: 900px) {
    .section5 {
        display: flex;
    }

    .service_label {
        font-size: 8vw;
    }

    .services {
        display: flex;
        flex-direction: column;
    }



    .service {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: left;
        margin-bottom: 50px;
    }

    .service_description {
        font-size: 20px;
    }

    .service_image {
        max-width: 100%;
    }

    .service_image img:hover {
        transform: scale(1);
    }
}
@media (max-width: 431px) {
    .service_label {
        font-size: 30px;
        margin-bottom: 50px;
    }
    .service_title{
        font-size: 15px;
    }
}
</style>