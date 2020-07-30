<template>
  <center>
    <el-card class="box-card">
      <el-button type="text" @click="refreshComputerInfoCard()">
        <div style="font-size:20px">PC信息绑定成功，点击刷新</div>
      </el-button>
    </el-card>
  </center>
</template>

<script>
export default {
  methods: {
    refreshComputerInfoCard () {
      this.$emit('updateComputerInfoCard')
    }
  }
}
</script>

<style>
.box-card {
  width: 300px;
}
</style>
