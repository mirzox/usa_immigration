<template>

    <div class="section1_container">
        <div :style="{ backgroundImage: `url('${backgroundImage}')` }" class="bg_section1">
            <div class="section1_text">
                <p v-html="msg"></p>
            </div>
        </div>
    </div>
</template>
<script>
// @ is an alias to /src

export default {
    name: 'Section1',
    props: {
        msg: String,
        backgroundImage: {
            type: String,
            required: true,
        },
    }
}
</script>
<style scoped>
.bg_section1 {
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    align-items: center;
}

.section1_text {
    color: white;
    padding: 9vw;
    max-width: 1400px;
    margin: auto;
}

.section1_text p {
    font-size: 5vw;
}

hr {
    border: 0px solid;
    padding: 0px;
    margin: 0px;
    background-color: #6E6C78;
    height: 3px;
}

@media (max-width: 431px) {
    .section1_text p {
        font-size: 6vw;
        margin-top: 6px;
    }
    .bg_section1 {
        height: 180px;
    }
}
</style>