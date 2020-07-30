<template>
  <center>
    <el-card class="box-card">
      <el-button type="text" @click="bindComputerInfo()">
        <div style="font-size:20px">点击绑定PC信息</div>
      </el-button>
    </el-card>
  </center>
</template>

<script>
export default {
  methods: {
    bindComputerInfo: function () {
      this.$confirm('此操作将绑定该PC至您的个人信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios
          .post('/api/BindComputerInfo', {
            params: {
              'mail': sessionStorage.getItem('userMail')
            }
          })
          .then(response => {
            if (response.data.errCode === '0') {
              sessionStorage.setItem('mac', response.data.params.MACAddress)
              this.$emit('setStepState', 2)
            } else {
              this.$message({
                type: 'error',
                message: 'PC信息绑定失败，请确保已正常执行PC信息检测工具'
              })
            }
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消绑定'
        })
      })
    }
  }
}
</script>

<style>
.box-card {
  width: 300px;
}
</style>
