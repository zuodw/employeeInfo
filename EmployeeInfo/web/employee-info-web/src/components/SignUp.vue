<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width: 400px; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀</el-header>
      <el-main>
        <el-form :label-position="labelPosition" label-width="80px" :model="formData" :rules="rules" ref="formData">
          <el-form-item label="邮件地址" prop="mail">
            <el-input v-model="formData.mail"></el-input>
            <el-button type="text" @click="applyVerifyCode()">发送验证码</el-button>
          </el-form-item>
          <el-form-item label="验证码" prop="verifyCode">
            <el-input v-model="formData.verifyCode"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass">
            <el-input type="password" v-model="formData.pass" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPass">
            <el-input type="password" v-model="formData.checkPass" autocomplete="off"></el-input>
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
  name: 'SignUp',
  data () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.formData.checkPass !== '') {
          this.$refs.formData.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.formData.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      labelPosition: 'top',
      formData: {
        mail: '',
        verifyCode: '',
        pass: '',
        checkPass: ''
      },
      rules: {
        mail: [
          { required: true, message: '请输入您的邮箱地址', trigger: 'blur' }
        ],
        verifyCode: [
          { required: true, message: '请输入验证码', trigger: 'blur' }
        ],
        pass: [
          { required: true, validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  created: function () {
    console.log('SignUp Created.')
  },
  methods: {
    applyVerifyCode () {
      this.$axios
        .post('/api/ApplyVerifyCode', {
          params: {
            'mail': this.formData.mail
          }
        })
        .then(response => {
          if (response.data.errCode === '0') {
            this.$message({
              message: '验证码已发送至您的邮箱，请注意查收。',
              type: 'success',
              center: true
            })
          } else if (response.data.errCode === '-2') {
            this.$confirm('该邮件已经注册!请直接登录。', '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'info'
            }).then(() => {
              this.$router.replace('/signin')
            }).catch(() => {
              this.$message({
                type: 'info',
                message: '已取消登录'
              })
            })
          } else {
            this.$message({
              message: response.data.errMsg,
              type: 'error',
              center: true
            })
          }
        })
    },
    submitForm (formData) {
      this.$refs[formData].validate((valid) => {
        if (valid) {
          this.$axios
            .post('/api/SignUp', {params: this.formData})
            .then(response => {
              if (response.data.errCode === '0') {
                sessionStorage.setItem('userMail', this.formData.mail)
                this.$router.replace('/employeeInfoUpdate')
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
