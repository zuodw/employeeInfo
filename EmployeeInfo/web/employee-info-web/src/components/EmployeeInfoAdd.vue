<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width:60%; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀</el-header>
      <el-main>
        <el-form label-width="80px" :model="formData" :rules="rules" ref="ruleForm">
          <el-form-item label="姓名" prop="name">
            <el-input v-model="formData.name"></el-input>
          </el-form-item>
          <el-form-item label="性别">
            <el-radio-group v-model="formData.sex" size="medium" style="align:left">
              <el-radio border label="男"></el-radio>
              <el-radio border label="女"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="民族">
            <el-input v-model="formData.nation"></el-input>
          </el-form-item>
          <el-form-item label="籍贯">
            <el-input v-model="formData.nativePlace"></el-input>
          </el-form-item>
          <el-form-item label="手机号码">
            <el-input v-model="formData.phoneNum"></el-input>
          </el-form-item>
          <el-form-item label="身份证号">
            <el-input v-model="formData.idCard"></el-input>
          </el-form-item>
          <el-form-item label="护照ID">
            <el-input v-model="formData.passportId"></el-input>
          </el-form-item>
          <el-form-item label="学历">
            <el-input v-model="formData.education"></el-input>
          </el-form-item>
          <el-form-item label="毕业院校">
            <el-input v-model="formData.school"></el-input>
          </el-form-item>
          <el-form-item label="专业">
            <el-input v-model="formData.speciality"></el-input>
          </el-form-item>
          <el-form-item label="部门">
            <el-input v-model="formData.department"></el-input>
          </el-form-item>
          <el-form-item label="手机号码">
            <el-input v-model="formData.phoneNum"></el-input>
          </el-form-item>
          <el-form-item label="邮箱地址">
            <el-input v-model="formData.mail"></el-input>
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
  name: 'EmployeeInfoAdd',
  data () {
    return {
      labelPosition: 'right',
      formData: {
        name: '左',
        sex: '男',
        nation: '汉族',
        nativePlace: '山东青岛',
        idCard: '370285198900000000',
        passportId: '',
        education: '本科',
        school: '理工大学',
        speciality: '数学',
        department: '組み込み系',
        phoneNum: '18688886666',
        mail: 'zzz@163.com'
      },
      rules: {
        name: [
          {required: true, message: '请输入您的姓名', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    submitForm (formData) {
      this.$axios
        .post('http://localhost:5000/api/AddEmployeeInfo', {params: this.formData})
        .then(response => { console.log(123) })
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
