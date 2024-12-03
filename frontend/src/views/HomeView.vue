<template>
  <div class="home">
    <el-card
      style="margin: 0px 0 20px 20px; background: #e0e1dd; height: 407px"
      v-loading="loading"
    >
      <div style="width: 300px">
        <span class="custom-font" style="font-size: 30px">
          TOPS NEWS STORIES
        </span>
      </div>
      <el-carousel
        :interval="5000"
        arrow="always"
        type="card"
        style="width: 100%"
      >
        <el-carousel-item
          v-for="(item, index) in data"
          :key="index"
          class="carousel-item"
        >
          <div
            class="background"
            :style="{
              backgroundImage: 'url(' + item.urlToImage + ')',
            }"
            @click="handleClick(item)"
          >
            <div class="overlay">
              <h3>{{ item.title }}</h3>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </el-card>
    <el-card style="margin: 20px 0 16px 20px; background: #e0e1dd">
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
                :src="images[0]"
                alt=""
                width="180px"
                height="180px"
                style="border-radius: 20px; cursor: pointer"
              />
              <span class="categories-font">business</span>
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
                :src="images[1]"
                alt=""
                width="180px"
                height="180px"
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
                :src="images[2]"
                alt=""
                width="180px"
                height="180px"
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
                :src="images[3]"
                alt=""
                width="180px"
                height="180px"
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
                :src="images[4]"
                alt=""
                width="180px"
                height="180px"
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
                :src="images[5]"
                alt=""
                width="180px"
                height="180px"
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
                :src="images[6]"
                alt=""
                width="180px"
                height="180px"
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
        <el-descriptions :title="dialogData.title" :column="1">
          <el-descriptions-item label="description">{{
            dialogData.description
          }}</el-descriptions-item>
          <el-descriptions-item label="content">{{
            dialogData.content
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
      </div>
    </el-dialog>
  </div>
</template>

<script>
// const topNewsata = require("../assets/top_news.json");
import { getTopNewsDataAPI } from "@/api/index";
import image from "@/assets/test.png";
export default {
  name: "HomeView",
  components: {},

  data() {
    return {
      imageSrc: image,
      data: null,
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
      classOption: {
        limitMoveNum: 9,
        direction: 3,
      },
      stockdio_events: true,
      dialogVisible: false,
      dialogData: null,
      images: [
        require("@/assets/business.jpg"),
        require("@/assets/entertainment.jpg"),
        require("@/assets/general.jpg"),
        require("@/assets/health.jpg"),
        require("@/assets/science.jpg"),
        require("@/assets/sports.webp"),
        require("@/assets/technology.jpg"),
      ],
      loading: false,
    };
  },
  created() {
    // this.init();
    this.getTopNewsData();
  },
  methods: {
    isLeftShow() {
      this.leftShow = !this.leftShow;
    },
    // init() {
    //   if (typeof stockdio_events == "undefined") {
    //     this.stockdio_events = true;
    //     var stockdio_eventMethod = window.addEventListener
    //       ? "addEventListener"
    //       : "attachEvent";
    //     var stockdio_eventer = window[stockdio_eventMethod];
    //     var stockdio_messageEvent =
    //       stockdio_eventMethod == "attachEvent" ? "onmessage" : "message";
    //     stockdio_eventer(
    //       stockdio_messageEvent,
    //       function (e) {
    //         if (
    //           typeof e.data != "undefined" &&
    //           typeof e.data.method != "undefined"
    //         ) {
    //           eval(e.data.method);
    //         }
    //       },
    //       false
    //     );
    //   }
    // },
    handleClick(item) {
      this.dialogData = item;
      this.dialogVisible = true;
    },
    async getTopNewsData() {
      this.loading = true;
      try {
        const res = await getTopNewsDataAPI();
        this.data = res.articles.slice(0, 10);
        console.log("topNews", this.data);
        this.loading = false;
      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
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
@font-face {
  font-family: "RobotoBlack";
  src: url("../assets/font/Roboto-Black.ttf");
}
@font-face {
  font-family: "LoraRegular";
  src: url("../assets/font/Lora-Regular.ttf");
}
.home {
  background: #494949;
}

.custom-font {
  font-family: "RobotoBlack";
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
  font-family: "LoraRegular";
}

.categorier {
  margin: 10px 0 20px 34px;
}
.categorier span {
  font-family: "RobotoBlack";
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
  background: #e2bdc1;
}
::v-deep .el-dialog__header {
  background: #e2bdc1;
}
::v-deep .el-dialog__body {
  background: #e2bdc1;
}

::v-deep .el-dialog__body {
  padding: 30px 40px;
}
</style>
