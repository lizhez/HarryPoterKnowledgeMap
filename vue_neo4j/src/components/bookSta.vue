<template>
  <div>
    <div id="book" style="height: 400px;width: 600px"></div>
    <div style="margin-top: 5px;font-family: Algerian,serif">
      <el-card>
        {{book}}
      </el-card>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "bookSta",
  data(){
    return{
      book:'点击对应的饼图板块可以查看全部书籍'
    }
  },
  mounted() {
    let chartDom = document.getElementById('book');
    let myChart = echarts.init(chartDom);
    let option;

    option = {
      legend: {
        top: 'bottom'
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)本'
      },
      toolbox: {
        show: true,
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      series: [
        {
          name: '出现书籍数目统计',
          type: 'pie',
          radius: [10, 100],
          center: ['50%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 8
          },
          data: [
            { value: 22, name: '哈利波特与魔法石' },
            { value: 21, name: '哈利波特与密室' },
            { value: 17, name: '哈利波特与阿兹卡班的囚徒' },
            { value: 17, name: '哈利波特与火焰杯' },
            { value: 16, name: '哈利波特与凤凰社' },
            { value: 10, name: '哈利波特与混血王子' },
            { value: 8, name: '哈利波特与死亡圣器' },
          ]
        },

      ]
    };

    option && myChart.setOption(option);

      myChart.on('click', this.getInfo);
  },
  methods:{
    getInfo(param){
      console.log(param)
      if(param.data.name==='哈利波特与魔法石'){
        this.book='《标准咒语：初级》《魔法史》《魔法理论》《初级变形指南》《千种神奇草药及蕈类》《魔法药剂与药水》《神奇动物在哪里》《黑暗力量：自卫指南》《诅咒与反诅咒》《现代魔法史》《黑魔法的兴衰》《20世纪重要魔法事件》《霍格沃茨，一段校史》《魁地奇溯源》《20世纪的大巫师》《当代著名魔法家名录》《现代魔法的重大发现》《近代巫术发展研究》 《大不列颠和爱尔兰的龙的种类》《从孵蛋到涅槃》《养龙指南》《为消遣和盈利而养龙》'
      }if(param.data.name==='哈利波特与密室'){
        this.book='《标准咒语，二级》《与女鬼决裂》《与食尸鬼同游》 《与母夜叉一起度假》《与巨怪同行》《与吸血鬼同船旅行》《与狼人一起流浪》《与西藏雪人在一起的一年》《给你的奶酪施上魔法》《烤面包的魔法》《变出一桌盛宴！》《疯麻瓜马丁·米格斯历险记》《级长怎样获得权力》《会魔法的我》毒菌大全》《巫师周刊》《强力药剂》《和火炮队一起飞翔》《巫师的十四行诗》《古代魔文简易入门》'
      }if(param.data.name==='哈利波特与阿兹卡班的囚徒'){
        this.book='《妖怪们的妖怪书》《标准咒语，三级》《中级变形指南》《拨开迷雾看未来》《飞天扫帚护理手册》《今日变形》《隐形术的隐形书》《预言无法预见的事：使你自己免受打击》《破碎的球：命运不济的时候》《死亡预兆：当你知道最坏的事即将到来的时侯，你该怎么办？》《巫师古迹》《分类飞天扫帚》《不列颠麻瓜家庭的生活与社会习惯》《数字学和语法学》《鹰头马身有翼兽心理手册》《家禽还是怪兽？》《鹰头马身有翼兽野蛮性研究》'
      }if(param.data.name==='哈利波特与火焰杯'){
        this.book='《标准咒语，四级》《高级变形术指南》《常见魔法病痛》《欧洲魔法教育评估》《地中海神奇水生植物和它们的特性》《溺爱龙的人》《对付多动和烦躁动物的基本魔咒》《英国和爱尔兰的魁地奇球队》《被遗忘的古老魔法和咒语》《古怪的魔法难题及其解答》《对付恶作剧的锦囊妙计》《怪男巫的疯狂魔法》《中世纪巫术指南》《18世纪魔咒选》《地底深处的可怕动物》《你不知道自己所拥有的能力，以及你一旦明白看样运用它们》《只要有魔杖，就有办法》'
      }if(param.data.name==='哈利波特与凤凰社'){
        this.book='《标准咒语，五级》《解梦指南》《魔咒成就》《魔法防御理论》《生而高贵：巫师家谱》《唱唱反调》《飞天扫帚大全》《亚洲抗毒大全》《普通咒语及解招》《智胜黑魔法》《自卫魔咒集》《以毒攻毒集》 《实用防御魔法及其对黑魔法的克制》《数字占卜学新原理》《魔法图符集》《魔法字音表》'
      }if(param.data.name==='哈利波特与混血王子'){
        this.book='《标准咒语，六级》《第五元素：探索》《高级魔药制作》《疗伤手册》《高级魔文翻译》《遭遇无脸妖怪》《食肉树大全》《血亲兄弟：我在吸血鬼中生活》《至毒魔法》《幻影显形常见错误及避免方法》'
      }if(param.data.name==='哈利波特与死亡圣器'){
        this.book='《魔咒创新》《实用魔药大师》《阿不思·邓布利多的生平与谎言》《数字占卜与图形》《尖端黑魔法揭秘》《迷倒女巫的12个制胜法宝》《诗翁彼豆故事集》《阿芒多·迪佩特：大师还是白痴？》'
      }
    }
  }
}
</script>

<style scoped>

</style>