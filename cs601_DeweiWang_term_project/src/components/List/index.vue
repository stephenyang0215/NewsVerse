<template>
  <div class="list-container">
    <el-divider>
      <b class="text primary fz18">
        <i :class="plateIcon"></i>
        {{ plateName }}
      </b>
    </el-divider>

    <template v-if="list.length">
      <ListItem v-for="(item, index) in list.slice(startIndex, endIndex)" :key="index" :info="item" @toggleActive="toggleActive(index)" />
    </template>
    <el-empty v-else description="No posting here.">
      <el-button icon="el-icon-edit-outline" type="primary" size="mini" title="button" @click="add">Posting</el-button>
    </el-empty>

    <div v-if="showPage" class="page-wrapper">
      <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="list.length"
        :disabled="!list.length"
        layout="total, prev, pager, next, jumper"
        small
        background
        @current-change="handleCurrentChange"
      />
    </div>
  </div>
</template>

<script>
import ListItem from './Item.vue'
import { mapGetters } from 'vuex'
import scrollTopMixin from '@/mixins/scroll-top-mixin'

export default {
  name: 'List',
  components: { ListItem },
  mixins: [scrollTopMixin],
  data() {
    return {
      plateIcon: null,
      plateName: null,
      plateKey: null,
      list: [],
      currentPage: 1,
      pageSize: 5
    }
  },

  computed: {
    ...mapGetters(['userInfo', 'listData']),
    startIndex() {
      return (this.currentPage - 1) * this.pageSize
    },
    endIndex() {
      return this.startIndex + this.pageSize
    },
    showPage() {
      return this.$route.path === '/list'
    }
  },

  created() {
    this.init()
  },

  methods: {
    init() {
      const { label, key, icon } = this.$route.query
      this.plateIcon = icon
      this.plateName = label || '· Hot Posts ·'
      this.plateKey = key
      this.getList()
      this.getCurrentPageFromRouter()
    },

    getList() {
      if (this.plateKey) {
        this.list = this.listData[this.plateKey]
      } else {
        // Data displayed on the board page Take out the latest three data by time
        const hotNews = Object.values(this.listData).flat()

        hotNews.sort(function (a, b) {
          return new Date(b.createTime).getTime() - new Date(a.createTime).getTime()
        })

        this.list = hotNews.slice(0, 3)
      }
    },

    getCurrentPageFromRouter() {
      const { currentPage } = this.$route.query
      if (currentPage) {
        this.currentPage = Number(currentPage)
      }
    },

    add() {
      if (this.userInfo) {
        this.$router.push({
          path: '/add',
          query: { ...this.$route.query, originPath: this.$route.fullPath }
        })
      } else {
        this.$router.push('/login')
      }
    },

    handleCurrentChange(val) {
      this.currentPage = val
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/list.scss';
</style>
