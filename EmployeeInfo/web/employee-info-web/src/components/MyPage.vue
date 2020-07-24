<template>
  <el-row>
    <el-col :span="8">
      <EmployeeInfoCardVue></EmployeeInfoCardVue>
    </el-col>
    <el-col :span="8">
      <ComputerInfoCardVue></ComputerInfoCardVue>
    </el-col>
  </el-row>
</template>

<script>
import EmployeeInfoCard from '@/components/EmployeeInfoCard.vue'
import ComputerInfoCard from '@/components/ComputerInfoCard.vue'

export default {
  data () {
    return {
      data: {
        isComputerInfoBind: false
      }
    }
  },
  created: function () {
  },
  components: {
    'EmployeeInfoCardVue': EmployeeInfoCard,
    'ComputerInfoCardVue': ComputerInfoCard
  }
}
</script>
