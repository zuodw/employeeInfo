<template>
  <center>
    <el-card class="box-card" style="text-align:left">
      STEP1.  请确保您已经成功执行PC信息检测工具。 </br>
      STEP2.  点击下方按钮，您当前账户将与上传成功的PC信息绑定。
    </el-card>
    <el-card class="box-card" >
      <el-button type="text" @click="bindComputerInfo()">点击绑定PC信息</el-button>
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
              this.$emit('setStepState', 3)
            } else {
              this.$message({
                type: 'error',
                message: 'PC信息绑定失败，请重试。'
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
  width: 600px;
}
</style>
