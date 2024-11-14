<template>
  <div class="home">
    <el-card style="margin: 0px 0 20px 20px; background: #ece8d9">
      <div style="width: 300px">
        <span style="font-size: 32px">tops news stories</span>
      </div>
      <el-carousel
        :interval="5000"
        arrow="always"
        type="card"
        style="width: 100%"
      >
        <el-carousel-item
          v-for="(item, index) in data.articles.L"
          :key="index"
          class="carousel-item"
        >
          <div
            class="background"
            :style="{
              backgroundImage: 'url(' + item.M.urlToImage.S + ')',
            }"
            @click="handleClick(item)"
          >
            <div class="overlay">
              <h3>{{ item.M.title.S }}</h3>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </el-card>
    <el-card style="margin: 20px 0 20px 20px; background: #ece8d9">
      <div class="categorier">
        <div class="categorier_title">Categories</div>
        <el-row :gutter="5">
          <el-col :span="5" :offset="2">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Business',
                      },
                    });
                  }
                "
                :src="data.articles.L[0].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>business</span>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Entertainment',
                      },
                    });
                  }
                "
                :src="data.articles.L[1].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>entertainment</span>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'General',
                      },
                    });
                  }
                "
                :src="data.articles.L[2].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>general</span>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Health',
                      },
                    });
                  }
                "
                :src="data.articles.L[3].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>health</span>
            </div>
          </el-col>
        </el-row>
        <el-row :gutter="5">
          <el-col :span="5" :offset="4">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Science',
                      },
                    });
                  }
                "
                :src="data.articles.L[4].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>science</span>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Sports',
                      },
                    });
                  }
                "
                :src="data.articles.L[5].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>sports</span>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="categorier_img_container">
              <img
                @click="
                  () => {
                    this.$router.push({
                      path: '/about',
                      query: {
                        title: 'Technology',
                      },
                    });
                  }
                "
                :src="data.articles.L[6].M.urlToImage.S"
                alt=""
                width="120px"
                height="120px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span>technology</span>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <el-dialog v-if="dialogVisible" :visible.sync="dialogVisible" width="50%">
      <div class="summary">
        <el-card style="background: #b7e4c7">
          <el-descriptions :title="dialogData.M.title.S" :column="1">
            <el-descriptions-item label="description">{{
              dialogData.M.description.S
            }}</el-descriptions-item>
            <el-descriptions-item label="content">{{
              dialogData.M.content.S
            }}</el-descriptions-item>
          </el-descriptions>
          <!-- <div>
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
          </div> -->
        </el-card>
      </div>
    </el-dialog>
  </div>
</template>

<script>
const topNewsata = require("../assets/top_news.json");

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      data: topNewsata,
      categorier: [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
      ],
      showTooltip: null,
      leftShow: true,
      isDown: [
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
      ],
      images: [
        require("@/assets/1.png"),
        require("@/assets/2.png"),
        require("@/assets/3.png"),
        require("@/assets/4.png"),
        require("@/assets/5.png"),
        require("@/assets/6.png"),
        require("@/assets/7.png"),
        require("@/assets/8.png"),
        require("@/assets/9.png"),
        require("@/assets/1.png"),
        require("@/assets/2.png"),
        require("@/assets/3.png"),
        require("@/assets/4.png"),
        require("@/assets/5.png"),
        require("@/assets/6.png"),
        require("@/assets/7.png"),
        require("@/assets/8.png"),
        require("@/assets/9.png"),
      ],
      classOption: {
        limitMoveNum: 9,
        direction: 3,
      },
      stockdio_events: true,
      dialogVisible: false,
      dialogData: null,
    };
  },
  created() {
    this.init();
  },
  methods: {
    isLeftShow() {
      this.leftShow = !this.leftShow;
    },
    init() {
      if (typeof stockdio_events == "undefined") {
        this.stockdio_events = true;
        var stockdio_eventMethod = window.addEventListener
          ? "addEventListener"
          : "attachEvent";
        var stockdio_eventer = window[stockdio_eventMethod];
        var stockdio_messageEvent =
          stockdio_eventMethod == "attachEvent" ? "onmessage" : "message";
        stockdio_eventer(
          stockdio_messageEvent,
          function (e) {
            if (
              typeof e.data != "undefined" &&
              typeof e.data.method != "undefined"
            ) {
              eval(e.data.method);
            }
          },
          false
        );
      }
    },
    handleClick(item) {
      this.dialogData = item;
      this.dialogVisible = true;
      console.log("dialogData", this.dialogData);
    },
  },
};
</script>

<style scoped>
@font-face {
  font-family: "warriot-Bold";
  src: url("../assets/font/warriot-Bold.ttf");
}
@font-face {
  font-family: "knorke";
  src: url("../assets/font/Knorke.ttf");
}
.home {
  background: #494949;
}

.carousel-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

.background {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  position: relative;
}

.overlay {
  position: absolute;
  width: 100%;
  bottom: 0px;
  left: 0px;
  color: white;
  background: rgba(0, 0, 0, 0.5);
  padding: 10px;
}

.categorier {
  margin: 10px 0 20px 34px;
}
.categorier span {
  font-family: "knorke";
}

.categorier_title {
  padding: 10px;
  font-size: 64px;
  border-bottom: #978f8f solid 1px;
  margin-bottom: 10px;
}
.categorier_img_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.summary {
  /* margin: 40px; */
  /* padding: 20px; */
  display: flex;
  justify-content: center;
  align-items: center;
}
::v-deep .el-descriptions__table {
  background: #b7e4c7;
}
::v-deep .el-dialog__body {
  padding: 30px 40px;
}
</style>
