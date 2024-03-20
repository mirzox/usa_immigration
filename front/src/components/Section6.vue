<template>
    <hr>
    <div class="section6_container">
        <div class="section6">
            <div class="footer">
                <div class="footer_menu">
                    <a href="#logo_image">  <div class="block logs"> <img src="../assets/log.png" alt="" srcset=""></div></a>
                    <div class="block"><span class="name">Vlad Mordukhovich</span></div>
                    <div class="block block_right"><span>{{ $t('interface.section6.contact') }}
                        </span>
                        <a href="tel:(480) 465 2531">(480) 465 2531</a>
                        <div class="block_image">
                            <div class="part1">
                                <a href="https://t.me/Vlad_Immigration"><img src="../assets/telegram.png" alt=""></a>
                                <a href="https://wa.me/14804652531"><img src="../assets/whatsapp.png" alt=""></a>
                                <a href="tel:(480) 465 2531"><img src="../assets/phone-call.png" alt=""></a>
                                <a href="mailto:vladicusa@gmail.com" target="_self"><img src="../assets/email.png" alt=""></a>
                            </div>
                            <div class="part1">
                                <img src="../assets/facebook.png" alt="">
                                <img src="../assets/instagram.png" alt="">
                                <img src="../assets/twitter.png" alt="">
                                <img src="../assets/youtube.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="footer_text">
                    <span v-html="$t('interface.section6.description')"></span>
                    Copyright © 2024 Vlad Mordukhovich
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.name {
    font-size: 25px;
}
.logs {
    width: 300px;
}
.section6_container {
    background-color: #6E6C78;
}

.section6 {
    max-width: 1600px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    font-size: 18px;
}

.footer {
    display: flex;
    flex-direction: column;
    padding: 0px 120px;
    margin: 20px 0px;
}

.footer_menu {
    display: flex;
    justify-content: space-between;
    margin: 50px 0px;
}
.footer_menu div{
 /* margin: 0px 50px; */
}

.block {
    display: flex;
    flex-direction: column;
    text-align: left;
    color: white;
}
.block a {
    color: white;
    text-decoration: none;
}
.block_right {
    text-align: right;
    font-size: 25px;
}

.block_image {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 20px;
}

.block_image img {
    width: 32px;
    margin: 5px;
}

.footer_text {
    text-align: center;
    color: white;
    margin-top: 20px;
}

hr {
    border: 0px solid;
    padding: 0px;
    margin: 0px;
    background-color: white;
    height: 3px;
}

@media (max-width: 750px) {
    .footer_menu {
        flex-direction: column;
        justify-content: left;
    }

    .block_right {
        text-align: left;
    }

    .block {
        margin: 10px 0px;
    }

    .block_image {
        display: block;

    }

    .block_image img {
        width: 48px;
        margin: 5px;
    }

    .footer {
        margin: 20px 0px;
        font-size: 20px;
        padding: 0px 10px;
    }
}
@media (max-width: 431px) {
.footer_text span {
    font-size: 14px;
}
}

@media (max-width: 300px) {
.logs {
    width: 200px;
}

}
</style>