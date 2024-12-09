<template>
  <div class="home">
    <el-card
      style="margin: 0px 0 20px 20px; background: #e0e1dd"
      v-loading="loading"
    >
      <div style="background-color: #0d1b2a">
        <div style="width: 300px">
          <span class="custom-font" style="font-size: 30px">
            TOP NEWS STORIES
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
      </div>
      <hr />
      <br />
      <br />
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Business
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Entertainment
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              General
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Health
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Science
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Sports
            </span>
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
              width="250px"
              height="250px"
              style="border-radius: 20px; cursor: pointer"
            />
            <span
              class="categories-font"
              style="font-weight: bold; font-size: 24px"
            >
              Technology
            </span>
          </div>
        </el-col>
      </el-row>
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
      </div>
    </el-dialog>
  </div>
</template>

<script>
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
    this.getTopNewsData();
  },
  methods: {
    isLeftShow() {
      this.leftShow = !this.leftShow;
    },
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
  background: #e2bdc1;
}

.custom-font {
  font-family: "RobotoBlack";
  color: #e0e1dd;
}

.carousel-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

.el-carousel {
  background-color: #0d1b2a;
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
