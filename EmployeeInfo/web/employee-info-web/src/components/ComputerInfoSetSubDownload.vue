<template>
  <center>
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
      this.$emit('setStepState', 1)
    }
  }
}
</script>

<style>
.box-card {
  width: 300px;
}
</style>
