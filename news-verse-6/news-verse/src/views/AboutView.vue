<template>
  <div class="about">
    <div class="top">
      <div style="display: flex; padding: 10px" @click="goBack">
        <i class="el-icon-back" style="color: #fff"></i>
      </div>
      <h1 class="title">{{ pageTitle }}</h1>
    </div>
    <div class="content">
      <el-card style="background: #ece8d9">
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
            <el-card style="background: #b7e4c7">
              <el-descriptions :title="item.M.title.S" :column="1">
                <el-descriptions-item label="description">{{
                  item.M.description.S
                }}</el-descriptions-item>
                <el-descriptions-item label="content">{{
                  item.M.content.S
                }}</el-descriptions-item>
              </el-descriptions>
              <div>
                <ul class="ul-item">
                  <li
                    class="li-item"
                    v-for="(i, index) in item.M.news_sources"
                    :key="index"
                  >
                    {{ i.title }}
                    <el-link
                      :href="'https://' + getDomain(i.url)"
                      target="_blank"
                      type="primary"
                      >{{ getDomain(i.url) }}</el-link
                    >
                    {{ i.rank }}
                    <el-popover
                      placement="top-start"
                      width="200"
                      trigger="hover"
                      content="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    >
                      <el-button slot="reference" type="text"
                        ><i class="el-icon-warning-outline"></i
                      ></el-button>
                    </el-popover>
                  </li>
                </ul>
              </div>
            </el-card>
          </div>
        </div>
        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 1">
            ← previous
          </button>
          <span>page {{ currentPage }} </span>
          <button @click="nextPage" :disabled="currentPage === totalPages">
            next →
          </button>
        </div>
      </el-card>
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
      linkList: {},
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
      this.$set(this.isDown, i, !this.isDown[i]);
    },
    getDomain(url) {
      const start = url.indexOf("://") + 3;
      const end = url.indexOf("/", start);
      return end === -1 ? url.substring(start) : url.substring(start, end);
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
};
</script>

<style scoped>
@font-face {
  font-family: "knorke";
  src: url("../assets/font/Knorke.ttf");
}
.about {
  background: #494949;
}
.title {
  font-family: "knorke";
  color: #d7d1d1;
}
.top {
}
.content {
  padding: 0px 300px 100px 300px;
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
  border-radius: 10px;
}
.summary {
  margin: 40px;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.ul-item {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  font-size: 12px;
}
.li-item {
}
::v-deep .el-descriptions__table {
  background: #b7e4c7;
}
</style>
