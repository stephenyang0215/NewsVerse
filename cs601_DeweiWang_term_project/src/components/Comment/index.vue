<template>
  <div ref="comment-todo-list-container" class="comment-todo-list-container">
    <template v-loading="!current">
      <div class="comment-todo-list-header">
        <span :title="current.title" class="todo-list-title single-line-ellipsis">{{ current.title }}</span>
        <div class="btns">
          <el-button size="mini" icon="el-icon-chat-dot-square" title="button" @click="handleRecover">Reply</el-button>
          <el-button size="mini" icon="el-icon-back" title="button" @click="handleBack">Back</el-button>
        </div>
      </div>

      <FloorItem :row="current" :index="0" isOrigin @recover="handleRecover" />

      <FloorItem
        v-for="(item, index) in current.otherFloors.slice(startIndex, endIndex)"
        :key="index"
        :row="item"
        :index="(currentPage - 1) * pageSize + index + 1"
      />

      <div class="page-wrapper">
        <el-pagination
          :current-page="currentPage"
          :page-size="pageSize"
          :total="current.otherFloors.length"
          :disabled="!current.otherFloors.length"
          layout="total, prev, pager, next, jumper"
          ref="page"
          small
          background
          @current-change="handleCurrentChange"
        />
      </div>

      <div class="comment-rich-text-wrapper">
        <div class="comment-rich-text-title">Post a reply</div>
        <template>
          <Editor v-model="commentContent" :min-height="192" />
        </template>
        <div ref="rich-text-btn" class="rich-text-btn">
          <el-button
            :loading="addBtnLoading"
            :disabled="!removeHtmlTags(commentContent)"
            type="primary"
            size="mini"
            class="recover-btn"
            title="button"
            @click="handleAddComment"
            >Reply
          </el-button>
        </div>
      </div>

      <el-backtop target=".comment-todo-list-container" />
    </template>
  </div>
</template>

<script>
import { getTime, removeHtmlTags } from '@/utils'
import { mapGetters } from 'vuex'
import FloorItem from './FloorItem.vue'
import Editor from '@/components/Editor'

export default {
  name: 'Comment',
  components: { FloorItem, Editor },
  data() {
    return {
      current: null,
      commentContent: null,
      addBtnLoading: false,
      currentPage: 1,
      pageSize: 5
    }
  },

  created() {
    this.init()
  },

  computed: {
    ...mapGetters(['userInfo', 'listData']),
    startIndex() {
      return (this.currentPage - 1) * this.pageSize
    },
    endIndex() {
      return this.startIndex + this.pageSize
    }
  },

  methods: {
    init() {
      this.getCurrent()
      document.documentElement.scrollTo(0, 0)
    },

    getCurrent() {
      const { key, itemId } = this.$route.query
      const info = this.listData[key]
      this.current = info.find((item) => item.id === itemId)
    },

    // Scrolls the reply area into the view
    handleRecover() {
      this.$refs['rich-text-btn'].scrollIntoView({
        behavior: 'smooth',
        block: 'end'
      })
    },

    handleBack() {
      this.$router.push({
        path: this.$route.query.originPath,
        query: { currentPage: this.$route.query.currentPage }
      })
    },

    handleAddComment() {
      this.addBtnLoading = true
      setTimeout(() => {
        const params = {
          id: Date.now() + '',
          content: this.commentContent,
          createTime: getTime(),
          userName: this.userInfo.userName,
          showRecoverBtn: false
        }
        this.current.otherFloors.push(params)
        this.$store.commit('list/SET_LIST_DATA', this.listData)
        this.commentContent = null
        this.addBtnLoading = false
        this.$nextTick(() => {
          const lastPage = this.$refs.page.internalPageCount
          this.currentPage = lastPage
        })
      }, 240)
    },

    handleCurrentChange(val) {
      this.currentPage = val
      document.documentElement.scrollTo(0, 0)
    },

    removeHtmlTags
  }
}
</script>
<style lang="scss" scoped>
@import '~@/styles/components/comment.scss';
</style>
