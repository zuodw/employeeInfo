<template>
  <el-card shadow="always" style="width:640px; margin-left: 20px">
    <div slot="header" style="text-align:left">
      <h3> PC信息
      <el-button style="float: right; padding: 3px 0" type="text" @click="updateMyComputerInfo()">更新</el-button>
      </h3>
    </div>
    <div class="text item">
      电脑型号： {{ this.data.ComputerSystemModel }}
    </div>
    <div class="text item">
      ・・・・・・</br>
    </div>
  </el-card>
</template>

<script>
export default {
  data () {
    return {
      data: {
        ComputerSystemModel: ''
      }
    }
  },
  created: function () {
    this.data.MACAddress = sessionStorage.getItem('mac')

    this.$axios
      .get('/api/GetComputerInfoByMac', {
        params: {
          'mac': this.data.MACAddress
        }
      })
      .then(response => {
        if (response.data.errCode === '0') {
          this.data.ComputerSystemModel = response.data.params.ComputerSystemModel
        }
      })
  },
  methods: {
    updateMyComputerInfo: function () {
      this.$router.replace('/computerinfoset')
    }
  }
}
</script>

<style>
  .text {
    font-size: 16px;
  }

  .item {
    margin-bottom: 8px;
  }
</style>
