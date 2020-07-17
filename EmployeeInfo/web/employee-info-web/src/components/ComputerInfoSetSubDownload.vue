<template>
  <div style="text-align:center">
    <el-link style="font-size:20px" type="primary" icon="el-icon-download" href="http://192.168.0.102:5000/api/Download" @click.native="downloadStart">点击下载PC信息检测工具</el-link>
  </div>
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
