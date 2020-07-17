<template>
  <div style="text-align:center">
    <el-steps :space="600" :active=stepState finish-status="success" align-center>
      <el-step title="下载PC信息检测工具"></el-step>
      <el-step title="上传PC检测结果"></el-step>
      <el-step title="恭喜你，成功啦"></el-step>
    </el-steps>

    <ComputerInfoSetSubDownloadVue v-on:setStepState="setStepState" v-if='stepState === 1'></ComputerInfoSetSubDownloadVue>
    <ComputerInfoSetSubUploadVue v-on:setStepState="setStepState" v-if='stepState === 2'></ComputerInfoSetSubUploadVue>
    <ComputerInfoSetSubResultVue v-if='stepState === 3'></ComputerInfoSetSubResultVue>
  </div>
</template>

<script>
import ComputerInfoSetSubDownload from '@/components/ComputerInfoSetSubDownload.vue'
import ComputerInfoSetSubUpload from '@/components/ComputerInfoSetSubUpload.vue'
import ComputerInfoSetSubResult from '@/components/ComputerInfoSetSubResult.vue'

export default {
  data () {
    return {
      stepState: 1
    }
  },
  components: {
    'ComputerInfoSetSubDownloadVue': ComputerInfoSetSubDownload,
    'ComputerInfoSetSubUploadVue': ComputerInfoSetSubUpload,
    'ComputerInfoSetSubResultVue': ComputerInfoSetSubResult
  },
  methods: {
    setStepState: function (state) {
      this.stepState = state
    }
  }
}

</script>
