<template>
  <div>
    <div id="main" style="height: 400px;width: 650px"></div>
    <div style="margin-top: 5px;font-family: Algerian,serif;white-space: pre-wrap;font-size: 16px">
      <el-card>
        {{word}}
      </el-card>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "wordSta",
  data(){
    return{
      word:'点击饼图查看魔咒'
    }
  },
  methods:{
      getInfo(param){
        console.log(param)
        if(param.data.name==='哈利波特与魔法石'){
          this.word='Oculus Reparo-恢复如初：修复眼镜等物品。\n Wingardium Lviosa-羽加迪姆勒维奥萨：漂浮咒，让物体漂浮到空中。\nPetrificus Totalus-统统石化：攻击型咒语，使敌人身体僵硬不能动弹。\nAlohomora-阿拉霍洞开：开锁咒语，可打开物理上锁的门窗。\nLumos Solem-强光闪耀：让魔杖末端发出耀眼的强光。咒语效果为荧光闪烁+最强。'
        }if(param.data.name==='哈利波特与密室'){
          this.word='Immobulus-全部定身：使敌方失去行动能力。\nVera Verto-维拉维托（变形咒）：让动物变为物品。\nFinite Incantatem-咒立停：可以解除一些其他魔咒的施展。\nBrakium Emendo-胳膊胳膊修：让人的肢体变得像橡胶一样柔软。\nExpelliarmus-除你武器：击飞敌人手中的任何武器或物品，也能用于直接攻击（击飞或击昏敌人），还能反制敌人发出的攻击性魔咒。'
        }if(param.data.name==='哈利波特与阿兹卡班的囚徒'){
          this.word='Lumos Maxima-特强荧光闪烁：让魔杖末端发出耀眼的强光。\n' +
              'Riddikulus-滑稽滑稽：专门用于对付博格特，使之变为施咒者心里的滑稽形象。\n' +
              'Arresto Momentum-减震止速：让高速下坠或移动的物体减速停止。\n' +
              'Expecto Patronum-呼神护卫：强大的防御咒，是防御摄魂怪、伏地蝙蝠的唯一方式。\n' +
              'Bombarda-爆破隆隆：让物体受爆炸轰击而破裂。'
        }if(param.data.name==='哈利波特与火焰杯'){
          this.word='Morsmordre-尸骨再现：召唤出伏地魔的标记。\n' +
              'Stupefy-昏昏倒地：击昏敌方使之失去意识。\n' +
              'Engorgio-速速变大：使物体的体积增大，密度不变。\n' +
              'Imperio-魂魄出窍（夺魂咒）：三大不可饶恕咒之一，使目标完全听令于施咒者，甚至可以做出平时靠自身能力无法完成的事。\n' +
              'Crucio-钻心剜骨（钻心咒）：三大不可饶恕咒之一，使目标遭受常人不可能忍受的剧痛，严重可致死。'
        }if(param.data.name==='哈利波特与凤凰社'){
          this.word='Legilimens-摄神取念：入侵人的大脑读取记忆或情感，也可在脑中制造幻象。\n' +
              'Protego-盔甲护身：形成防护罩，可抵消甚至反弹敌方击发的咒语。\n' +
              'Impedimenta-障碍重重：.Impedimenta-障碍重重。\n' +
              'Incarcerous-速速禁锢：施放捆仙索将敌方全身捆绑无法挣脱。\n' +
              'Levicorpus-倒挂金钟：斯内普以“混血王子”的名义发明，将敌方倒吊于半空或击退。'
        }if(param.data.name==='哈利波特与混血王子'){
          this.word='Episkey-愈合如初：修正小伤。\n' +
              'Confundus-混淆视听：可扰乱对手行动，进行干扰，施咒一般隐秘不易发现。\n' +
              'Sectumsempra-神锋无影：斯内普以“混血王子”的名义发明，可撕裂目标肌体造成大出血，是杀伤力极强的攻击性咒语。\n' +
              'Vulnera Sanentur-速速愈合：强大的治愈术，可恢复目标的生命活力。\n' +
              'Aguamenti-清水如泉：制造出干净的清水。'
        }if(param.data.name==='哈利波特与死亡圣器'){
          this.word='Protego Totalum-统统加护：施放以自己为中心的护盾，阻挡魔咒的攻击。\n' +
              'Salvio Hexia-平安镇守：形成防御的魔法场，可驱逐一些攻击性咒语。\n' +
              'Repello Muggletum-麻瓜屏蔽：形成自动防止麻瓜进入的魔法场。\n' +
              'Muffiliato-闭耳塞听：形成阻断视觉和听觉的魔法场，身处其中无法被外部的敌人看到和听到。\n' +
              'Dissendium-左右分离：使物体碎裂为两瓣。'
        }
      }
  },
  mounted() {
    let chartDom = document.getElementById('main');
    let myChart = echarts.init(chartDom);
    let option;

    option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        data: [
          '哈利波特与魔法石',
          '哈利波特与密室',
          '哈利波特与阿兹卡班的囚徒',
          '哈利波特与火焰杯',
          '哈利波特与凤凰社',
          '哈利波特与混血王子',
          '哈利波特与死亡圣器',
        ]
      },
      series: [
        {
          name: '出现魔咒统计',
          type: 'pie',
          selectedMode: 'single',
          radius: [0, '25%'],
          label: {
            position: 'inner',
            fontSize: 14
          },
          labelLine: {
            show: false
          },
          data: [
            { value: 5, name: '哈利波特与魔法石' },
            { value: 12, name: '哈利波特与密室' },
            { value: 5, name: '哈利波特与阿兹卡班的囚徒', selected: true }
          ]
        },
        {
          name: '出现魔咒统计',
          type: 'pie',
          radius: ['45%', '60%'],
          labelLine: {
            length: 30
          },
          label: {
            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
            backgroundColor: '#F6F8FC',
            borderColor: '#8C8D8E',
            borderWidth: 1,
            borderRadius: 4,
            rich: {
              a: {
                color: '#6E7079',
                lineHeight: 22,
                align: 'center'
              },
              hr: {
                borderColor: '#8C8D8E',
                width: '100%',
                borderWidth: 1,
                height: 0
              },
              b: {
                color: '#4C5058',
                fontSize: 14,
                fontWeight: 'bold',
                lineHeight: 33
              },
              per: {
                color: '#fff',
                backgroundColor: '#4C5058',
                padding: [3, 4],
                borderRadius: 4
              }
            }
          },
          data: [
            { value: 10, name: '哈利波特与火焰杯' },
            { value: 5, name: '哈利波特与凤凰社' },
            { value: 5, name: '哈利波特与混血王子' },
            { value: 15, name: '哈利波特与死亡圣器' },
          ]
        }
      ]
    };

    option && myChart.setOption(option);
    myChart.on('click', this.getInfo);

  }
}
</script>

<style scoped>

</style>