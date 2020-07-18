<template>
  <div style="text-align:center">
    <el-upload
      drag
      show-file-list
      :action='action'
      multiple
      :on-success='success'
      >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">只能上传使用PC信息检测工具生成的结果文件</div>
    </el-upload>
  </div>
</template>

<script>
export default {
  data () {
    return {
      action: this.$axios.defaults.baseURL + '/api/Upload'
    }
  },
  created () {
    console.log(this.action)
  },
  methods: {
    success: function (response, file, fileList) {
      this.$emit('setStepState', 3)
    }
  }
}
</script>
