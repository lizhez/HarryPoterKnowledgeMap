<template>
  <div class="scene">
    <article class="book">
      <div class="page active">
        <div class="front" style="margin-top: 30px">
          <header class="htmleaf-header1" >
            <h1 style="font-family:Algerian">Harry Potter<br/>The First<br/>Part</h1>
            <div class="htmleaf-links">
<!--              <a class="htmleaf-icon icon-htmleaf-home-outline" href="/" target="_blank"></a>-->
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>

          <h1 style="font-family:'Agency FB';margin-top: 30px">The reduction of Harry Potter</h1>
          <p style="font-family:'Agency FB'">
            &nbsp;&nbsp;"Harry Potter" is the British writer J. K. Rowling (J. K. Rowling) in 1997 to 2007 by the magical literature series of novels， a total of seven.
            The first six to Hogwarts School of Witchcraft and Wizardry (Hogwarts School of Witchcraft and Wizardry) as the main stage，
            describes the protagonist - young wizard student Harry Potter in Hogwarts six years before and after the study of life and adventure Story
            the seventh is described by Harry Potter in the second witch war in the search for the Horcrux and destroy the story of Voldemort.
          </p>
          <br>
          <p style="font-family:cursive">
            &nbsp;&nbsp;哈利·波特是英国魔幻系列小说《哈利·波特》及其衍生作品中的主人公，波特夫妇的独子、霍格沃茨魔法学校格兰芬多学院学生，被视为巫师世界救世主。
            他有着一双绿眼睛，戴着圆框眼镜，额头上有一道闪电形伤疤，是唯一一位逃过伏地魔的阿瓦达索命咒的人，被称为“大难不死的男孩”。他与好朋友们经过许多历练，最终击败了伏地魔。
          </p>

        </div>
        <div class="back">
          <h1 style="font-family:Algerian">– The Members Of HarryPotter –</h1>
          <div style="margin-top: 30px;font-family: 'Agency FB'">
            <el-row>
              <el-button type="danger" round @click="getDataBySchool(1)">格兰芬多</el-button>
              <el-button type="primary" round @click="getDataBySchool(2)">拉文克劳</el-button>
              <el-button type="success" round @click="getDataBySchool(3)">斯兰特林</el-button>
              <el-button type="warning" round @click="getDataBySchool(4)">赫奇帕奇</el-button>
              <el-button type="info" round @click="getAll()">全部信息</el-button>
            </el-row>
          </div>
          <div style="height: 520px;margin-top: 20px">
            <Graph ref="graph1" :myChart="a" :datas="data_graph1" v-on:turnPage="turnPage"></Graph>
          </div>

        </div>
      </div>

      <div class="page">
        <div class="front">
          <h1 style="font-family:Algerian">– the relationship of actors –</h1>
          <div style="width: 100%;margin-top: 10px;display: flex;margin-inside: 10px">
            <div style="width: 40%;margin-right: 10px">
              <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
            </div>
            <el-input v-if="value!=='mul'" placeholder="请输入一个人名" v-model="inputName1" clearable></el-input>
            <el-input v-if="value==='mul'" placeholder="请输入一串人名，用,隔开" v-model="inputNameMul" clearable></el-input>
            <el-input v-if="value==='two'" placeholder="请输入一个人名" v-model="inputName2" clearable></el-input>
            <el-input v-if="value==='comRe'" placeholder="请输入一串关系，使用,隔开" v-model="inputRelation" clearable></el-input>
<!--            <el-input v-if="value==='personByRe'" placeholder="请输入一串关系，使用,隔开" v-model="inputRePerson" clearable></el-input>-->

            <el-button v-if="value==='one'" icon="el-icon-search" circle @click="getByOne"></el-button>
            <el-button v-if="value==='two'" icon="el-icon-search" circle  type="primary"  @click="getByTwo"></el-button>
            <el-button v-if="value==='mul'" icon="el-icon-search" circle type="success"  @click="getMul"></el-button>
            <el-button v-if="value==='comRe'" icon="el-icon-search" circle type="warning"  @click="getComplex"></el-button>
          </div>
