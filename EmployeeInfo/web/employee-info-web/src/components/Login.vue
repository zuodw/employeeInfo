<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width:60%; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀</el-header>
      <el-main>
        <el-form label-width="80px" :model="formData" :rules="rules" ref="ruleForm">
          <el-form-item label="邮件地址" prop="mail">
            <el-input v-model="formData.mail"></el-input>
          </el-form-item>
          <el-form-item label="验证码" prop="verifyCode">
            <el-input v-model="formData.verifyCode"></el-input>
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
  name: 'Login',
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
    submitForm (formData) {
      this.$axios
        .post('http://localhost:5000/api/Login', {params: this.formData})
        .then(response => { console.log(456) })
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
