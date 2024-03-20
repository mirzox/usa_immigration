<template>
    <div class="section4_container">
        <div class="bg_section4">
            <div class="section4_text">
                <p v-html="$t('interface.section4.description')">
                </p>
            </div>
        </div>
    </div>
    <hr>
</template>
<script>
export default {
    name: 'Section4',
}
</script>


<style scoped>
.section4_container {
    background-image: url(../assets/sec4.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position-y: -50px;
}

.bg_section4 {
    max-width: 1600px;
    margin: auto;
}

.section4_text {
    color: white;
    padding: 5vw;
    max-width: 850px;
    /* margin: auto; */
    /* width: 850px; */
    text-align: right;
}

.section4_text p {
    text-align: left;
    font-size: 1.4vw;

    /* padding: 0px 60px; */
}

hr {
    border: 0px solid;
    padding: 0px;
    margin: 0px;
    background-color: #6E6C78;
    height: 3px;
}


@media (max-width: 900px) {

    .section4_text p {
        text-align: left;
        font-size: 4vw;
        padding: 0px 10px;

    }

    .bg_section4 {
        background-image: url(../assets/sec4.jpg);
        background-repeat: no-repeat;
        background-size: auto;
    }
    .section4_text {

    }


}
</style>