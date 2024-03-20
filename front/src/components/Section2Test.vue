<template>
    <div class="section2_container" >
        <div class="section2">
            <div class="section2_title">
                <span class="name">Vlad Mordukhovich</span>
                <br>
                <span v-html="$t('interface.section1.name_description')" class="name_description"></span>
                <br>
                <span v-html="$t('interface.section1.description')" class="deal"></span>
            </div>
            <div class="section_body">
                <div class="section_left">
                    <div class="block bl1">
                        <div class="title"><img src="../assets/help.png" alt="" srcset="">{{ $t('interface.section1.title.experience.title') }}</div>
                        <div class="text">{{ $t('interface.section1.title.experience.description') }}
                        </div>
                    </div>
                    <div class="block bl2">
                        <div class="title"><img src="../assets/experience.png" alt="" srcset=""> {{ $t('interface.section1.title.way.title') }}</div>
                        <div class="text">{{ $t('interface.section1.title.way.description') }}
                        </div>
                    </div>
                    <div class="block bl3">
                        <div class="title"><img src="../assets/attorney.png" alt="" srcset="">{{ $t('interface.section1.title.usa.title') }}</div>
                        <div class="text">{{ $t('interface.section1.title.usa.description') }}
                        </div>
                    </div>
                </div>
                <div class="section_right">
                    <div class="photo"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.section2_container {
    background-color: #fff;
}
.section2 {
    max-width: 1600px;
    margin: auto;
    margin-top: 30px;
}

.section_body {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0px 120px;
}

.section_left {
    max-width: 700px;
}

.section_right {
    max-width: 800px;
}

.photo {
    width: 500px;
    /* border: 1px solid; */
    /* background-color: red; */
    height: 670px;
    background-image: url(../assets/vlad.png);
    background-size: cover;
    background-position: center;
    border-radius: 10px;
}

.block {
    border: 1px solid;
    padding: 20px;
    text-align: left;
    color: white;
    border-radius: 10px;
}

.title {
    font-size: 30px;
    font-weight: 800;
    display: flex;
    align-items: center;

}
.title img{
 width: 48px;
 margin-right: 15px;
}
.text {
    font-size: 18px;
}

.section2_title {
    margin-bottom: 10px;
}

.name {
    font-size: 35px;
    font-weight: 600;
}
.name_description {
    font-size: 18px;
}
.deal {
    color: rgb(123, 178, 80);
    font-size: 40px;
    font-weight: 200;
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

.block:hover {
    background-color: #6E6C78;
}

@media(max-width: 1200px) {
    .section_body {
        flex-wrap: wrap-reverse;

        justify-content: center;
    }
}

@media(max-width: 850px) {
    .section_body {
        justify-content: center;
        padding: 0px 10px;
    }

    .photo {
        width: 60vw;
        height: 400px;
    }

    .title {
        font-size: 30px;
    }
}

@media(max-width: 430px) {
    .section_body {
        padding: 0px;
    }

    .photo {
        width: 72vw;
    }

    .section2 {
        margin-top: 5px;
    }

    .title {
        font-size: 27px;
    }

    .deal {
        font-size: 19px;
    }

}</style>    