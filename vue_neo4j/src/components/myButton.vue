<template>
<div>
  <div class="backimg">
    <img src='../assets/img/bg.jpg' />
  </div>

  <div class="btnBox">
    <div class="btn">
      <div class="btn-border-top"></div>
      <div class="btn-top-left"></div>
      <a href="#">ENTRANCE1</a>
      <div class="btn-bottom-right"></div>
      <div class="btn-border-bottom"></div>
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: "myButton"
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.backimg {
  width: 100%;
  height: 100%;
  min-height: 600px;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow: hidden;
  z-index: -1;
}

.backimg img {
  width: 100%;
  height: 100%;
}

.btnBox {
  position: absolute;
  width: 100%;
}

.btn {
  width: 200px;
  height: 60px;
  margin: 450px 200px 0 70%;
  background-color: rgba(0,0,0,.8);
  text-align: center;
  position: relative;
}

.btn a {
  display: block;
  text-decoration: none;
  color: #FFFFFF;
  font: bold 20px arial;
  line-height: 60px;
  height: 60px;
}

.btn-border-top, .btn-border-bottom {
  height: 5px;
  background-color: #FFFFFF;
  position: absolute;
  width: 0%;
  transition: .4s;
}

.btn-top-left, .btn-bottom-right {
  height: 0;
  background-color: #FFFFFF;
  position: absolute;
  width: 5px;
  transition: .4s;
}

.btn-border-top {
  right: 0;
  top: 0;
}

.btn-border-bottom {
  left: 0;
  bottom: 0;
}

.btn-top-left {
  left: 0;
  top: 0;
}

.btn-bottom-right {
  right: 0;
  bottom: 0;
}

.btn:hover .btn-border-top {
  width: 100%;
}

.btn:hover .btn-border-bottom {
  width: 100%;
}

.btn:hover .btn-top-left {
  height: 58px;
}

.btn:hover .btn-bottom-right {
  height: 58px;
}

.btn:hover {
  background-color: rgba(0,0,0,0);
}

.btn:hover a {
  color: #FFFFFF;
  text-decoration: none;
}

</style>