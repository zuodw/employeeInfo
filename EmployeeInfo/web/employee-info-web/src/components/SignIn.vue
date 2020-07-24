<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width: 400px; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀</el-header>
      <el-main>
        <el-form :label-position="labelPosition" label-width="80px" :model="formData" :rules="rules" ref="formData">
          <el-form-item label="邮件地址" prop="mail">
            <el-input placeholder="请输入邮件地址" v-model="formData.mail"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input placeholder="请输入密码" show-password v-model="formData.password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('formData')">提交</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'SignIn',
  data () {
    return {
      labelPosition: 'top',
      formData: {
        mail: '',
        password: ''
      },
      rules: {
        mail: [
          {required: true, message: '请输入您的邮箱地址', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'}
        ]
      }
    }
  },
  created: function () {
    console.log('SignIn Created.')
  },
  methods: {
    submitForm (formData) {
      this.$refs[formData].validate((valid) => {
        if (valid) {
          this.$axios
            .post('/api/SignIn', {params: this.formData})
            .then(response => {
              if (response.data.errCode === '0') {
                sessionStorage.setItem('userMail', this.formData.mail)
                this.$router.replace('/')
              } else if (response.data.errCode === '-1') {
                this.$alert('您输入的邮箱尚未注册，请点击前往注册。', '登录失败', {
                  confirmButtonText: '前往注册',
                  callback: action => {
                    this.$router.replace('/signup')
                  }
                })
              } else if (response.data.errCode === '-2') {
                this.$alert('登录失败，请重试。', '登录失败', {
                  confirmButtonText: '重试',
                  callback: action => {
                    this.$refs[formData].resetFields()
                  }
                })
              }
            })
        } else {
          this.$message({
            message: '信息填写失败',
            type: 'error',
            center: true
          })
        }
      })
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
    text-align: center;
}
</style>
