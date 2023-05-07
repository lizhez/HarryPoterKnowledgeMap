<template>
  <div class="scene">
    <article class="book">
      <div class="page active">
        <div class="front" style="margin-top: 30px">
          <header class="htmleaf-header2">
            <h1 style="font-family:Algerian">Harry Potter<br/>The Second<br/>Part</h1>
            <div class="htmleaf-links">
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/book1" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>

          <h1 style="font-family:'Agency FB';">The Story of Harry Potter</h1>
          <p style="font-family:cursive">
            &nbsp;&nbsp;伏地魔是近代巫师界继格林德沃后能力最强的黑巫师，主张纯血统巫师论，想要统治巫师和麻瓜，同时大开杀界使得人心惶惶。
            此时他听到一个预言:一个七月份出生的男孩拥有可以打败他的力量。伏地魔将目光锁定在了年仅一岁的哈利身上，
            一天晚上他闯入了哈利的家，杀掉了哈利的父母。正想要杀掉哈利时奇迹发生了，他不仅没有杀死哈利，自己反而受到重创，落荒而逃，故事正式开始...
          </p>
          <br>
          <p style="font-family:cursive">
            &nbsp;&nbsp;时间一转眼到了十年后，被姨夫姨妈收养而长大的哈利收到了霍格沃茨魔法学校的录取通知书，成为一名年轻的巫师，学习魔法。
            在学校里他结识了好朋友赫敏和罗恩，以及处处与自己作对的死敌马尔福，总是为难他的斯内普教授和和蔼可亲的校长邓布利多。
            邓布利多校长为自己的好朋友尼克•勒梅看管可以使人延长寿命的宝石魔法石，并将它藏在了霍格沃茨机关重重的地下室中，
            苟延残喘的伏地魔附身到了学校老师奇洛身上并想借助魔法石恢复活力，哈利和伙伴们通过层层魔法考验及时出现阻止了奇洛的行动，
            保护了魔法石，奇洛受伤后死亡，伏地魔再次逃走并继续蛰伏...
          </p>

        </div>
        <div class="back">
          <h1 style="font-family:Algerian">– the main actors –</h1>
          <div>
            <el-row :gutter="70">
              <el-col :span="10">
                <el-card shadow="hover">
                  <img src='../assets/picture/哈利·波特.jpg' width="120px" height="130px" @click="getRoleInfo(1)">
