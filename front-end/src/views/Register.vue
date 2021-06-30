<template>
  <div class="container-login">
    <div class="main">
      <div class="notes">
        <h4>《EDVAC 报告书的第一份草案》</h4>
        <p>
          这种码和条形码是什么关系？1949
          年，伍德兰和西尔弗基于摩尔斯电码发明了环状条形码，是条形码概念的最初提出者。此后，许多组织和个人为条形码的发展做出了贡献，其中最为突出的要数劳雷尔，他提出了斑马条纹状条形码。
        </p>
        <span>
          <i></i>
          6231
        </span>
      </div>
      <div class="main-login">
        <div class="login">
          <span>帐号密码登录</span>
          <span>手机免密登录</span>
        </div>
        <div class="register"></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.container-login {
  /* 可能存在的问题：图片加载比组件慢 */
  background-image: url("../../static/images/bg-login.jpeg");
  min-height: 600px;
  background-size: cover;
}
.main {
  min-height: 500px;
  width: 790px;
  position: absolute;
  left: 50%;
  top: 50%;
  margin-left: -395px;
  margin-top: -250px;
}
.notes {
  width: 340px;
  height: 500px;
  background: rgba(0, 0, 0, 0.4);
  float: left;
  /* 因为 div 里面有多个 内容，但是所有的都要保持边距，所以设置的是父div的 padding*/
  padding: 40px;
  color: #fff;
  /* 定义如何计算总宽度和总高度， */
  box-sizing: border-box;
}
.notes h4 {
  /* 防止内容太长溢出 */
  overflow: hidden;
  /* 设置溢出的样式 */
  text-overflow: ellipsis;
  line-height: 34px;
  height: 34px;
  font-size: 28px;
  font-weight: 400;
  margin-bottom: 24px;
}
.notes p {
  line-height: 34px;
  height: 270px;
}
.notes span {
  position: absolute;
  box-sizing: border-box;
  min-width: 120px;
  height: 40px;
  padding: 0 10px;
  color: #fc5531;
  text-align: center;
  line-height: 40px;
  border-radius: 24px 24px;
  border: 1px solid #fc5531;
  left: 40px;
  bottom: 40px;
  cursor: pointer;
}
.notes span i {
  background-image: url("../../static/images/up_default.png");
  display: inline-block;
  width: 18px;
  height: 18px;
  background-size: cover;
  /* position: relative; */
  vertical-align: middle;
  top: -3px;
  margin-right: 8px;
  animation-duration: 1s;
}
.main-login {
  width: 450px;
  height: 500px;
  background-color: #fff;
  float: right;
  padding: 30px 0;
}
.main-login .login {
  width: 50%;
  margin: 40px auto 0;
}
</style>