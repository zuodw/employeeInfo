<template>
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column prop="mail" label="邮箱地址" width="180"></el-table-column>
    <el-table-column prop="name" label="姓名" width="180"></el-table-column>
    <el-table-column prop="birthday" label="生日"></el-table-column>
  </el-table>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        mail: '',
        name: '',
        birthday: ''
      }]
    }
  },
  created: function () {
    console.log(sessionStorage.getItem('userMail'))
    this.$axios
      .get('/api/GetPersonalInfo', {
        params: {
          'mail': sessionStorage.getItem('userMail')
        }
      })
      .then(response => {
        if (response.data.errCode === '0') {
          this.tableData[0].mail = response.data.params.mail
          this.tableData[0].name = response.data.params.name
          this.tableData[0].birthday = response.data.params.birthday
        }
      })
  }
}
</script>
