<template>
  <div>
    <el-container style="margin-left:auto; margin-right:auto; width:60%; border: 1px solid #eee">
      <el-header class="el-header">欢迎来到王者荣耀</el-header>
      <el-main>
        <el-form :label-position="labelPosition" label-width="80px" :model="formData" :rules="rules" ref="formData">
          <el-form-item label="姓名" prop="name">
            <el-input v-model="formData.name"></el-input>
          </el-form-item>
          <el-form-item label="性别">
            <el-radio-group v-model="formData.sex" size="medium" style="align:left">
              <el-radio border label="男"></el-radio>
              <el-radio border label="女"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="民族" prop="nation">
            <el-input v-model="formData.nation"></el-input>
          </el-form-item>
          <el-form-item label="籍贯" prop="nativePlace">
            <el-input v-model="formData.nativePlace"></el-input>
          </el-form-item>
          <el-form-item label="手机号码" prop="phoneNum">
            <el-input v-model="formData.phoneNum"></el-input>
          </el-form-item>
          <el-form-item label="身份证号" prop='idCard'>
            <el-input v-model="formData.idCard"></el-input>
          </el-form-item>
          <el-form-item label="护照ID">
            <el-input v-model="formData.passportId"></el-input>
          </el-form-item>
          <el-form-item label="学历">
            <el-select v-model="formData.education" placeholder="请选择学历">
              <el-option label="专科" value="专科"></el-option>
              <el-option label="本科" value="本科"></el-option>
              <el-option label="硕士" value="硕士"></el-option>
              <el-option label="博士" value="博士"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="毕业院校" prop="school">
            <el-input v-model="formData.school"></el-input>
          </el-form-item>
          <el-form-item label="专业" prop="speciality">
            <el-input v-model="formData.speciality"></el-input>
          </el-form-item>
          <el-form-item label="部门">
            <el-select v-model="formData.department" placeholder="请选择部门">
              <el-option label="嵌入式" value="嵌入式"></el-option>
              <el-option label="DB" value="DB"></el-option>
              <el-option label="WEB" value="WEB"></el-option>
              <el-option label="人事" value="人事"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="邮箱地址">
            <el-input :disabled="true" v-model="formData.mail"></el-input>
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
import rules from '@/assets/rules'

export default {
  name: 'EmployeeInfoUpdate',
  data () {
    var checkIdCard = (rule, value, callback) => {
      if (rules.idCard(value) === false) {
        callback(new Error('身份证信息错误'))
      } else {
        callback()
      }
    }
    return {
      labelPosition: 'right',
      formData: {
        name: '',
        sex: '',
        nation: '',
        nativePlace: '',
        phoneNum: '',
        idCard: '',
        passportId: '',
        education: '',
        school: '',
        speciality: '',
        department: '',
        mail: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入您的姓名', trigger: 'change' }
        ],
        nation: [
          { required: true, message: '请输入您的民族', trigger: 'blur' }
        ],
        nativePlace: [
          { required: true, message: '请输入您的籍贯', trigger: 'blur' }
        ],
        phoneNum: [
          { required: true, message: '请输入您的手机号码', trigger: 'blur' }
        ],
        school: [
          { required: true, message: '请输入您的毕业院校', trigger: 'blur' }
        ],
        speciality: [
          { required: true, message: '请输入您的专业', trigger: 'blur' }
        ],
        idCard: [
          { required: true, validator: checkIdCard, trigger: 'blur' }
        ]
      }
    }
  },
  created: function () {
    this.formData.mail = sessionStorage.getItem('userMail')
    this.$axios
      .get('/api/GetEmployeeInfoByMail', {
        params: {
          'mail': sessionStorage.getItem('userMail')
        }
      })
      .then(response => {
        if (response.data.errCode === '0') {
          this.formData.name = response.data.params.name
          this.formData.sex = response.data.params.sex
          this.formData.nation = response.data.params.nation
          this.formData.nativePlace = response.data.params.nativePlace
          this.formData.idCard = response.data.params.idCard
          this.formData.passportId = response.data.params.passportId
          this.formData.education = response.data.params.education
          this.formData.school = response.data.params.school
          this.formData.speciality = response.data.params.speciality
          this.formData.department = response.data.params.department
          this.formData.phoneNum = response.data.params.phoneNum
        }
      })
  },
  methods: {
    submitForm (formData) {
      this.$refs[formData].validate((valid) => {
        if (valid) {
          this.$axios
            .post('/api/UpdateEmployeeInfo', {params: this.formData})
            .then(response => {
              if (response.data.errCode === '0') {
                this.$alert('个人信息更新完成，点击前往个人页主页。', '提交结果', {
                  confirmButtonText: '前往个人主页',
                  callback: action => {
                    this.$router.replace('/myPage')
                  }
                })
              }
            })
        } else {
          return false
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
