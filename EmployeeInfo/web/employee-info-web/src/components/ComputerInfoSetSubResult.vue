<template>
  <div style="text-align:center">
    <el-button type="primary" @click="toMyPage()">点击前往个人主页</el-button>
  </div>
</template>

<script>
export default {
  methods: {
    toMyPage () {
      this.$router.replace('/mypage')
    }
  }
}
</script>
