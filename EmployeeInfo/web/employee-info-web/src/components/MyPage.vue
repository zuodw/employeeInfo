<template>
  <div>
    <EmployeeInfoCardVue></EmployeeInfoCardVue>
    <ComputerInfoCardVue></ComputerInfoCardVue>
  </div>
</template>

<script>
import EmployeeInfoCard from '@/components/EmployeeInfoCard.vue'
import ComputerInfoCard from '@/components/ComputerInfoCard.vue'

export default {
  data () {
    return {
      data: {
      }
    }
  },
  components: {
    'EmployeeInfoCardVue': EmployeeInfoCard,
    'ComputerInfoCardVue': ComputerInfoCard
  }
}
</script>
