<template>
  <div :id="this.myChart" style="width: 600px;height:100%">
  </div>
</template>

<script>
import * as echarts from "echarts";
import axios from "axios";
// import img from "../main.js"
let option = {
    title: {},
    tooltip: {}, //提示框
    animationDurationUpdate: 1500,
    animationEasingUpdate: "quinticInOut",
    series: [
      {
        type: "graph",
        layout: "force",
        // symbolSize: 50, //倘若该属性不在link里，则其表示节点的大小；否则即为线两端标记的大小
        symbolSize: (value, params) => {
          switch (params.data.category) {
          case 0:
            return 45;
          break;
          case 1:
            return 50;
          break;
        }
      },
      roam: true, //鼠标缩放功能
      label: {
        show: true, //是否显示标签
        position:'bottom'
      },
      minRadius: 25,
      maxRadius: 25,
      focusNodeAdjacency: true, //鼠标移到节点上时突出显示结点以及邻节点和边
      edgeSymbol: ["none", "none"], //关系两边的展现形式，也即图中线两端的展现形式。arrow为箭头
      edgeSymbolSize: [4, 10],
      draggable: true,
      edgeLabel: {
        fontSize: 10, //关系（也即线）上的标签字体大小
      },
      force: {
        repulsion: 200,
        edgeLength: 250,
      },
      toolbox: {//工具栏。内置有导出图片，数据视图，动态类型切换，数据区域缩放，重置五个工具。
        show: true,
        feature: {
          restore: { show: true },//重置
          magicType: { show: true, type: ['force', 'chord'] },
          saveAsImage: { show: true }//导出图片
        }
      },
      data: [],
      links:[],
      lineStyle: {
        opacity: 0.9,
        width: 2,
        curveness: 0,
      },
    },
  ],
}

let images=[];
let imgs=[];

