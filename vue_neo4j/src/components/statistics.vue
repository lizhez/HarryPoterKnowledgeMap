<template>
<div>
  <el-row>
    <el-card>
      <el-col :span="10">
        <div id="college" style="width:600px;height: 250px"></div>
      </el-col>
    </el-card>
  </el-row>
  <br>
  <el-row>
    <el-card>
      <el-col :span="10">
        <div id="org" style="width:600px;height: 250px"></div>
      </el-col>
    </el-card>
  </el-row>
</div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "statistics",
  data(){
    return{

    }
  },
  mounted() {

    let optionCollege = {
      title: {
        text: '各学院人数统计',
        subtext: '统计图',
        left: 'center'
      },
      tooltip: {
        trigger: 'item',
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      xAxis: {
        type: 'category',
        data: ["格兰芬多学院","斯兰特林学院","拉文克劳学院","赫奇帕奇学院"]
      },
      yAxis: {
        type: 'value'
      },
      series: [
        { name:"人数",//name相同代表是一组值，颜色会相同
          data: [],
          type: 'line'
        },
        { name:"人数",
          data: [],
          type: 'bar'
        },
      ]
    };

    let optionOrg = {
      title: {
        text: '各组织人数统计',
        subtext: '统计图',
        left: 'center'
      },
      tooltip: {
        trigger: 'item',
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      xAxis: {
        axisLabel: {
          interval:0,
          rotate:40
        },
        type: 'category',
        data: ["英国魔法部","食死徒 ","霍格沃兹魔法学校","凤凰社","邓布利多军"]
      },
      yAxis: {
        type: 'value'
      },
      series: [
        { name:"人数",//name相同代表是一组值，颜色会相同
          data: [],
          type: 'line'
        },
        { name:"人数",
          data: [],
          type: 'bar'
        },
      ]
    };


    let OrgDom = document.getElementById('org');
    let OrgChart = echarts.init(OrgDom);
    OrgChart.setOption(optionOrg);
    let CollegeDom = document.getElementById('college');
    let CollegeChart = echarts.init(CollegeDom);
    CollegeChart.setOption(optionCollege);


    this.request.get("/searches/getCountOfClubs").then(res => {
      optionOrg.series[0].data=res
      optionOrg.series[1].data=res
      console.log(res)

      OrgChart.setOption(optionOrg);
    })

        this.request.get("/searches/getCountOfSchools").then(res => {
          optionCollege.series[0].data=res
          optionCollege.series[1].data=res

          CollegeChart.setOption(optionCollege);
        })
  },
  methods:{

  }
}
</script>

<style scoped>

</style>