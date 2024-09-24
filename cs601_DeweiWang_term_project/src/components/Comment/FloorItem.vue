<template>
  <div class="floor-item-container" :class="{ 'first-floor-wrapper': isOrigin }">
    <div class="floor-wrapper">
      <div class="floor-user-wrapper">
        <div :title="row.userName" class="floor-user-name single-line-ellipsis">{{ row.userName }}</div>
        <el-tag v-if="isOrigin" type="warning" effect="dark" size="mini">Original poster</el-tag>
      </div>
      <div class="floor-content-wrapper">
        <template v-if="row && (row.content || row.replyContent)">
          <div class="floor-content-html" v-html="row.content" />
        </template>
        <el-empty v-else description="No posting here" />
        <div class="floor-content-footer">
          <span v-if="isOrigin" class="floor-footer-item">Floor 1</span>
          <span v-else class="floor-footer-item">Floor {{ index + 1 }}</span>
          <span class="floor-footer-item">{{ row.createTime }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FloorItem',

  props: {
    index: {
      type: [String, Number],
      required: true
    },
    row: {
      type: Object,
      required: true
    },
    isOrigin: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/FloorItem.scss';
</style>
