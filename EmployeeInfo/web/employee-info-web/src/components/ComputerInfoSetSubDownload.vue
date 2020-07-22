<template>
  <center>
    <el-card class="box-card" style="text-align:left">
      STEP1.  点击下方按钮, 下载PC信息检测工具 <br/>
      STEP2.  执行PC信息检测工具，工具将自动收集您当前使用的PC信息并上传至服务器。
    </el-card>
    <el-card class="box-card">
      <el-link style="font-size:20px" type="primary" icon="el-icon-download" :href="this.$axios.defaults.baseURL + 'api/Download'" @click.native="downloadStart">点击下载PC信息检测工具</el-link>
    </el-card>
  </center>
</template>

<script>
export default {
  data () {
    return {}
  },
  methods: {
    downloadStart: function () {
      this.$emit('setStepState', 2)
    }
  }
}
</script>

<style>
.box-card {
  width: 600px;
}
</style>
