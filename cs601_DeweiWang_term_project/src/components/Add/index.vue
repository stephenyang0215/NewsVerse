<template>
  <div class="add-container">
    <el-divider> <h3 class="title">· Posting ·</h3></el-divider>
    <el-form ref="form" :model="form" :rules="rules" label-position="top" size="small">
      <el-form-item label="" prop="title">
        <b slot="label">
          Title
          <el-button
            :loading="randomTitleBtnLoading"
            icon="el-icon-collection"
            type="primary"
            size="mini"
            class="ml10"
            title="button"
            @click="createRandomTitle"
            >Random title
          </el-button>
        </b>
        <el-input v-model="form.title" placeholder="Enter a post title" clearable />
      </el-form-item>
      <el-form-item label="Content" prop="content">
        <b slot="label">
          Content
          <el-button
            :loading="randomContentBtnLoading"
            icon="el-icon-notebook-2"
            type="primary"
            size="mini"
            class="ml10"
            title="button"
            @click="createRandomContent"
            >Random content
          </el-button>
        </b>
        <Editor v-model="form.content" :min-height="192" />
      </el-form-item>
    </el-form>

    <el-button :disabled="randomTitleBtnLoading || randomContentBtnLoading" type="primary" size="small" title="button" @click="handlePublish">
      Handle
    </el-button>
  </div>
</template>

<script>
import Editor from '@/components/Editor/index.vue'
import { mapGetters } from 'vuex'
import { getTime } from '@/utils'
import { getRandomTitle, getRandomContent } from '@/api/index'

export default {
  name: 'Add',
  components: { Editor },

  data() {
    return {
      form: {
        title: null,
        content: null
      },
      rules: {
        title: [{ required: true, trigger: 'blur', message: 'Repuired' }],
        content: [{ required: true, trigger: 'blur', message: 'Repuired' }]
      },
      randomTitleBtnLoading: false,
      randomContentBtnLoading: false
    }
  },

  computed: {
    ...mapGetters(['userInfo', 'listData'])
  },

  methods: {
    handlePublish() {
      const content = {
        id: Date.now() + '',
        parentKey: this.$route.query.key,
        ...this.form,
        createTime: getTime(),
        userName: this.userInfo.userName,
        otherFloors: []
      }
      const { key } = this.$route.query
      this.listData[key].unshift(content)
      this.$store.commit('list/SET_LIST_DATA', this.listData)
      this.$router.push({
        path: this.$route.query.originPath
      })
    },

    async createRandomTitle() {
      this.randomTitleBtnLoading = true
      try {
        const res = await getRandomTitle()
        this.form.title = res.data.content
      } catch (error) {
        console.error(error)
      }
      this.randomTitleBtnLoading = false
    },

    async createRandomContent() {
      this.randomContentBtnLoading = true
      try {
        const res = await getRandomContent()
        this.form.content = res.data.value
      } catch (error) {
        console.error(error)
      }
      this.randomContentBtnLoading = false
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~@/styles/components/add.scss';
</style>
