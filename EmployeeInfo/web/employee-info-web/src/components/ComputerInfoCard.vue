<template>
  <el-card shadow="always" style="margin-left: 20px" v-if="this.data.isComputerInfoBind === true">
    <div slot="header" style="text-align:left">
      <h3> PC信息
      <el-button style="float: right; padding: 3px 0" type="text" @click="updateMyComputerInfo()">更新</el-button>
      </h3>
    </div>
    <div class="text item">
      电脑型号： {{ this.data.ComputerSystemModel }}
    </div>
    <div class="text item">
      操作系统： {{ this.data.OperatingSystemCaption }}
    </div>
    <div class="text item">
      IPv4地址： {{ this.data.IPv4Address }}
    </div>
    <div class="text item">
      MAC地址： {{ this.data.MACAddress }}
    </div>
    <div class="text item">
      CPU： {{ this.data.ProcessorName }}
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity01 !== ''">
      内存1： {{ this.data.PhysicalMemoryCapacity01 }}GB
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity02 !== ''">
      内存2： {{ this.data.PhysicalMemoryCapacity02 }}GB
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity03 !== ''">
      内存3： {{ this.data.PhysicalMemoryCapacity03 }}GB
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity04 !== ''">
      内存4： {{ this.data.PhysicalMemoryCapacity04 }}GB
    </div>
    <div class="text item" v-if="this.data.DiskDriveSize01 !== ''">
      硬盘1： {{ this.data.DiskDriveSize01 }}GB
    </div>
    <div class="text item" v-if="this.data.DiskDriveSize02 !== ''">
      硬盘2： {{ this.data.DiskDriveSize02 }}GB
    </div>
    <div class="text item" v-if="this.data.DiskDriveSize03 !== ''">
      硬盘3： {{ this.data.DiskDriveSize03 }}GB
    </div>
    <div class="text item" v-if="this.data.DiskDriveSize04 !== ''">
      硬盘4： {{ this.data.DiskDriveSize04 }}GB
    </div>
    <div class="text item">
      ・・・・・・<br/>
    </div>
  </el-card>
  <el-card shadow="always" style="margin-left: 20px" v-else>
    <el-button style="font-size: 16px" type="text" @click="updateMyComputerInfo()"> 您尚未绑定个人PC,请点击前往更新 </el-button>
  </el-card>
</template>

<script>
export default {
  data () {
    return {
      data: {
        isComputerInfoBind: false,
        ComputerSystemModel: '',
        OperatingSystemCaption: '',
        IPv4Address: '',
        ProcessorName: '',
        PhysicalMemoryCapacity01: '',
        PhysicalMemoryCapacity02: '',
        PhysicalMemoryCapacity03: '',
        PhysicalMemoryCapacity04: ''
      }
    }
  },
  created: function () {
    if (sessionStorage.getItem('mac') !== null) {
      this.data.isComputerInfoBind = true
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
            this.data.ProcessorName = response.data.params.ProcessorName
            this.data.IPv4Address = response.data.params.IPv4Address
            this.data.OperatingSystemCaption = response.data.params.OperatingSystemCaption
            this.data.PhysicalMemoryCapacity01 = response.data.params.PhysicalMemoryCapacity01
            this.data.PhysicalMemoryCapacity02 = response.data.params.PhysicalMemoryCapacity02
            this.data.PhysicalMemoryCapacity04 = response.data.params.PhysicalMemoryCapacity03
            this.data.PhysicalMemoryCapacity03 = response.data.params.PhysicalMemoryCapacity04
            this.data.DiskDriveSize01 = response.data.params.DiskDriveSize01
            this.data.DiskDriveSize02 = response.data.params.DiskDriveSize02
            this.data.DiskDriveSize03 = response.data.params.DiskDriveSize03
            this.data.DiskDriveSize04 = response.data.params.DiskDriveSize04
          }
        })
    }
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
