<template>
  <el-card shadow="always" style="margin-left: 20px" v-if="this.data.isComputerInfoBind === true">
    <div slot="header" style="text-align:left">
      <h3> PC信息
      <el-button style="float: right; padding: 3px 0" type="text" @click="updateMyComputerInfo()">更新</el-button>
      </h3>
    </div>
    <div class="text item">
      电脑番号： {{ this.data.ProcessorSystemName }}
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
      内存1： {{ this.data.PhysicalMemoryCapacity01 }}GB &nbsp;&nbsp;&nbsp;&nbsp; {{ this.data.PhysicalMemorySpeed01 }}MHz
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity02 !== ''">
      内存2： {{ this.data.PhysicalMemoryCapacity02 }}GB &nbsp;&nbsp;&nbsp;&nbsp; {{ this.data.PhysicalMemorySpeed02 }}MHz
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity03 !== ''">
      内存3： {{ this.data.PhysicalMemoryCapacity03 }}GB &nbsp;&nbsp;&nbsp;&nbsp; {{ this.data.PhysicalMemorySpeed03 }}MHz
    </div>
    <div class="text item" v-if="this.data.PhysicalMemoryCapacity04 !== ''">
      内存4： {{ this.data.PhysicalMemoryCapacity04 }}GB &nbsp;&nbsp;&nbsp;&nbsp; {{ this.data.PhysicalMemorySpeed04 }}MHz
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
    <h3> 请按以下步骤更新并绑定PC信息 </h3>
    <ComputerInfoSetMainVue v-on:updateComputerInfoCard="updateComputerInfoCard" ></ComputerInfoSetMainVue>
  </el-card>
</template>

<script>
import ComputerInfoSetMain from '@/components/ComputerInfoSetMain.vue'

export default {
  data () {
    return {
      data: {
        isComputerInfoBind: false,
        ComputerSystemModel: '',
        OperatingSystemCaption: '',
        IPv4Address: '',
        ProcessorSystemName: '',
        ProcessorName: '',
        PhysicalMemoryCapacity01: '',
        PhysicalMemorySpeed01: '',
        PhysicalMemoryCapacity02: '',
        PhysicalMemorySpeed02: '',
        PhysicalMemoryCapacity03: '',
        PhysicalMemorySpeed03: '',
        PhysicalMemoryCapacity04: '',
        PhysicalMemorySpeed04: '',
        DiskDriveSize01: '',
        DiskDriveSize02: '',
        DiskDriveSize03: '',
        DiskDriveSize04: ''
      }
    }
  },
  components: {
    'ComputerInfoSetMainVue': ComputerInfoSetMain
  },
  methods: {
    updateMyComputerInfo: function () {
      this.data.isComputerInfoBind = false
    },
    updateComputerInfo () {
      this.$axios
        .get('/api/GetComputerInfoByUserMail', {
          params: {
            'mail': sessionStorage.getItem('userMail')
          }
        })
        .then(response => {
          if (response.data.errCode === '0') {
            sessionStorage.setItem('mac', response.data.params.MACAddress)
            this.data.isComputerInfoBind = true

            this.data.ComputerSystemModel = response.data.params.ComputerSystemModel
            this.data.ProcessorSystemName = response.data.params.ProcessorSystemName
            this.data.ProcessorName = response.data.params.ProcessorName
            this.data.IPv4Address = response.data.params.IPv4Address
            this.data.MACAddress = response.data.params.MACAddress
            this.data.OperatingSystemCaption = response.data.params.OperatingSystemCaption
            this.data.PhysicalMemoryCapacity01 = response.data.params.PhysicalMemoryCapacity01
            this.data.PhysicalMemoryCapacity01 = response.data.params.PhysicalMemoryCapacity01
            this.data.PhysicalMemorySpeed01 = response.data.params.PhysicalMemorySpeed01
            this.data.PhysicalMemoryCapacity02 = response.data.params.PhysicalMemoryCapacity02
            this.data.PhysicalMemorySpeed02 = response.data.params.PhysicalMemorySpeed02
            this.data.PhysicalMemoryCapacity03 = response.data.params.PhysicalMemoryCapacity03
            this.data.PhysicalMemorySpeed03 = response.data.params.PhysicalMemorySpeed03
            this.data.PhysicalMemoryCapacity04 = response.data.params.PhysicalMemoryCapacity04
            this.data.PhysicalMemorySpeed04 = response.data.params.PhysicalMemorySpeed04
            this.data.DiskDriveSize01 = response.data.params.DiskDriveSize01
            this.data.DiskDriveSize02 = response.data.params.DiskDriveSize02
            this.data.DiskDriveSize03 = response.data.params.DiskDriveSize03
            this.data.DiskDriveSize04 = response.data.params.DiskDriveSize04
          }
        })
    },
    updateComputerInfoCard: function () {
      this.updateComputerInfo()
      this.$forceUpdate()
    }
  },
  created: function () {
    this.updateComputerInfo()
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
