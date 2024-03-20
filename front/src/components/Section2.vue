<template>
    <hr>
    <div class="section2_container">
        <div class="section2">
            <div class="section2_info">
                <div class="title">
                    <span>Vlad Mordukhovich</span>
                    <br>
                    <span>Иммиграционный Консультант</span>
                    <hr class="under">
                </div>
                <div class="title">
                    <span>{{$t('interface.section1.title')}}</span>
                    <br>
                    <br>
                    <span>Более 15 лет успешно помогаю людям преодолевать все этапы на иммиграционном пути в США.
                        <br>
                        <br>
                        Мой путь в США также, как и ваш начинался когда-то с мечты, но я эту мечту превратил в реальность.
                        Сейчас готов помочь в этом и Вам!
                        <br>
                        <br>
                        Весь свой иммиграционный путь, от выигрыша в DV лотерею «Green Card» в 2007 году до получения
                        гражданства США в 2013 году, я успешно прошел самостоятельно, так как обладаю необходимыми знаниями
                        и опытом. Являясь иммигрантом сам, я отлично понимаю и знаю, как бывает трудно найти правильные и
                        компетентные ответы на все возникающие вопросы, связанные с иммиграционным процессом и нюансами
                        жизни в США. Я уже нашел все ответы и теперь могу помочь сэкономить Вам время и деньги в этом
                        процессе.
                        <br>
                        <br>
                        Приехав в США, я работал в юридическом офисе помощником адвоката, также продолжительное время
                        работал в крупной международной некоммерческой организации, занимающейся помощью иммигрантам.
                        В данное время я готов предоставить Вам свои услуги, знания, опыт, профессионализм для того, чтобы
                        вы прошли свой иммиграционный путь легко, комфортно и по доступным ценам.
                    </span>
                </div>
            </div>
            <div class="section2_photo">
                <img src="../assets/vlad.png" alt="" srcset="">
            </div>
        </div>
    </div>
    <hr>
</template>
<script>
// @ is an alias to /src

export default {
    name: 'Section2',
}
</script>
<style scoped>
.section2_container {
    background-color: #7AA899;
    padding: 60px 0px;
}

.section2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    max-width: 1600px;
    margin: auto;
}

.section2_photo {
    display: flex;
    justify-content: center;
    align-items: center;
}

.section2_photo img {
    width: 100%;
    margin: 0px 120px 0px 0px;
}

.section2_info {
    padding: 0px 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    color: white;
}


.title {
    font-size: 1.3vw;
}

.title span:first-child {
    font-size: 2.5vw;
    font-weight: 800;
}

hr {
    border: 0px solid;
    padding: 0px;
    margin: 0px;
    background-color: #6E6C78;
    height: 3px;
}

.under {
    height: 1px;
    background-color: black;
    margin: 5px 0px;
}

@media (min-width: 2000px) {
    .title {
        font-size: 1vw;
    }

    .title span:first-child {
        font-size: 2vw;
    }

}

@media (max-width: 750px) {
    .title {
        font-size: 1vw;
    }

    .section2_info {
        padding: 0px 30px;
    }
}
</style>