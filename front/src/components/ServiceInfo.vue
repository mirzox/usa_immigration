<template>
    <div class="service_containter">
        <div class="title_texts">
            <span> {{ $t('interface.serviceinfo.title') }}</span>
        </div>
        <div v-if="responseData === null" class="loaders">
            <div class="loader"></div>
        </div>
        <div v-else class="service_info">
            <div class="info_block" v-for="item in responseData" :key="item.id">
                <div class="left">
                    <div class="title_info" ><b>{{ $i18n.locale == 'ru-RU' ? item.title_ru : item.title_en }}</b></div>
                    <div class="text">{{ $i18n.locale == 'ru-RU' ? item.title_description_ru : item.title_description_en }}</div>
                </div>
                <div class="right">
                    <div class="button">
                        <Modal :id="item.id" :data="item" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Modal from '@/components/Modal.vue';
export default {
    name: 'FamilyInfo',
    components: {
        Modal
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
            axios.get('https://vladicusa.com/api/another_service/')
                .then(response => {
                    this.responseData = response.data;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }
    }
}
</script>
<style scoped>
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

.title_info {
    font-size: 20px;
}

.title_texts {
    display: flex;
    justify-content: center;
    font-size: 20px;
    margin: 30px 0px;
}

.service_info {
    max-width: 1600px;
    text-align: left;
    margin: auto;
    padding: 0px 120px;
}

.info_block {
    display: flex;
    background: rgb(108, 168, 62);
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    color: white;
    padding: 10px;
    margin-bottom: 5px;

}

.info_block:hover {
    background-color: #6E6C78;
}

.description {
    display: flex;
    justify-content: space-between;

}

.text {
    width: 85%;
    font-size:20px
}

@media (max-width: 780px) {
    .service_info {
        padding: 0px 30px;
    }

    .description {
        flex-direction: column;
    }

    .button {
        margin-top: 20px;
    }

    .service_form input {
        padding: 15px 30px;
    }
    .info_block {
        flex-direction: column;
    }
}
</style>