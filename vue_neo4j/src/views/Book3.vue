<template>
  <div class="scene">
    <article class="book">
      <div class="page active">
        <div class="front" style="margin-top: 30px">
          <header class="htmleaf-header3">
            <h1 style="font-family:Algerian">Harry Potter<br/>The Third<br/>Part</h1>
            <div class="htmleaf-links">
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/book2" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>

          <h1 style="font-family:'Agency FB';">The meaning of Harry Potter</h1>
          <p style="font-family:cursive">
            &nbsp;&nbsp;《哈利·波特》虽然是一部以魔幻为主题的儿童文学小说，却超出了儿童魔幻世界，有着深刻的现实意义。小说中一方面反映了人类生存过程中的普遍境遇:
            混乱与和平,磨难与成长，失去与收获﹐失败与成功;另一方面呈现了人类生活过程中的精神历程:幼稚与成熟，困惑与领悟，恐惧与淡定，绝望与希望。
            而本文通过对小说中选择，磨难和“爱”的浅析，发现《哈利·波特》是现实意义与文学艺术高度结合的产物，无论是对青少年还是对教师,
            都有极强的教育意义。
          </p>
          <br>
          <p style="font-family:cursive">
            &nbsp;&nbsp;正如托尔金在《魔戒》认为现实世界是第一世界，文学“幻想”创作是第二世界，并表述:“第二世界的所有规则都是以看得见的‘真实’建构起来的，
            尽管表面上看起来第二世界是非现实的产物，但绝非谎言，而是真实地反映了第一世界”6'由此可见，艺术虽高于生活，却是源于生活，更应益于生活，
            文学创作亦是如此。在欣赏文学作品的同时，更应学习文学作品中的深刻现实意义。
          </p>

        </div>
        <div class="back">
          <h1 style="font-family:Algerian">– The Clubs Of HarryPotter –</h1>
          <div>
            <el-row :gutter="70">
              <el-col :span="10">
                <el-card shadow="hover">
                  <img src='../assets/img/狮院.png' width="120px" height="130px" style="border-radius: 50%" title="格兰芬多学院">
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card shadow="hover">
                  <img src='../assets/img/鹰院.png' width="120px" height="130px" style="border-radius: 50%" title="拉文克劳学院">
                </el-card>
              </el-col>
            </el-row>
            <br>
            <el-row :gutter="70">
              <el-col :span="12">
                <el-card shadow="hover">
                  <img src='../assets/img/蛇院.png' width="120px" height="130px" style="border-radius: 50%" title="斯莱特林学院">
                </el-card>
              </el-col>
              <el-col :span="10">
                <el-card shadow="hover">
                  <img src='../assets/img/獾院.png' width="120px" height="130px" style="border-radius: 50%" title="赫奇帕奇学院">
                </el-card>
              </el-col>
            </el-row>
            <br>
            <el-row :gutter="70">
              <el-col :span="10">
                <el-card shadow="hover">
                  <img src='../assets/img/魁地奇.png' width="130px" height="130px" style="border-radius: 50%" title="魁地奇">
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card shadow="hover">
                  <img src='../assets/img/火焰杯.png' width="120px" height="130px" style="border-radius: 50%" title="火焰杯">
                </el-card>
              </el-col>
            </el-row>
          </div>

        </div>
      </div>

      <div class="page">
        <div class="front">
          <h1 style="font-family: Algerian,serif">– The Member Of Clubs –</h1>
          <statistics></statistics>
        </div>
        <div class="back">
          <h1 style="font-family: Algerian,serif">– Statistics of book –</h1>
          <book-sta></book-sta>
        </div>
      </div>

      <div class="page">
        <div class="front">
          <h1 style="font-family: Algerian,serif">– Statistics of word –</h1>
          <word-sta></word-sta>
        </div>
        <div class="back">
          <header class="htmleaf-header3" style="margin-top: 30px">
            <h3 style="font-family:Algerian">Thanks To Watching!</h3>
            <h3 style="font-family:Algerian">Harry Potter Part 3 End!</h3>
            <div class="htmleaf-links">
              <!--              <a class="htmleaf-icon icon-htmleaf-home-outline" href="/" target="_blank"></a>-->
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>
          <div style="margin-top: 20px">
            <img src='../assets/img/img_end2.jpg' style="width: 400px;height: 320px">
          </div>
        </div>
      </div>

    </article>
    <div style="padding-top: 100px;padding-left: 20px">
      <h1 style="font-family:'Agency FB';margin-top: 30px;color: white">Thank you very much for watching. That's all the content of Harry Potter.</h1>
      <p style="font-family:'Agency FB';font-size: 30px;color: white">
        &nbsp;&nbsp;The <router-link to="/book1" style="color: white;">first</router-link> part is about the complicated relationship between all the characters and related queries.<br/>
        &nbsp;&nbsp;The <router-link to="/book2" style="color: white;">second</router-link> part is the display of the detailed information of the main characters and the playback of classic clips.<br/>
        &nbsp;&nbsp;The <router-link to="/book3" style="color: white;">third</router-link> part shows the number of major organizations and colleges in the whole data set.
      </p>
      <pre style="font-family:Algerian;margin-top: 25px;color: white">                                                                    --《HarryPotter》</pre>
    </div>
  </div>
</template>

<script>


import  '../assets/js/jquery-1.11.0.min.js'
import $ from 'jquery'
import statistics from "@/components/statistics";
import bookSta from "@/components/bookSta";
import wordSta from "@/components/wordSta";

function nextPage() {
  $('.active')
      .removeClass('active')
      .addClass('flipped')
      .next('.page')
      .addClass('active')
      .siblings();
}

function prevPage() {
  $('.flipped')
      .last()
      .removeClass('flipped')
      .addClass('active')
      .siblings('.page')
      .removeClass('active');
}

export default {
  name: 'HomeView',
  components: {
    statistics,bookSta,wordSta
  },
  data() {
    return {
      currentPage: 0,
      input: '',
      data: '',
      tableData: [],
    }
  },
  mounted() {
    /*左键双击翻页*/
    $('.book')
        .on('dblclick', '.active', nextPage)
        .on('dblclick', '.flipped', prevPage);

    $('.book').hammer().on("swipeleft", nextPage);
    $('.book').hammer().on("swiperight", prevPage);


  },
  methods: {
    getAll() {
      this.request.get("/person/get").then(res => {
        this.tableData = res
      })
    },

  }
}
</script>

<style scoped lang="less">
  @import '../assets/css/normalize.css';
  @import '../assets/css/htmleaf-demo.css';
  @import '../assets/css/style.css';

</style>