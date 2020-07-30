<template>
  <center>
    <el-steps direction="vertical" :space="80" :active=stepState finish-status="success" align-center style="float: left">
      <el-step title="下载PC信息检测工具并执行"></el-step>
      <el-step title="绑定PC信息"></el-step>
      <el-step title="恭喜你，成功啦"></el-step>
    </el-steps>

    <ComputerInfoSetSubDownloadVue v-on:setStepState="setStepState" v-if='stepState === 0'></ComputerInfoSetSubDownloadVue>
    <ComputerInfoSetSubBindVue v-on:setStepState="setStepState" v-if='stepState === 1'></ComputerInfoSetSubBindVue>
    <ComputerInfoSetSubResultVue v-on:updateComputerInfoCard="updateComputerInfoCard" v-if='stepState === 2'></ComputerInfoSetSubResultVue>
  </center>
</template>

<script>
import ComputerInfoSetSubDownload from '@/components/ComputerInfoSetSubDownload.vue'
import ComputerInfoSetSubBind from '@/components/ComputerInfoSetSubBind.vue'
import ComputerInfoSetSubResult from '@/components/ComputerInfoSetSubResult.vue'

export default {
  data () {
    return {
      stepState: 0
    }
  },
  components: {
    'ComputerInfoSetSubDownloadVue': ComputerInfoSetSubDownload,
    'ComputerInfoSetSubBindVue': ComputerInfoSetSubBind,
    'ComputerInfoSetSubResultVue': ComputerInfoSetSubResult
  },
  methods: {
    setStepState: function (state) {
      this.stepState = state
    },
    updateComputerInfoCard: function () {
      this.$emit('updateComputerInfoCard')
    }
  }
}

</script>
