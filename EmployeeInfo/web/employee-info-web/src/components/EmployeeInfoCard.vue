<template>
  <el-card shadow="always" style="margin-left: 20px">
    <div slot="header" style="text-align:left">
      <h3> 个人信息
      <el-button style="float: right; padding: 3px 0" type="text" @click="updateMyInfo()">更新</el-button>
      </h3>
    </div>
    <div class="text item">
      姓名： {{ this.data.name }}
    </div>
    <div class="text item">
      性别： {{ this.data.sex }}
    </div>
    <div class="text item">
      邮箱： {{ this.data.mail }}
    </div>
    <div class="text item">
      生日： {{ this.data.birthday }}
    </div>
    <div class="text item">
      民族： {{ this.data.nation }}
    </div>
    <div class="text item">
      籍贯： {{ this.data.nativePlace }}
    </div>
    <div class="text item">
      身份证号： {{ this.data.idCard }}
    </div>
    <div class="text item">
      手机号码： {{ this.data.phoneNum }}
    </div>
    <div class="text item">
      ・・・・・・<br/>
    </div>
  </el-card>
</template>

<script>
export default {
  data () {
    return {
      data: {
        name: '',
        sex: '',
        mail: '',
        birthday: '',
        nation: '',
        nativePlace: '',
        idCard: '',
        MACAddress: ''
      }
    }
  },
  created: function () {
    this.$axios
      .get('/api/GetEmployeeInfoByMail', {
        params: {
          'mail': sessionStorage.getItem('userMail')
        }
      })
      .then(response => {
        if (response.data.errCode === '0') {
          this.data.name = response.data.params.name
          this.data.sex = response.data.params.sex
          this.data.mail = response.data.params.mail
          this.data.nation = response.data.params.nation
          this.data.birthday = response.data.params.birthday
          this.data.nativePlace = response.data.params.nativePlace
          this.data.idCard = response.data.params.idCard
          this.data.phoneNum = response.data.params.phoneNum
        }
      })
  },
  methods: {
    updateMyInfo: function () {
      this.$router.replace('/employeeInfoUpdate')
    }
  }
}
</script>

<style>
  .text {
    font-size: 16px;
  }

  .item {
    margin-bottom: 8px;
  }
</style>
