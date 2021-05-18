<template>
  <div class="copyright-box">
      <div class="copyright-footer">
          <ul class="footer-column-t">
            <li>关于我们</li>
            <li>招贤纳士</li>
            <li>广告服务</li>
            <li>开发助手</li>
            <li>400-660-0108</li>
            <li>kefu@csdn.net</li>
            <li>在线客服</li>
            <li>工作时间 8:30-22:00</li>

          </ul>
          <ul class="footer-column-b">
            <li>公安备案号11010502030143</li>
            <li>京ICP备19004658号</li>
            <li>京网文〔2020〕1039-165号</li>
            <li>经营性网站备案信息</li>
            <li>北京互联网违法和不良信息举报中心</li>
            <li>网络110报警服务</li>
            <li>中国互联网举报中心</li>
            <li>家长监护</li>
            <li>Chrome商店下载</li>
            <li>©1999-2021北京创新乐知网络技术有限公司</li>
            <li>版权与免责声明</li>
            <li>版权申诉</li>
          </ul>
      </div>
  </div>
</template>
  
  <script>
  
  </script>
  
  <style>
  .copyright-box {
    min-width: 1280px;
    background-color: #ffffff;
  }
  .copyright-footer {
    min-width: 972px;
    margin: auto;
    padding: auto;
  }
  .footer-column-t,.footer-column-b {
    /* 弹性布局 */
    display: flex;
    /*内容居中*/
    justify-content: center;
    flex-wrap: wrap;
  }
  .footer-column-t li {
    margin: 0 4px;
  }
  .footer-column-b li {
    margin: 4px 6px;
  }
  .footer-column-t, .footer-column-b {
    list-style-type: none;
  }
  </style>