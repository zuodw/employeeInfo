<template>
  <div>
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column prop="mail" label="邮箱地址" width="180"></el-table-column>
      <el-table-column prop="name" label="姓名" width="180"></el-table-column>
      <el-table-column prop="birthday" label="生日"></el-table-column>
    </el-table>
    <el-button type="primary" @click="deleteMyInfo()">删除个人信息</el-button>
  </div>
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
  },
  methods: {
    deleteMyInfo: function () {
      this.$confirm('操作将永久删除您的个人信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios
          .post('/api/DeleteEmployeeInfo', {
            params: {
              'mail': sessionStorage.getItem('userMail')
            }
          })
          .then(response => {
            if (response.data.errCode === '0') {
              sessionStorage.removeItem('userMail')
              this.tableData.length = 0
              this.$router.replace('/')
            }
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>
