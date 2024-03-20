<template>
    <!-- Modal toggle -->
    <div class="service_form reverse">
        <input :data-modal-target="id + 'modal'" :data-modal-toggle="id + 'modal'" type="submit" :value="getTranslatedHTML('interface.modal.input_text')">
    </div>

    <!-- Main modal -->
    <div class="winds hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
        :id="id + 'modal'" tabindex="-1" aria-hidden="true">
        <div class="relative p-4 w-full max-w-2xl max-h-full topsf">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg  dark:bg-gray-700 opper">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 headerv">
                    <h3 v-html="($i18n.locale == 'ru-RU' ? data.title_ru : data.title_en)" class="text-xl font-semibold text-gray-900 dark:text-white ">

                    </h3>
                    <button class="buts" type="button" :data-modal-hide="id + 'modal'">
                        <img class="imgs" src="../assets/close.png" alt="" srcset="">
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4 bodyes">
                    <p v-html="$t('interface.modal.price') + ($i18n.locale == 'ru-RU' ? data.price_ru : data.price_en)" class="blolds"></p>
                    <p v-html="$t('interface.modal.tax') + ($i18n.locale == 'ru-RU' ? data.tax_ru : data.tax_en)" class="blolds"></p>
                    <p v-html="$t('interface.modal.includes') +($i18n.locale == 'ru-RU' ? data.description_ru : data.description_en)" class="blolds"></p>
                </div>
                <!-- Modal footer -->
                <div>
                    <div class="service_form">
                        <input :data-modal-hide="id + 'modal'" :data-modal-target="id + 'form-modal'"
                            :data-modal-toggle="id + 'form-modal'" type="submit"
                            :value="getTranslatedHTML('interface.modal.button_text')">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <Form :id="id" :data="data"></Form>
</template>
  
<script >
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import axios from 'axios';
import Form from './Form.vue';

export default {
    name: 'Section1',
    props: {
        id: Number,
        data: Object
    },
    components: {
        Form
    },
    data() {
        onMounted(() => {
            initFlowbite();
        })

    },
    methods: {
        getTranslatedHTML(translationKey) {
            const translatedText = this.$t(translationKey);
            return translatedText;
        },

    }
}

// initialize components based on data attribute selectors

</script>

<style scoped>
.topsf {
    padding: 0px !important;
}
.opper {
    padding: 20px !important;
}

.buts {
    background-color: rgba(0, 0, 0, 0);
    border: 0px;
    padding: 0px;
    margin: 0px;
    height: auto;
    width: auto;
    padding-block: 0px;
    padding-inline: 0px;
}

.winds div {
    padding: 10px;
    background-color: #fff;
    color: #000;
}

.headerv {
    padding: 0px;
    margin: 0px;
}

.headerv h3 {
    font-size: 25px;
    color: rgb(108, 168, 62);
}

.bodyes {
    padding: 0px;
    margin: 0px;
}

.imgs {
    width: 32px;
}

.blolds {
    font-size: 18px;
}

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


}

.service_form input:hover {
    background-color: rgb(55 65 81);
}

.reverse input {
    background-color: rgb(55 65 81);
    color: white;
}




@media (max-width: 780px) {

    .service_form input {
        padding: 15px 30px;
    }
}</style>


