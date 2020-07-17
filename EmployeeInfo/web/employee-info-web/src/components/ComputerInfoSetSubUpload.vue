<template>
  <div style="text-align:center">
    <el-upload
      drag
      show-file-list
      action="http://192.168.0.102:5000/api/Upload"
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
  methods: {
    success: function (response, file, fileList) {
      this.$emit('setStepState', 3)
    }
  }
}
</script>
