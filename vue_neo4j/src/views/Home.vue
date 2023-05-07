<template>
<div>
  <div id='building'>
    <div>
      <div class="btnBox">
        <div class="btn" style="margin-left: 1270px;margin-top: 680px">
          <div class="btn-border-top"></div>
          <div class="btn-top-left"></div>
          <router-link to="/book1">
            ENTRANCE1
          </router-link>
          <div class="btn-bottom-right"></div>
          <div class="btn-border-bottom"></div>
        </div>
    </div>
    </div>
    <div>
      <div class="btnBox">
        <div class="btn" style="margin-left: 650px;margin-top: 285px">
          <div class="btn-border-top"></div>
          <div class="btn-top-left"></div>
          <router-link to="/book2">
            ENTRANCE2
          </router-link>
          <div class="btn-bottom-right"></div>
          <div class="btn-border-bottom"></div>
        </div>
      </div>
    </div>
    <div>
      <div class="btnBox">
        <div class="btn" style="margin-left: 20px;margin-top: 10px">
          <div class="btn-border-top"></div>
          <div class="btn-top-left"></div>
          <router-link to="/book3">
            ENTRANCE3
          </router-link>
          <div class="btn-bottom-right"></div>
          <div class="btn-border-bottom"></div>
        </div>
      </div>
    </div>
    <div>
      <h1 align="center" style="font-family:Algerian;font-size: 45px;">Welcome to Harry Potter' world</h1>
    </div>

  </div>
</div>
</template>


<script>

export default {
  name: "Home",
  mounted() {
    this.color()
  },


}
</script>

<style scoped>
#building{
  background:url("../assets/img/bg.jpg");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
  /*-webkit-filter: blur(1px);*/
  /*filter: blur(1px)*/
}

.btnBox {
  position: absolute;
  width: 100%;
}

.btn {
  width: 200px;
  height: 60px;
  /*margin: 450px 200px 0 70%;*/
  background-color: #380250FF;
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