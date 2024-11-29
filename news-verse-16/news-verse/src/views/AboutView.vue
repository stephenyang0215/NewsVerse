<template>
  <div class="about">
    <div class="top">
      <div style="display: flex; padding: 10px; width: 40px" @click="goBack">
        <i class="el-icon-back" style="color: #fff; cursor: pointer"></i>
      </div>
      <h1 class="title">{{ pageTitle }}</h1>
    </div>
    <div class="content">
      <el-card style="background: #e0e1dd; width: 78%" v-loading="loading">
        <div v-if="tableData.length !== 0">
          <div style="min-height: 555px">
            <div v-for="(item, i) in paginatedData" :key="i">
              <div class="itemContainer">
                <div class="textContainer">
                  {{ item.topic }}
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
                <el-card style="background: #c0bdc1">
                  <el-descriptions :title="item.topic" :column="1">
                    <el-descriptions-item label="summary">{{
                      item.summary
                    }}</el-descriptions-item>
                  </el-descriptions>
                  <div>
                    <ul class="ul-item">
                      <li
                        class="li-item"
                        v-for="(i, index) in item.news_sources"
                        :key="index"
                      >
                        {{ i.title }}
                        <el-link
                          :href="'https://' + getDomain(i.url)"
                          target="_blank"
                          type="primary"
                          >{{ getDomain(i.url) }}</el-link
                        >
                        keyword:
                        <span
                          v-for="(kitem, k) in i.keywords"
                          @click="filterNewsByKeyword(kitem)"
                          style="
                            margin: 0px 5px 0px 5px;
                            color: #409eff;
                            border-bottom: 1px solid #409eff;
                            cursor: pointer;
                          "
                          :key="k"
                          >{{ kitem }}</span
                        >
                        Score :{{ i.bias }}
                        <el-popover
                          placement="top-start"
                          width="600"
                          trigger="hover"
                          content="Stay informed with concise summaries and objective bias ratings across business, entertainment, health, science, sports, and technology news. Each category is organized by topic for streamlined browsing, while bias is rated from 0-3 (left-leaning), 4-6 (neutral), and 7-10 (right-leaning). Access diverse perspectives and make informed decisions with ease."
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
          </div>
          <div class="pagination">
            <button @click="prevPage" :disabled="currentPage === 1">
              <img src="@/assets/previous.png" alt="← Previous" />
            </button>
            <span>page {{ currentPage }} </span>
            <button @click="nextPage" :disabled="currentPage === totalPages">
              <img src="@/assets/next.png" alt="next →" />
            </button>
          </div>
        </div>
        <div
          style="
            min-height: 663px;
            display: flex;
            align-items: center;
            justify-content: center;
          "
          v-else
        >
          <el-empty
            description="No results found for the given keyword."
          ></el-empty>
        </div>
      </el-card>
      <el-card
        style="background: #ece8d9; width: 20%; margin-left: 20px"
        v-loading="loading"
      >
        <div style="font-size: 24px; font-weight: 700; margin-bottom: 20px">
          Top Keywords List
        </div>
        <div
          v-for="(item, index) in topKeywords"
          :key="index"
          style="margin-top: 15px; cursor: pointer"
          @click="filterNewsByKeyword(item.keyword)"
        >
          <div style="margin-bottom: 5px; font-weight: 700; font-size: 18px">
            {{ item.keyword }}
          </div>
          <div style="color: grey">frequency:{{ item.frequency }}</div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
// const data = require("../assets/data.json");
// const data = require("../assets/final_output_1107.json");
import {
  getCategotiesDataAPI,
  getKeywordsDataAPI,
  getSearchDataAPI,
} from "@/api/index";

export default {
  data() {
    return {
      pageTitle: "",
      tableData: [],
      currentPage: 1,
      itemsPerPage: 5,
      isDown: [false, false, false, false, false],
      linkList: {},
      topKeywords: [],
      data: null,
      loading: false,
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
    filterNewsByKeyword(keyword) {
      this.loading = true;
      this.pageTitle = keyword;
      this.getSecrchData({ keyword: keyword, id: 1 });
    },
    async getData() {
      this.loading = true;
      switch (this.$route.query.title) {
        case "Business":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.business;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "Entertainment":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.entertainment;

            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "General":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.general;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "Health":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.health;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "Science":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.science;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "Sports":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.sports;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        case "Technology":
          try {
            const res = await getCategotiesDataAPI();
            this.data = res;
            this.tableData = this.data.technology;
            this.loading = false;
          } catch (error) {
            console.error(error);
          } finally {
            this.loading = false;
          }
          break;
        default:
          this.filterNewsByKeyword(this.$route.query.title);
      }
    },
    async getKeywords() {
      try {
        const res = await getKeywordsDataAPI();
        this.topKeywords = res.slice(0, 10);
      } catch (error) {
        console.error(error);
      }
    },
    async getSecrchData(data) {
      try {
        const res = await getSearchDataAPI(data);
        const filteredNews = {
          item: res,
        };
        console.log("filteredNews", filteredNews);

        this.tableData = filteredNews;
        this.loading = false;
      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
  computed: {
    totalPages() {
      if (this.tableData.length !== 0) {
        return Math.ceil(this.tableData.item.length / this.itemsPerPage);
      } else {
        return null;
      }
    },
    paginatedData() {
      if (this.tableData.length !== 0) {
        const start = (this.currentPage - 1) * this.itemsPerPage;
        return this.tableData.item.slice(start, start + this.itemsPerPage);
      } else {
        return null;
      }
    },
  },
  created() {
    this.getData();
    this.getKeywords();
  },
};
</script>

<style scoped>
@font-face {
  font-family: "knorke";
  src: url("../assets/font/Knorke.ttf");
}
.about {
  background: #0d1b2a;
}
.title {
  font-family: "knorke";
  color: #d7d1d1;
}
.content {
  padding: 0px 100px 100px 100px;
  display: flex;
  margin-bottom: 13px;
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
  text-align: left;
}
::v-deep .el-descriptions__table {
  background: #c0bdc1;
}
</style>
