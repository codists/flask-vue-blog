<template>
  <div id="app" class="main-wrap">
    <Header></Header>
    <div class="container">内容区域</div>
    <Footer></Footer>
  </div>
</template>

<script>
// 导入组件，import隶属于 JavaScript 的范畴
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
// 注册组件
export default {
  components: { Header, Footer },
};
</script>

<style>
html,
body,
#app {
  height: 100%;
}

#app {
  margin: 0;
  padding: 0;
}

.container {
  height: 80%;
}
.main-wrap {
  min-width: 1200px;
}
</style>
