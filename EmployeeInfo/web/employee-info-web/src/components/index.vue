<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width:800px; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀
        <template v-if='userMail'>
          <el-button type="primary" @click="toMyPage">前往个人主页</el-button>
        </template>
        <template v-else>
          <el-button type="primary" @click="signUp()">注册</el-button>
          <el-button type="primary" @click="signIn()">登录</el-button>
        </template>
      </el-header>
      <el-main>
        <template v-if='userName'>
          欢迎你，{{ this.userName }}。
        </template>
        <template v-else-if='userMail'>
          欢迎你，{{ this.userMail }}。
        </template>
        <template v-else>
          大家好，我是主页。<br />
          未注册的同事，请点击【注册】按钮。<br />
          已注册的同事，请点击【登录】按钮。
        </template>
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
      userMail: '',
      userName: '',
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
  created: function () {
    this.userMail = sessionStorage.getItem('userMail')

    this.$axios
      .get('/api/GetEmployeeInfoByMail', {
        params: {
          'mail': sessionStorage.getItem('userMail')
        }
      })
      .then(response => {
        if (response.data.errCode === '0') {
          this.userName = response.data.params.name
        }
      })

  },
  methods: {
    signUp () {
      this.$router.replace('/signup')
    },
    signIn () {
      this.$router.replace('/signin')
    },
    toMyPage () {
      this.$router.replace('/mypage')
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