export default {
  name: "Graph",
  props:['datas','myChart'],
  data(){
    return{
      myTestChart:null,
      data:[],
      links:[]
    }
  },
  methods:{
    getData(){

      let data=this.datas.data;
      let links =this.datas.links;

      this.data=data;
      this.links=links;
      this.data.forEach(function (value, index) {
        var str=value.name;
        if(imgs[str]==null){
          data[index].symbol='image://'+imgs["default"];
        }else{
          data[index].symbol='image://'+imgs[str];
        }
      });
      this.data=data;
      option.series[0].data=this.data;
      option.series[0].links=this.links;
      console.log(option);
    },
    myInit(){
      const _this=this;
      this.myTestChart=echarts.init(document.getElementById(this.myChart));
      this.myTestChart.setOption(option);
      this.myTestChart.on('click', function (params) {
        if (params.data.id) {
          let idCard = params.data.id; // 获取被点击节点的身份证号
          _this.$emit("turnPage",idCard);
        } else {
        }
      });
    },
    refresh(graph){

      let data=graph.data;
      let links=graph.links;
      graph.data.forEach(function (value, index) {
        var str=value.name;
        if(imgs[str]==null){
          data[index].symbol='image://'+imgs["default"];
        }else{
          data[index].symbol='image://'+imgs[str];
        }
      });
      option.series[0].data=data;
      option.series[0].links=links;
      console.log("option",option)
      this.myTestChart.clear();
      this.myTestChart.setOption(option);
      console.log("graph",this.myTestChart)
    },

  },

  beforeCreate(){

    imgs["哈利·波特"]=require("./img/哈利·波特.png");
    imgs["赫敏·格兰杰"]=require('./img/赫敏·格兰杰.png');
    imgs["乌姆里奇"]=require('./img/乌姆里奇.jpg');
    imgs["亚瑟·韦斯莱"]=require('./img/亚瑟·韦斯莱.jpg');
    imgs["伊戈尔·卡卡洛夫"]=require('./img/伊戈尔·卡卡洛夫.jpg');
    imgs["伏地魔"]=require('./img/伏地魔.jpg');
    imgs["克利切"]=require('./img/克利切.jpg');
    imgs["克拉布"]=require('./img/克拉布.jpg');
    imgs["卢修斯·马尔福"]=require('./img/卢修斯·马尔福.jpg');
    imgs["卢娜·洛夫古德"]=require('./img/卢娜·洛夫古德.jpg');
    imgs["厄尼·麦克米兰"]=require('./img/厄尼·麦克米兰.jpg');
    imgs["塞德里克·迪戈里"]=require('./img/塞德里克·迪戈里.jpg');
    imgs["奥利姆·马克西姆"]=require('./img/奥利姆·马克西姆.jpg');
    imgs["威克多尔·克鲁姆"]=require('./img/威克多尔·克鲁姆.jpg');
    imgs["小天狼星"]=require('./img/小天狼星.jpg');
    imgs["小矮星彼得"]=require('./img/小矮星彼得.jpg');
    imgs["康奈利·福吉"]=require('./img/康奈利·福吉.jpg');
    imgs["德拉科·马尔福"]=require('./img/德拉科·马尔福.jpg');
    imgs["摄魂怪"]=require('./img/摄魂怪.jpg');
    imgs["斯内普"]=require('./img/斯内普.jpg');
    imgs["海格"]=require('./img/海格.jpg');
    imgs["珀西·韦斯莱"]=require('./img/珀西·韦斯莱.jpg');
    imgs["福克斯"]=require('./img/福克斯.jpg');
    imgs["秋·张"]=require('./img/秋·张.jpg');
    imgs["纳威·隆巴顿"]=require('./img/纳威·隆巴顿.jpg');
    imgs["罗恩·韦斯莱"]=require('./img/罗恩·韦斯莱.jpg');
    imgs["芙蓉·德拉库尔"]=require('./img/芙蓉·德拉库尔.jpg');
    imgs["莱姆斯·卢平"]=require('./img/莱姆斯·卢平.jpg');
    imgs["贝拉特里克斯"]=require('./img/贝拉特里克斯.jpg');
    imgs["邓布利多"]=require('./img/邓布利多.jpg');
    imgs["金妮·韦斯莱"]=require('./img/金妮·韦斯莱.jpg');
    imgs["闪闪"]=require('./img/闪闪.jpg');
    imgs["高尔"]=require('./img/高尔.jpg');
    imgs["default"]=require("./img/default.png");
    imgs["佩妮·德思礼"]=require('./img/佩妮·德思礼.jpg');
    imgs["詹姆·波特"]=require('./img/詹姆·波特.jpg');
    imgs["西弗勒斯·斯内普"]=require('./img/西弗勒斯·斯内普.jpg');
    imgs["奥利弗·伍德"]=require('./img/奥利弗·伍德.jpg');
    imgs["鲁伯·海格"]=require('./img/鲁伯·海格.jpg');
    imgs["阿不思·邓布利多"]=require('./img/邓布利多.jpg');
    imgs["詹姆·小天狼星·波特"]=require('./img/小天狼星.jpg');
    imgs["弗雷德·韦斯莱"]=require('./img/弗雷德·韦斯莱.jpg');
    imgs["弗农·德思礼"]=require('./img/弗农·德思礼.jpg');
    imgs["比尔·韦斯莱"]=require('./img/比尔·韦斯莱.jpg');
    imgs["罗丝·韦斯莱"]=require('./img/罗丝·韦斯莱.jpg');
    imgs["汤姆·里德尔"]=require('./img/汤姆·里德尔.jpg');
    imgs["西莫·斐尼甘"]=require('./img/西莫·斐尼甘.jpg');
    imgs["弗利蒙·波特"]=require('./img/弗利蒙·波特.jpg');
    imgs["乔治·韦斯莱"]=require('./img/乔治·韦斯莱.jpg');
    imgs["查理·韦斯莱"]=require('./img/查理·韦斯莱.jpg');
    imgs["梅林"]=require('./img/梅林.jpg');
    imgs["沃尔布加·布莱克"]=require('./img/沃尔布加·布莱克.jpg');
    imgs["纳西莎·马尔福"]=require('./img/纳西莎·马尔福.jpg');
    imgs["萨拉查·斯莱特林"]=require('./img/萨拉查·斯莱特林.jpg');
    imgs["蒙太"]=require('./img/蒙太.jpg');
    imgs["贝拉特里克斯·莱斯特兰奇"]=require('./img/贝拉特里克斯·莱斯特兰奇.jpg');
    imgs["达芙妮·格林格拉斯"]=require('./img/达芙妮·格林格拉斯.jpg');
    imgs["阿布拉克萨斯·马尔福"]=require('./img/阿布拉克萨斯·马尔福.jpg');
    imgs["雷古勒斯·布莱克"]=require('./img/雷古勒斯·布莱克.jpg');
    imgs["马库斯·弗林特"]=require('./img/马库斯·弗林特.jpg');
    imgs["厄克特"]=require('./img/厄克特.jpg');
    imgs["奥赖恩·布莱克"]=require('./img/奥赖恩·布莱克.jpg');
    imgs["德里安·普赛"]=require('./img/德里安·普赛.jpg');
    imgs["杰玛·法利"]=require('./img/杰玛·法利.jpg');
    imgs["汉娜·艾博"]=require('./img/汉娜·艾博.jpg');
    imgs["纽特·斯卡曼德"]=require('./img/纽特·斯卡曼德.jpg');
    imgs["苏珊·博恩斯"]=require('./img/苏珊·博恩斯.jpg');
    imgs["西尔瓦努斯·凯特尔伯恩"]=require('./img/西尔瓦努斯·凯特尔伯恩.jpg');
    imgs["赫尔加·赫奇帕奇"]=require('./img/赫尔加·赫奇帕奇.jpg');
    imgs["韦恩·霍普金斯"]=require('./img/韦恩·霍普金斯.jpg');
    imgs["夏比"]=require('./img/夏比.jpg');
    imgs["扎卡赖斯·史密斯"]=require('./img/扎卡赖斯·史密斯.jpg');
    imgs["戈德里克·格兰芬多"]=require('./img/戈德里克·格兰芬多.jpg');
    imgs["吉米·珀克斯"]=require('./img/吉米·珀克斯.jpg');
    imgs["杰弗里·胡珀"]=require('./img/杰弗里·胡珀.jpg');
    imgs["杰克·斯劳珀"]=require('./img/杰克·斯劳珀.jpg');
    imgs["莉莉·伊万斯"]=require('./img/莉莉·伊万斯.jpg');
    imgs["米勒娃·麦格"]=require('./img/米勒娃·麦格.jpg');
    imgs["尤安·阿伯克龙比"]=require('./img/尤安·阿伯克龙比.jpg');
    imgs["安东尼·戈德斯坦"]=require('./img/安东尼·戈德斯坦.jpg');
    imgs["波佩图阿·范考特"]=require('./img/波佩图阿·范考特.jpg');
    imgs["莉莎·杜平"]=require('./img/莉莎·杜平.jpg');
    imgs["曼蒂·布洛贺"]=require('./img/曼蒂·布洛贺.jpg');
    imgs["佩内洛·克里瓦特"]=require('./img/佩内洛·克里瓦特.jpg');
    imgs["泰瑞·布特"]=require('./img/泰瑞·布特.jpg');
    imgs["桃金娘·沃伦"]=require('./img/桃金娘·沃伦.jpg');
    imgs["西比尔·特里劳妮"]=require('./img/西比尔·特里劳妮.jpg');

  },
  mounted() {
    this.getData();
    this.myInit();
  },
}
</script>

<style scoped>

</style>
