<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width:60%; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀
        <el-button type="primary" @click="signUp('formData')">注册</el-button>
      </el-header>
      <el-main>
        大家好，我是主页。
        请点击右上角【注册】按钮。
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data () {
    return {
      labelPosition: 'right',
      formData: {
        mail: 'test@qq.com',
        verifyCode: '123456'
      },
      rules: {
        mail: [
          {required: true, message: '请输入您的邮箱地址', trigger: 'blur'}
        ],
        verifyCode: [
          {required: true, message: '请输入验证码', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    signUp () {
      this.$router.replace('/signup')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
    text-align: right;
}
</style>
