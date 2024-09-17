<template>
  <div class="plate-container">
    <el-divider>
      <b class="text primary fz18">· Moodle ·</b>
    </el-divider>

    <div :gutter="16" class="plate-wrapper">
      <div v-for="item in plateList" :key="item.key" class="plate-item" @click="golist(item)">
        <div class="item-icon">
          <i :class="item.icon" />
        </div>
        <div class="item-label">{{ item.label }}</div>
      </div>
    </div>

    <List />
  </div>
</template>

<script>
import List from '@/components/List'
import scrollTopMixin from '@/mixins/scroll-top-mixin'

export default {
  name: 'Plate',
  components: { List },
  mixins: [scrollTopMixin],
  data() {
    return {
      plateList: [
        {
          label: 'POLITICS',
          icon: 'el-icon-info',
          key: 1
        },
        {
          label: 'MUDDLE TALKING',
          icon: 'el-icon-s-comment',
          key: 2
        },
        {
          label: 'RESOURCE SHARING',
          icon: 'el-icon-message-solid',
          key: 3
        },
        {
          label: 'GAME ZONE',
          icon: 'el-icon-mouse',
          key: 4
        }
      ]
    }
  },

  methods: {
    golist(item) {
      this.$router.push({
        path: '/list',
        query: { ...item }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/plate.scss';
</style>
