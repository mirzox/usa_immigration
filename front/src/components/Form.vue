<template>
    <div class="winds hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
        :id="id + 'form-modal'" tabindex="-1" aria-hidden="true">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <div class="close_windows" :data-modal-hide="id + 'form-modal'">
                        <img src="../assets/close.png" alt="">
                    </div>
            <div class="relative bg-white rounded-lg  dark:bg-gray-700 opper">
                <form class="max-w-sm mx-auto" @submit.prevent="sendMessage">
                 
                    <div class="grid md:grid-cols-2 md:gap-6">
                        <div>
                            <label for="text"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('interface.form.inputs.name') }}</label>
                            <input v-model="name" type="text" id="name"
                                class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" />
                        </div>
                        <div>
                            <label for="text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('interface.form.inputs.phone')}}
                            </label>
                            <input v-model="phoneNumber" type="text" id="phone"
                                class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" />
                        </div>
                    </div>
                    <div class="mb-5">
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('interface.form.inputs.email')}}</label>
                        <input v-model="email" type="text" id="text"
                            class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                            placeholder="name@flowbite.com" />
                    </div>

                    <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"> {{ $t('interface.form.inputs.add')}}
                    </label>
                    <textarea v-model="additionalMessage" id="message" rows="4"
                        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        :placeholder="getTranslatedHTML('interface.form.inputs.placeholer')"></textarea>
                    <button :data-modal-hide="id + 'form-modal'" type="submit" class="checls">{{ $t('interface.form.inputs.button_text')}}</button>
                </form>
            </div>
        </div>
    </div>
</template>
<style>
.close_windows {
    display: flex;
    justify-content: flex-end;
}
.close_windows img {
    width: 32px;
}
.checls {
    background-color: rgb(108, 168, 62);
    border: 0px solid;
    border-radius: 10px;
    color: white;
    padding: 15px;
    font-size: 17px;
    cursor: pointer;
    transition: 0.3s;
}

.checls:hover {
    background-color: #6E6C78;
}

.winds div {
    background: #fff;
}

form label {
    color: rgb(108, 168, 62) !important;
    font-size: 20px !important;
    padding: 4px;
}

button {
    margin-top: 20px
}

@media (max-width: 480px) {
    form input {
        padding: 10px 2px !important;
    }

    form textarea {
        padding: 2px !important;
    }
}
</style>
<script >

import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import axios from 'axios';
import ServicePrice from './ServicePrice.vue';
export default {
    name: 'Section1',
    props: {
        id: Number,
        data: Object
    },
    components: {
        ServicePrice
    },
    data() {
        return {
            name: '',
            phoneNumber: '',
            email: '',
            additionalMessage: '',
        },
            onMounted(() => {
                initFlowbite();
            })

    },
    methods: {
    async sendMessage() {
        try {
            const HTTP_API_TOKEN = '7108177200:AAEQYXFIrzAH_4g7B3wPlRv50UOCA71Qo6c';
            const CHAT_ID = '-1002042926253';
            let titles =  this.$i18n.locale == 'ru-RU' ? this.data?.title_ru : this.data?.title_en
            const title = '<b>Услуга</b>: ' + titles
            // Check if all required fields are not empty
            if (this.name && this.phoneNumber) {
                const MESSAGE_TEXT = `
                    ${!!this.data?.title_ru ? title : ''}
<b>Имя</b>: ${this.name}
<b>Номер телефона</b>: ${this.phoneNumber}
<b>Email</b>: ${this.email ? this.email : ''}
<b>Дополнительная информация</b>: ${this.additionalMessage ? this.additionalMessage : ''}
                `;

                const apiUrl = `https://api.telegram.org/bot${HTTP_API_TOKEN}/sendMessage?chat_id=${CHAT_ID}&text=${encodeURIComponent(MESSAGE_TEXT)}&parse_mode=HTML`;

                const response = await axios.get(apiUrl);
                if (response.status === 200) {
                    // Alert window for successful message
                    alert('Сообщение отправлено');
                } else {
                    // Handle other HTTP response statuses if needed
                    alert('Error sending message. Unexpected status:');
                }
            } else {
                // Handle the case when some of the required fields are empty
                alert('Заполните все поля!');
            }
        } catch (error) {
            // Handle the error, e.g., show an error message to the user.
            console.error('Error sending message:', error.message);
        }
    },
    getTranslatedHTML(translationKey) {
      // Предполагается, что у вас есть функция i18n для получения перевода по ключу
      const translatedText = this.$t(translationKey);

      // Возвращаем HTML
      return translatedText;
    },
},


};

// initialize components based on data attribute selectors

</script>