<template>
    <!-- Modal toggle -->
    <div class="service_form reverse">
        <a class="texts" :data-modal-target="id + 'contact-modal'" :data-modal-toggle="id + 'contact-modal'" type="submit">
            {{ $t('interface.navigate.contact') }}</a>
    </div>

    <!-- Main modal -->
    <div class="winds hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
        :id="id + 'contact-modal'" tabindex="-1" aria-hidden="true">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg  dark:bg-gray-700 opper">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 headerv">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white ">
                        {{ $t('interface.contacts.title') }}
                    </h3>
                    <button class="buts" type="button" :data-modal-hide="id + 'contact-modal'">

                        <img class="imgs" src="../assets/close.png" alt="" srcset="">
                    </button>
                </div>
                <!-- Modal body -->
                <div class="contact_body">
                    <div class="bodies">
                        <div class="name">
                            Vlad Mordukhovich
                        </div>
                        <div class="block_image">
                            <div class="part1">
                                <a href="https://t.me/Vlad_Immigration">
                                    <img src="../assets/telegram (1).png" alt=""></a>
                                <a href="https://wa.me/14804652531">
                                    <img src="../assets/whatsapp (1).png" alt=""></a>
                                <img src="../assets/facebook (1).png" alt=""><img src="../assets/social(1).png" alt="">
                            </div>
                        </div>
                        <div class="section_block">
                            <div class="block_texts">
                                <div class="block">
                                    <div class="tag">{{ $t('interface.contacts.phone') }}:</div>
                                    <div class="text"> <a href="tel:+(480) 465 2531">(480) 465 25 31</a></div>
                                </div>
                                <div class="block">
                                    <div class="tag">Email:</div>
                                    <div class="text"> <a href="mailto:vladicusa@gmail.com">vladicusa@gmail.com</a></div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal footer -->
                <div>
                    <div class="text_call">
                        <!-- <input :data-modal-hide="id + 'contact-modal'" type="submit" value="Позвозить"> -->
                        <a class="calls" href="tel:(480) 465 2531">{{ $t('interface.contacts.buttons') }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script >
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'


export default {
    name: 'Contact',
    props: {
        id: Number,
        data: Object
    },
    data() {
        onMounted(() => {
            initFlowbite();
        })
    }
}

// initialize components based on data attribute selectors

</script>

<style scoped>
.part1 {
    margin-top: 10px;
}

.tag {
    color: rgb(108, 168, 62) !important;
}

.section_block {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
    font-size: 20px;
}

.text {
    margin-left: 5px;
}
.text a {
    color: #000;
    text-decoration: none;
}
.block {
    display: flex;
}

.text_call {
    margin-top: 30px;
}

.name {
    padding: 0px !important;
    font-size: 24px;
    font-weight: 800;
}


.block_image {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 0px !important;
}

.block_image img {
    width: 32px;
    margin: 5px;
}

.texts {
    color: white;
    /* font-size: 18px; */
    font-size: 1.1vw;
    margin-left: 30px;
    cursor: pointer;
}

.opper {
    padding: 0px 20px 20px 20px !important;
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
    /* padding: 10px; */
    background-color: white;
    color: #000;
}

.headerv {
    padding: 0px;
    margin: 0px;
}

.headerv h3 {
    font-size: 25px;
    color: rgb(108, 168, 62);
    font-weight: 300;
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
    display: block;
}


.calls {
    background-color: rgb(108, 168, 62);
    border: 0px solid;
    border-radius: 10px;
    color: white;
    padding: 10px 15px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
    text-decoration: none;
    margin-top: 40px;
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

.reverse a:hover {
    text-decoration: underline;
}


@media (max-width: 780px) {

    .service_form input {
        padding: 15px 30px;
    }
}
</style>