<!--          <div style="margin-top: 20px;height: 520px">-->
<!--            <el-card shadow="hover" style="height: 100%">-->
<!--              <Graph ref="graph2" :myChart="b" :datas="data_graph2"></Graph>-->
<!--            </el-card>-->
<!--          </div>-->
          <div v-if="value==='comRe'" style="margin-top: 20px">
            <el-card shadow="hover">
              <!--              复杂关系使用：展示查询出的人名的卡片1-->
              <span style="font-family:'Agency FB',serif">{{inputName1}}的{{inputRelation.replaceAll(',','的')}}是:</span>
              <span v-for="item in finalPerson">{{item.name}} </span>
            </el-card>
          </div>
          <el-card shadow="hover" style="margin-top: 5px">
            <div v-if="value==='comRe'" style="height: 410px;">
              <Graph ref="graph2" :myChart="b" :datas="data_graph2" v-on:turnPage="turnPage"></Graph>
            </div>
            <div v-if="value!=='comRe'" style="height: 500px;">
              <Graph ref="graph2" :myChart="b" :datas="data_graph2" v-on:turnPage="turnPage"></Graph>
            </div>
          </el-card>
        </div>
        <div class="back">
          <div>
            <h1 style="font-family:Algerian,serif">
              - the detail message of somebody -
            </h1>
            <div style="font-family: 'Agency FB',serif;font-weight: bolder;font-size: 14px;line-height: 25px" >
              <el-row>
                name:{{person1.name===null?'***':person1.name}}
              </el-row>
              <br>
              <el-row>
                nickname:{{person1.nickname===null?'***':person1.nickname}}
              </el-row>
              <br>
              <el-row>
                player:{{person1.player===null?'***':person1.player}}
              </el-row>
              <br>
              <el-row>
                appearance:{{person1.appearance===null?'***':person1.appearance}}
              </el-row>
              <br>
              <el-row>
                birthday:{{person1.birthday===null?'***':person1.birthday}}
              </el-row>
              <br>
              <el-row>
                character:{{person1.character===null?'***':person1.character}}
              </el-row>
              <br>
              <el-row>
                information:{{person1.meta===null?'***':person1.meta}}
              </el-row>
            </div>

          </div>

        </div>

      </div>
      <div class="page">
        <div class="front">
          <div v-if="person2">
            <h1 style="font-family:Algerian,serif">
              - the detail message of somebody -
            </h1>
            <div style="font-family: 'Agency FB',serif;font-weight: bolder;font-size: 14px;line-height: 25px">
              <el-row>
                name:{{person2.name===null?'***':person2.name}}
              </el-row>
              <br>
              <el-row>
                nickname:{{person2.nickname===null?'***':person2.nickname}}
              </el-row>
              <br>
              <el-row>
                player:{{person2.player===null?'***':person2.player}}
              </el-row>
              <br>
              <el-row>
                appearance:{{person2.appearance===null?'***':person2.appearance}}
              </el-row>
              <br>
              <el-row>
                birthday:{{person2.birthday===null?'***':person2.birthday}}
              </el-row>
              <br>
              <el-row>
                character:{{person2.character===null?'***':person2.character}}
              </el-row>
              <br>
              <el-row>
                information:{{person2.meta===null?'***':person2.meta}}
              </el-row>
            </div>
          </div>
          <div v-else>
            <!--            如果没有数据展示-->
            <h1 style="font-family: 'Agency FB',serif">
              Sorry,the left page is the last person in the database.So,this page is blank!
            </h1>
            <img src='../assets/img/404.jpg' height="470px">
          </div>

        </div>

        <div class="back">
          <header class="htmleaf-header1" style="margin-top: 30px">
            <h3 style="font-family:Algerian">Thanks To Watching!</h3>
            <h3 style="font-family:Algerian">Harry Potter Part 1 End!</h3>
            <div class="htmleaf-links">
              <!--              <a class="htmleaf-icon icon-htmleaf-home-outline" href="/" target="_blank"></a>-->
              <router-link to="/" class="htmleaf-icon icon-htmleaf-home-outline"></router-link>
              <router-link to="/" class="htmleaf-icon icon-htmleaf-arrow-forward-outline"></router-link>
            </div>
          </header>

          <div style="margin-top: 20px">
            <img src='../assets/img/img_end.jpg' style="width: 400px;height: 420px">
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
import Graph from '../components/Graph.vue'
let someone;
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
    videoLabel,
    Graph
  },
  data() {
    return {
      a:"a",
      b:"b",
      c:"c",
      schoolName:'',
      currentPage: 0,
      inputName1: '',
      inputName2: '',
      inputNameMul:'',
      inputRelation:'',
      data: '',
      tableData: [],
      options: [
          {
            value: 'one',
            label: 'single'
          },{
            value: 'two',
            label: 'double'
          },{
            value: 'mul',
            label: 'multi'
          },{
            value: 'comRe',
            label: 'maze'
          },
      ],
      value:'',
      data_graph1:{
        data:[],
        links:[]
      },
      data_graph2:{
        data:[],
        links:[]
      },
      data_graph3:{
        data:[],
        links:[]
      },
      finalPerson:[],
      person1:'',
      person2:''
    }
  },
  watch: {
    data_graph1:{
      handler(newValue, oldValue) {
        this.$refs.graph1.refresh(newValue);
        console.log("-----------")
      },
      deep: true
    },
    data_graph2: {
      handler(newValue, oldValue) {
        this.$refs.graph2.refresh(newValue);
      },
      deep: true
    },
    data_graph3: {
      handler(newValue, oldValue) {
        this.$refs.graph3.refresh(newValue);
      },
      deep: true
    }
  },
  mounted() {
    this.getAll();

    /*左键双击翻页*/
    $('.book')
        .on('dblclick', '.active', nextPage)
        .on('dblclick', '.flipped', prevPage);

    $('.book').hammer().on("swipeleft", nextPage);
    $('.book').hammer().on("swiperight", prevPage);

  },

  methods: {
    changeLinks(oldLinks){
      let links = []
      oldLinks.forEach(function (value, index) {
        let normal = {
          formatter:"",
          show:true
        }
        normal.formatter = value.label;
        let link = {
          label:'',
          source:'',
          target:'',
        }
        link.label = normal;
        link.source = value.source;
        link.target = value.target;
        links[index] = link;
        console.log(links[index])
      });
      return links
    },
    //拿到所有知识图谱数据
    getAll(){
      this.request.get("/searches/allNodes").then(res=>{
      //拿到所有节点
        console.log("data",res)
        this.data_graph1.data=res;
      })
      this.request.get("/searches/allNodeRelations").then(res=>{
        //拿到所有关系
        console.log("links",res)
        this.data_graph1.links=this.changeLinks(res);
      })
    },
    //根据一个人名查找其对应的关系
    getByOne() {
      //将inputName1当做参数传过去
      this.request.get("/searches/getRelationOfOne/nodes/"+this.inputName1).then(res => {
        this.data_graph2.data=res;
      })
      this.request.get("/searches/getRelationOfOne/relations/"+this.inputName1).then(res => {
        this.data_graph2.links=this.changeLinks(res)
      })
    },
    //根据两个人名查找他们之间的关系
    getByTwo() {
      //将inputName1和inputRePath当做参数传过去
      this.request.get("/searches/getRelationBetweenTwo/nodes/"+this.inputName1+"/"+this.inputName2).then(res => {
        this.data_graph2.data=res;
      })

      this.request.get("/searches/getRelationBetweenTwo/relations/"+this.inputName1+"/"+this.inputName2).then(res => {
        this.data_graph2.links=this.changeLinks(res)
      })
    },
    //多人关系查询
    getMul() {
      this.request.get("/searches/getRelationBetweenMany/nodes/"+this.inputNameMul).then(res => {
        this.data_graph2.data=res;
      })

      this.request.get("/searches/getRelationBetweenMany/relations/"+this.inputNameMul).then(res => {
        this.data_graph2.links=this.changeLinks(res)
      })
    },
    //复杂关系查询
    getComplex() {
      //将inputName1和inputRePerson当做参数传过去
      this.request.get("/searches/getRelationsOfSomebody/nodes/"+this.inputName1+"/"+this.inputRelation).then(res => {
        //拿到路径上所有节点
        this.data_graph2.data=res;
        console.log("allnode:",res)
      })
      this.request.get("/searches/getRelationsOfSomebody/relations/"+this.inputName1+"/"+this.inputRelation).then(res => {
        //拿到路径上所有节点之间的关系
        this.data_graph2.links=this.changeLinks(res)
        console.log("all:",res)
      })
      this.request.get("/searches/getRelationsOfSomebodyIsSomeone/"+this.inputName1+"/"+this.inputRelation).then(res => {
        //拿到最终查询的人
        this.finalPerson=res;
        console.log("node:",res)
      })
    },
    //根据学院显示对应的知识图谱
    getDataBySchool(num){
      if(num===1){
        this.schoolName='格兰芬多学院'
      }  if(num===2){
        this.schoolName='拉文克劳学院'
      }  if(num===3){
        this.schoolName='斯莱特林学院'
      }  if(num===4){
        this.schoolName='赫奇帕奇学院'
      }

      this.request.get("/searches/getRelationsOfSchool/nodes/"+this.schoolName).then(res=>{
        console.log(this.schoolName)
        this.data_graph1.data=res;
        console.log("aaaaa",this.data_graph1.data[0].name)
      })
      this.request.get("/searches/getRelationsOfSchool/relations/"+this.schoolName).then(res=>{
        this.data_graph1.links=this.changeLinks(res)
        // console.log("hhh",res)
      })
    },
    turnPage(idCard){

      this.request.get("/searches/person/"+idCard).then(res=>{
        this.person1=res[0]
        this.person2=res[1]
      })
      nextPage();
      this.data_graph1.data.forEach(function (value, index) {
        if(value.id==idCard){
          someone=value;
          //將someone顯示到Page上
        }
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