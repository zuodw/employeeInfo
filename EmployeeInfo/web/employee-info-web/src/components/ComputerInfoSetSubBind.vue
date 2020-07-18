<template>
  <div style="text-align:center">
    <el-button type="primary" @click="bindComputerInfo()">点击绑定PC信息</el-button>
  </div>
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
            .post('/api/BindComputerInfo')
            .then(response => {
              if (response.data.errCode === '0') {
                this.$emit('setStepState', 3)
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
