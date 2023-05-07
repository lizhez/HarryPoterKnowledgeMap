<template>
  <div>
    <video    :preload="preload" :src="childMessage"
              :height="height" :width="width" align="center" :controls="controls"  :autoplay="autoplay" >
<!--      <source :src="childMessage" type="video/mp4">-->
    </video>
  </div>

</template>

<script>
// 视频播放页面

export default {
  name: "video",
  props: ['childMessage'],
  data(){
    return {
      // videoSrc: '../../video/哈利波特.mp4',
      playStatus: '',
      muteStatus: '',
      isMute: true,
      isPlay: false,
      width: '600', // 设置视频播放器的显示宽度（以像素为单位）
      height: '500', // 设置视频播放器的显示高度（以像素为单位）
      preload: 'auto', //  建议浏览器是否应在<video>加载元素后立即开始下载视频数据。
      controls: true, // 确定播放器是否具有用户可以与之交互的控件。没有控件，启动视频播放的唯一方法是使用autoplay属性或通过Player API。
      autoplay: false
    }

  },
  methods:{
    // 实例化播放器


  },
  mounted() {
    this.createVideo()
  }
}
</script>

<style scoped lang="less">
.video-js .vjs-big-play-button{
  font-size: 0.5rem;
  width: 1.5rem;
  height: 0.8rem;
  line-height: 0.75rem;
  top: 1.6rem;
  left: 3rem;
}
</style>

