<template>
  <div class="about">
    <div class="top">
      <div style="display: flex; padding: 10px" @click="goBack">
        <i class="el-icon-back"></i>
      </div>
      <h1>{{ pageTitle }}</h1>
    </div>
    <div class="content">
      <div v-for="(item, i) in paginatedData" :key="i">
        <div class="itemContainer">
          <div class="textContainer">
            {{ item.M.title.S }}
          </div>
          <div
            v-if="!isDown[i]"
            @click="downClick(i)"
            style="cursor: pointer; font-size: 32px"
          >
            <i class="el-icon-arrow-down"></i>
          </div>
          <div
            v-if="isDown[i]"
            @click="downClick(i)"
            style="cursor: pointer; font-size: 32px"
          >
            <i class="el-icon-arrow-up"></i>
          </div>
        </div>
        <div v-if="isDown[i]" class="summary">
          <el-card>
            <el-descriptions :title="item.M.title.S" column="1">
              <el-descriptions-item label="description">{{
                item.M.description.S
              }}</el-descriptions-item>
              <el-descriptions-item label="content">{{
                item.M.content.S
              }}</el-descriptions-item>
            </el-descriptions>
          </el-card>
        </div>
      </div>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
        <span>第 {{ currentPage }} 页</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">
          下一页
        </button>
      </div>
    </div>
  </div>
</template>

<script>
const data = require("../assets/data.json");

export default {
  data() {
    return {
      pageTitle: this.$route.query.title,
      data: data,
      currentPage: 1,
      itemsPerPage: 5,
      isDown: [false, false, false, false, false],
    };
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
      this.isDown = [false, false, false, false, false];
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
      this.isDown = [false, false, false, false, false];
    },
    downClick(i) {
      console.log("click");
      this.$set(this.isDown, i, !this.isDown[i]);
    },
  },
  computed: {
    totalPages() {
      return Math.ceil(this.data.articles.L.length / this.itemsPerPage);
    },
    paginatedData() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.data.articles.L.slice(start, start + this.itemsPerPage);
    },
  },
  mounted() {
    console.log(this.data.articles.L);
  },
};
</script>

<style scoped>
.top {
}
.content {
  padding: 100px 300px;
}
.content-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 200px;
  background: #f1f1f1;
  border: 1px solid #ccc;
  padding: 20px;
  text-align: center;
}
.pagination {
  margin-top: 20px;
}
button {
  margin: 0 5px;
}
.textContainer {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 32px;
}
.itemContainer {
  margin: 40px;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #ccc;
}
.summary {
  margin: 40px;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
