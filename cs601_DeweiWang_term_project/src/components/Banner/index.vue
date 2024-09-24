<template>
  <!-- 轮播图 -->
  <el-carousel class="banner-container" height="350px">
    <el-carousel-item>
      <img alt="BUimg" src="../../assets/images/Boston_University_seal.png" class="carousel-img" @click="openNewWindow" />
    </el-carousel-item>
    <el-carousel-item>
      <img alt="BUimg" src="../../assets/images/i_love_BU.jpg" class="carousel-img" @click="openNewWindow" />
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  name: 'Banner',

  methods: {
    openNewWindow() {
      window.open('https://www.bu.edu/', '_blank')
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/banner.scss';
</style>
