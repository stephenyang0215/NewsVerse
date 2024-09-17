<template>
  <el-row :gutter="8" class="list-item-container" @click.native="goComment">
    <el-col :span="24">
      <div class="list-item-title">{{ info.title }}</div>
      <div class="list-item-content" v-html="removeHtmlTags(info.content)"></div>
      <div class="list-item-info">
        <span>{{ info.createTime }}</span>
        <b class="text primary ml10">{{ info.userName }}</b>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import { mapGetters } from 'vuex'
import { removeHtmlTags } from '@/utils'

export default {
  name: 'ListItem',

  props: {
    info: {
      type: Object,
      required: true
    }
  },

  computed: {
    ...mapGetters(['userInfo'])
  },

  methods: {
    goComment() {
      if (this.userInfo) {
        const query = {
          key: this.info.parentKey,
          ...this.$route.query,
          itemId: this.info.id,
          originPath: this.$route.fullPath
        }
        // Record current paging when list page jumps
        if (this.$route.path === '/list') query.currentPage = this.$parent.currentPage
        this.$router.push({
          path: '/comment',
          query
        })
      } else {
        this.$router.push({
          path: '/login',
          query: { originPath: this.$route.fullPath }
        })
      }
    },

    removeHtmlTags
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/list.scss';
</style>
