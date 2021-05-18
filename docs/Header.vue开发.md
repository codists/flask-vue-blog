创建顶部导航栏
---

# 概述

顶部导航栏，顶部导航栏可以划分成三个部分：左（logo + 分类），中(搜索)，右（注册登陆）。

# 创建单文件组件

创建表示顶部导航栏的单文件组件  `Header.vue` 。创建完成后， `Header.vue`  的路径为：`flask-vue-blog/front-end/src/components/Header.vue`，同时将 Header.vue 里的代码修改为如下内容：

```vue

<template>
  <div class="navbar">
      <!-- logo -->
      <div>
        <h1>Hello!</h1>
      </div>
      <!-- 搜索框 -->
      <div></div>
      <!-- 注册登录 -->
      <div></div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
</style>
```

# 运行单文件组件

代码编写完成后，先运行单文件组件看下效果。可以使用 `vue serve` 和 `vue build` 命令对单个 `*.vue` 文件进行快速原型开发，但是使用  `vue` 命令之前，需要先安装一个全局扩展(global addon)：

```bash
$ sudo npm install -g @vue/cli-service-global
```

安装完成后，在 `Header.vue` 文件所在的目录下运行：：

```bash
/flask-vue-blog/front-end/src/components$ vue serve Header.vue 
```

启动后，通过提示的链接访问，如： ` http://localhost:8080/ `。

注：

（1）`vue` 命令的详细用法可以通过 `vue --help` 命令查看。

（2）参考资料：https://cli.vuejs.org/zh/guide/prototyping.html

#  引入logo图片

在 assets 目录创建一个 images目录。然后把名为 logo.png 的图片放置到该目录下。放置后，logo.png 的路径为： `flask-vue-blog/front-end/src/assets/images/logo.png` 。

接在 `Header.vue` 里面使用相对路径引入 logo.png 图片：

```vue

```



# 编辑 Header.vue 文件

```vue

```



