<template>
  <div class="home-page">
    <div class="container">
      <div class="header-wrapper">
        <div class="title">CS601 Simulate Form</div>
        <div class="btns">
          <el-button v-if="showEditBtn" type="text" icon="el-icon-edit-outline" class="login-btn" title="button" @click="add">Posting</el-button>
          <el-button v-if="showPlateBtn" type="text" icon="el-icon-price-tag" class="login-btn" title="button" @click="togglePlate">Home</el-button>
          <el-button v-if="!userInfo" type="text" icon="el-icon-user" class="login-btn" title="button" @click="login">Log in</el-button>
        </div>
      </div>
      <div class="decoration" />
      <el-card>
        <Banner v-if="showBanner" />

        <router-view />
      </el-card>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/Banner'
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  components: { Banner },

  computed: {
    ...mapGetters(['userInfo']),
    showEditBtn() {
      return this.$route.path === '/list'
    },
    showPlateBtn() {
      return this.$route.path !== '/plate'
    },
    showBanner() {
      return this.$route.path !== '/comment'
    }
  },

  methods: {
    login() {
      this.$router.push('/login')
    },

    // Post
    add() {
      if (this.userInfo) {
        this.$router.push({
          path: '/add',
          query: { ...this.$route.query, originPath: this.$route.fullPath }
        })
      } else {
        this.$router.push({
          path: '/login',
          query: { originPath: this.$route.fullPath }
        })
      }
    },

    // Go back
    togglePlate() {
      this.$router.push('/plate')
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/home.scss';
</style>
