<template>
    <div class="section3_container" id="section3_container">
        <div class="section3">
            <div class="section3_title">
                <span class="sec3_title">{{ $t('interface.section2.title.title') }}</span>
                <br>
                <span class="sec3_sub">{{ $t('interface.section2.title.sub_title') }}</span>
                <br>
            </div>
            <div class="section3_blocks">
                <div class="block bl1">
                    <div class="block_image"><img src="../assets/delivery.png" alt="" srcset=""></div>
                    <div class="block_label">{{ $t('interface.section3.title.collecting_informatiom') }}</div>
                    <div class="block_text">{{ $t('interface.section3.description.collecting_informatiom') }}</div>
                </div>
                <div class="block bl2">
                    <div class="block_image"><img src="../assets/case.png" alt="" srcset=""></div>
                    <div class="block_label">{{ $t('interface.section3.title.researchig_case') }} </div>
                    <div class="block_text">{{ $t('interface.section3.description.researchig_case') }}
                    </div>
                </div>
                <div class="block bl3">
                    <div class="block_image"><img src="../assets/info.png" alt="" srcset=""></div>
                    <div class="block_label">{{ $t('interface.section3.title.check_forms') }}</div>
                    <div class="block_text">{{ $t('interface.section3.description.check_forms') }}</div>
                </div>
                <div class="block bl4">
                    <div class="block_image"><img src="../assets/sub.png" alt="" srcset=""></div>
                    <div class="block_label">{{ $t('interface.section3.title.send_case') }}</div>
                    <div class="block_text">{{ $t('interface.section3.description.send_case') }}</div>
                </div>
            </div>
        </div>
    </div>
    <hr>
</template>
<script>
// @ is an alias to /src

export default {
    name: 'Section3',
}
</script>
<style scoped>
.section3_title {
    font-size: 2.3vw;
    font-weight: 00;
    margin-bottom: 50px;
}

.section3_container {
    /* background-color: rgb(188, 227, 204); */
    background-color: white;
}

.section3 {
    display: flex;
    flex-direction: column;
    max-width: 1600px;
    margin: auto;
    padding: 60px;

}

.section3_blocks {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}

.block {
    /* border: 1px solid ; */
    width: 300px;
    height: 300px;
    /* margin: 5px; */
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #059a41;
    flex-direction: column;
    padding: 20px;
}

.sec3_title {
    font-weight: 900;
    font-size: 50px;
}

.sec3_sub {
    color: rgb(123, 178, 80);
    font-weight: 300;
}

.bl1 {
    background-color: rgb(108, 168, 62);
    transition: 0.3s;

}

.bl2 {
    background-color: rgb(93, 141, 53);
    transition: 0.3s;

}

.bl3 {
    background-color: rgb(78, 118, 45);
    transition: 0.3s;

}

.bl4 {
    background-color: rgb(61, 91, 38);
    transition: 0.3s;

}

.block_image {
    width: 100px;
}

.block_image img {
    width: 100%;
}

.block_label {
    color: white;
    font-size: 25px;
    font-weight: 700;
}

.block_text {
    color: white;
}

hr {
    border: 0px solid;
    padding: 0px;
    margin: 0px;
    background-color: #6E6C78;
    height: 3px;
}

.block:hover {
    background-color: #6E6C78;
}

@media (max-width: 850px) {
    .section3 {
        padding: 0px;

    }

    .block {
        width: 100%;
    }

    .section3_blocks {
        padding: 0px 10px;
    }
}

@media (max-width: 750px) {

    .section3_title {
        font-size: 5vw;
        padding-top: 20px;
    }


}

@media (max-width: 431px) {
    .block {
        width: 100%;
    }
    .sec3_title {
    font-size: 30px;
}
}
</style>