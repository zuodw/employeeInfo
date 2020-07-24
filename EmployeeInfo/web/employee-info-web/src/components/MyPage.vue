<template>
  <div>
    <el-row>
      <el-col :span="8">
        <EmployeeInfoCardVue></EmployeeInfoCardVue>
      </el-col>
      <el-col :span="8">
        <ComputerInfoCardVue></ComputerInfoCardVue>
      </el-col>
    </el-row>
    <el-button style="margin-left: 20px" type="danger" @click="deleteMyInfo()">删除个人信息</el-button>
  </div>
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
  },
  methods: {
    deleteMyInfo: function () {
      this.$confirm('操作将永久删除您的个人信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios
          .post('/api/DeleteEmployeeInfo', {
            params: {
              'mail': sessionStorage.getItem('userMail')
            }
          })
          .then(response => {
            if (response.data.errCode === '0') {
              sessionStorage.removeItem('userMail')
              this.$router.replace('/')
            }
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>
