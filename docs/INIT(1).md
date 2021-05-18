## 初始化项目
- 初始化前端 Vue
- Flask 项目

## 初始化 Vue
1. 安装 nodejs (http://nodejs.cn/download) Vue CLI 4.x 需要 Node.js v8.9 或更高版本 (推荐 v10 以上)。
2. [可选], 配置淘宝镜像
    - npm config set registry https://registry.npm.taobao.org --global
    - npm config set disturl https://npm.taobao.org/dist --global
3. 安装 Vue-CLI (Vue脚手架工具): npm install -g @vue/cli
4. 创建前端项目
    - vue create [项目名称]  名称不能包含大写英文
        - 1.选择 default
        - 2.选择 npm (可根据个人习惯是否用 yarn)
    - cd 项目名称 && npm run serve 即可启动项目
5. [可选], 安装 UI 组件库，此处选择 element-ui
    - 安装 element-ui, 项目目录下执行: npm install element-ui
    - 在 src 目录下找到 main.js, 插入如下内容
        ```JavaScript
        import ElementUI from 'element-ui';
        import 'element-ui/lib/theme-chalk/index.css';
        Vue.use(ElementUI);
        ```
    - 在 App.vue 中 加入 <el-button>测试按钮</el-button> 验证是否安装成功
6. [可选], 安装 Vue-Router: npm install vue-router, 以下是可选操作，个人习惯不同差异不同 
    - 在 src 目录下新建 router 目录
    - 在 router 目录下，新建 index.js
    - 在 index.js 中 编写如下内容
        ```
        import Vue from 'vue';
        import VueRouter from 'vue-router';
        Vue.use(VueRouter);
        let router = new VueRouter({
            mode: 'history',
            routes: [
                {
                    name: 'default',
                    path: '/',
                    redirect: {
                        name: 'login'
                    }
                },
                {
                    name: 'login',
                    path: '/login',
                    component: Login
                }
            });
        export default router;
        ```
    - 在 src 目录下找到 main.js, 插入如下内容
        ```
        import router from '@/router/index.js';  // @代表的是src 
        // new Vue() 修改为 
        new Vue({
            router,
            render: h => h(App),
        }).$mount('#app');
        ```
7. [可选], 安装 axios (npm install axios)
    - 在 src 目录下找到 main.js, 插入如下内容
        ```
        import axios from 'axios';
        Vue.prototype.$axios = axios;
        ```
