<!-- flask-vue-blog/front-end/src/components/Header.vue -->
<!-- 单文件组件规范：https://vue-loader.vuejs.org/zh/spec.html#%E7%AE%80%E4%BB%8B-->
<template>
  <div class="navbar">
    <div class="toolbar-container-left">
      <img style="float: left;" src="../assets/images/logo.png" />
      <ul>
        <!-- 也可以用of代替in -->
        <!-- index属于VUE循环的范畴 -->
        <li
          class="toolbar-category"
          v-for="item in items"
          :key="item.name"
          :class="{ active: item.name === current }"
          @click="selected(item)"
        >
          {{ item.name }}
        </li>
      </ul>
    </div>
    <div class="toolbar-container-middle">
    </div>
    <div class="toolbar-container-right">
      <ul>
        <li class="toolbar-category" 
        v-for="item in toolbarRight.items" 
        v-bind:key="item.name" v-on:click="selected(item)" v-bind:class="{ active:  item.name === current }" >
          {{ item.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  // data () 函数属于 VUE 的范畴
  data() {
    // 返回一个对象，是 JS 的范畴
    return {
      items: [
        { id: 0, name: "首页" },
        { id: 1, name: "博客" },
        { id: 2, name: "下载" },
      ],
      // 当前所在栏
      current: "首页",
      toolbarRight: {
        items: [
          { id: 0, name: "登录/注册" },
          { id: 1, name: "会员中心" },
          { id: 2, name: "收藏" },
          { id: 3, name: "消息" },
        ],
      },
    };
  },
  methods: {
    selected(item) {
      this.current = item.name;
      console.log(item);
    }
  },
};
</script>

<style>
/* flex:弹性布局 */
.navbar {
  display: flex;
  min-width: 1280px;
  background-color: #ffffff;
  margin-top: -9px;
}
.toolbar-container-left {
  height: 48px;
}
.toolbar-container-middle {
  height: 48px;
}
.toolbar-container-right {
  /* flex布局控制最后一个元素右浮动 */
  margin-left: auto;
}

.navbar img {
  height: 100%;
}
/* 设置ul样式 */
.toolbar-container-left ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: inline;
}
/* 设置li样式 */
.toolbar-container-left ul li {
  float: left;
  /* 设置方框形状  */
  padding: 12px 16px;
  font-size: 14px;
}
/* 设置导航栏鼠标放上去的颜色 */
.toolbar-container-left ul li:hover:not(.active) {
  background: #f0f0f5;
}
.toolbar-container-right ul li:hover:not(.active) {
  background: #f0f0f5;
}
.toolbar-category {
  /* 点击前的样式 */
  border-top-style: solid;
  border-top-color:  #f5f6f7;
}
.active {
  /* 设置点击后的样式 */
  border-top-style: solid;
  border-top-color: #fc1944;
}

/* 右侧导航 */
/* 设置ul样式 */
.toolbar-container-right ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
/* 设置li样式 */
.toolbar-container-right ul li {
  float: left;
  /* 设置方框形状  */
  padding: 12px 16px;
  font-size: 14px;
}
</style>