<!--                  <img src='../assets/picture/哈利·波特.jpg' width="120px" height="130px" @click="nextPage">-->
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card shadow="hover">
                  <img src='../assets/picture/赫敏·格兰杰.jpg' width="200px" @click="getRoleInfo(2)">
                </el-card>
              </el-col>
            </el-row>
            <br>
            <el-row :gutter="30">
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/罗恩·韦斯莱.jpg' width="120px" @click="getRoleInfo(3)">
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/邓布利多.jpg' width="120px" @click="getRoleInfo(4)">
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/斯内普.jpg' width="140px" @click="getRoleInfo(5)">
                </el-card>
              </el-col>
            </el-row>
            <br>
            <el-row :gutter="20">
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/麦格.jpg' height="130px" @click="getRoleInfo(6)">
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/海格.jpg' width="120px" @click="getRoleInfo(7)">
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover">
                  <img src='../assets/picture/伏地魔.jpg' height="120px" @click="getRoleInfo(8)">
                </el-card>
              </el-col>
            </el-row>
          </div>
        </div>
      </div>

      <div class="page">
        <div class="front">
        <h1 style="font-family:Algerian">- the info of actor -</h1>
          <el-card shadow="hover">
            <p style="text-align: left;font-family:'Agency FB';"><b>Name:</b> {{role.name}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Nickname:</b> {{role.nickname}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Player:</b> {{role.player}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Appearance:</b> {{role.appearance}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Message:</b> {{role.meta}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Birthday: </b>{{role.birthday}}</p>
            <p style="text-align: left;font-family:'Agency FB';"><b>Character:</b> {{role.character}}</p>
          </el-card>
        </div>
        <div class="back">
          <h1 style="font-family:Algerian">- the video list -</h1>
          <h3 style="font-family:'Agency FB'">Chick the picture to see the detail message and video!</h3>
         <el-row>
           <el-col span=8>
             <el-button @click="modifyVideo(1)">哈利·波特</el-button>
           </el-col>
           <el-col span="16">
             <el-card>
               <p>
                  {{info1}}
               </p>
             </el-card>
           </el-col>

         </el-row><br>
          <el-row>
            <el-col span="8">
              <el-button type="success" @click="modifyVideo(2)">赫敏·格兰杰</el-button>
            </el-col>
            <el-col span="16">
              <el-card>
                <p>
                  {{info2}}
                </p>
              </el-card>
            </el-col>
          </el-row><br>
          <el-row>
            <el-col span="8">
              <el-button type="info" @click="modifyVideo(3)">罗恩·韦斯莱</el-button>
            </el-col>
            <el-col span="16">
              <el-card>
                <p>
                  {{info3}}
                </p>
              </el-card>
            </el-col>
          </el-row><br>
          <el-row>
            <el-col span="8">
              <el-button type="warning" @click="modifyVideo(4)">邓布利多</el-button>
            </el-col>
            <el-col span="16">
              <el-card>
                <p>
                  {{info4}}
                </p>
              </el-card>
            </el-col>
          </el-row><br>
          <el-row>
            <el-col span="8">
              <el-button type="danger" @click="modifyVideo(5)">伏地魔</el-button>
            </el-col>
            <el-col span="16">
              <el-card>
                <p>
                  {{info5}}
                </p>
              </el-card>
            </el-col>
          </el-row>

        </div>
      </div>

      <div class="page">
        <div class="front">
          <h1 style="font-family:Algerian">– video of actor –</h1>
          <div>
            <video-label :child-message=videoName />
          </div>
        </div>
        <div class="back">
          <header class="htmleaf-header2" style="margin-top: 30px">
            <h3 style="font-family:Algerian">Thanks To Watching!</h3>
            <h3 style="font-family:Algerian">Harry Potter Part 2 End!</h3>
            <div class="htmleaf-links">
              <!--              <a class="htmleaf-icon icon-htmleaf-home-outline" href="/" target="_blank"></a>-->
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>
          <div style="margin-top: 20px">
            <img src='../assets/img/img_end1.jpg' style="width: 400px;height: 320px">
          </div>
        </div>
      </div>

    </article>
  </div>
</template>

<script>
// @ is an alias to /src

import  '../assets/js/jquery-1.11.0.min.js'
import $ from 'jquery'
import videoLabel from '../components/videoLabel.vue'

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
    videoLabel
  },
  data() {
    return {
      currentPage: 0,
      input: '',
      data: '',
      tableData: [],
      // videoName:'../../video/哈利波特.mp4'
      videoName:'',
      info1:'',
      info2:'',
      info3:'',
      info4:'',
      info5:'',
      //主角团信息
      name:'',
      meta:'',
      nickname:'',
      player:'',
      appearance:'',
      birthday:'',
      character:'',
      role:[],
      roleData:['哈利·波特','赫敏·格兰杰','罗恩·韦斯莱','阿不思·邓布利多','西弗勒斯·斯内普','米勒娃.麦格','鲁伯·海格','汤姆·马沃罗·里德尔']


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
    },nextPage() {
      $('.active')
          .removeClass('active')
          .addClass('flipped')
          .next('.page')
          .addClass('active')
          .siblings();
    },
    prevPage() {
      $('.flipped')
          .last()
          .removeClass('flipped')
          .addClass('active')
          .siblings('.page')
          .removeClass('active');
    },
    //改变视频路径和显示的信息
    modifyVideo(name){
      if(name===1){
        // console.log(1111)
        this.videoName='../../video/哈利波特.mp4'
        this.info1='哈利·波特（Harry James Potter），主角，生于1980年7月31日，是巫师夫妇詹姆·波特和莉莉·波特的独生子。他是伊诺特·皮福雷的后裔，而书中的反派势力伏地魔，则是卡德马·皮福雷之后代，因此两人有共同的祖先。哈利有着黑发绿眼，就像他的父亲一样，黑色的头发总是四处乱翘，有着波特家族的飞行天赋。'
        this.info2=''
        this.info3=''
        this.info4=''
        this.info5=''
      }
      if(name===2){
        // console.log(2222)
        this.videoName='../../video/赫敏·格兰杰.mp4'
        this.info2=' 赫敏·格兰杰（Hermione Jean Granger），生于1979年9月19日，出身一个麻瓜家庭。在书中以一个喜好钻研学术及无所不知的聪明女孩形象出现，有时显得独断专行，她的知识在他们许多的冒险旅程中证明有用。赫敏到霍格沃茨不久就成为全年级最聪明的学生。'
        this.info1=''
        this.info3=''
        this.info4=''
        this.info5=''
      }
      if(name===3){
        this.videoName='../../video/罗恩·韦斯莱.mp4'
        this.info3='罗恩·韦斯莱（Ronald Bilius Ron Weasley），生于1980年3月1日，哈利在霍格沃茨最要好的朋友，书中的喜剧角色。韦斯莱家族是古老的纯血统家族，他们都拥有一头火焰般的红发。'
        this.info2=''
        this.info1=''
        this.info4=''
        this.info5=''
      }
      if(name===4){
        this.videoName='../../video/邓布利多.mp4'
        this.info4=' 阿不思·邓布利多（Albus Percival Wulfric Brian Dumbledore），变形术教授兼霍格沃茨魔法学校校长，被公认为是当代最伟大的巫师，哈利最尊敬的人之一。第六卷时为了得到魂器牺牲.'
        this.info2=''
        this.info3=''
        this.info1=''
        this.info5=''
      }
      if(name===5){
        this.videoName='../../video/伏地魔.mp4'
        this.info5='魔法界最邪恶的黑巫师，被人们称为“神秘人”，大多数人不敢直呼其名字。原名汤姆·马沃罗·里德尔。他一生追求名利并沉迷黑魔法，渴望获得永生。后以“伏地魔”自居，并招揽相同嗜好的一批信徒(即食死徒)，希望“净化”巫师界。对待非纯血统巫师、麻瓜和反叛者手段非常残忍。'
        this.info2=''
        this.info3=''
        this.info4=''
        this.info1=''
      }
    },
    //角色信息展示，主角团信息查询
    getRoleInfo(roleNum){
      // //调用后端接口函数
      //roleName是传给后端的参数，在roleData数组里存着对应的角色名称
      let name;
      if(roleNum===1){
        name="哈利·波特"
      }if(roleNum===2){
        name='赫敏·格兰杰'
      }if(roleNum===3){
        name='罗恩·韦斯莱'
      }if(roleNum===4){
        name='阿不思·邓布利多'
      }if(roleNum===5){
        name='西弗勒斯·斯内普'
      }if(roleNum===6){
        name='米勒娃.麦格'
      }if(roleNum===7){
        name='鲁伯·海格'
      }if(roleNum===8){
        name='汤姆·马沃罗·里德尔'
      }
      this.request.get("/searches/getNodeByName/"+name).then(res=>{
        this.role=res
      })
    }

  }
}
</script>

<style scoped lang="less">
  @import '../assets/css/normalize.css';
  @import '../assets/css/htmleaf-demo.css';
  @import '../assets/css/style.css';

</style>