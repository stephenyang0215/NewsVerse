<template>
  <div class="home">
    <el-container>
      <el-container>
        <el-header>
          <img
            src="../assets/main logo.png"
            alt=""
            width="50px"
            height="50px"
            style="float: left"
          />
        </el-header>
        <el-main>
          <div style="width: 400px">
            <div class="title">News Verse</div>
          </div>
          <el-card style="margin: 20px 0 20px 20px; background: #ece8d9">
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
              <div class="categorier_title">Categorier</div>
              <el-row :gutter="5">
                <el-col :span="5" :offset="2">
                  <div class="categorier_img_container">
                    <img
                      @click="
                        () => {
                          this.$router.push({
                            path: '/about',
                            query: { title: 'Business' },
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
                            query: { title: 'Entertainment' },
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
                            query: { title: 'General' },
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
                            query: { title: 'Health' },
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
                            query: { title: 'Science' },
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
                            query: { title: 'Sports' },
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
                            query: { title: 'Technology' },
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
        </el-main>
      </el-container>
      <div v-if="leftShow" @click="isLeftShow" style="margin-top: 25px">
        <i class="el-icon-arrow-right" style="color: #fff"></i>
      </div>
      <div v-if="!leftShow" @click="isLeftShow" style="margin-top: 25px">
        <i class="el-icon-arrow-left" style="color: #fff"></i>
      </div>
      <el-aside v-if="leftShow">
        <el-card style="background-color: #ece8d9; height: 99%">
          <div style=""><h2>widgets</h2></div>
          <el-collapse accordion>
            <el-collapse-item>
              <template slot="title">
                <i
                  class="el-icon-moon"
                  style="font-size: 20px; margin-right: 5px"
                ></i>
                <span style="font-family: knorke">Weather</span>
              </template>
              <div>
                <WeatherDetail />
              </div>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <i
                  class="el-icon-alarm-clock"
                  style="font-size: 20px; margin-right: 5px"
                ></i
                ><span style="font-family: knorke">Time</span>
              </template>
              <div>
                <BostonClock />
              </div>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <i
                  class="el-icon-data-line"
                  style="font-size: 20px; margin-right: 5px"
                ></i
                ><span style="font-family: knorke">Shares</span>
              </template>
              <iframe
                id="st_c90090eb416e4d159c5383b345474ef5"
                frameBorder="0"
                scrolling="no"
                width="238"
                height="100%"
                src="https://api.stockdio.com/visualization/financial/charts/v1/MarketOverviewChart?app-key=2188E1E9E21944319FE2009AF7B66B8A&palette=Financial-Light&title=Market%20Overview&width=300px&onload=st_c90090eb416e4d159c5383b345474ef5"
              ></iframe>
            </el-collapse-item>
            <el-collapse-item>
              <template slot="title">
                <i
                  class="el-icon-headset"
                  style="font-size: 20px; margin-right: 5px"
                ></i
                ><span style="font-family: knorke">Music</span>
              </template>
              <div>
                <MusicPlayer />
              </div>
            </el-collapse-item>
          </el-collapse>
        </el-card>
      </el-aside>
    </el-container>
    <div style="margin: 0 20px 20px 20px">
      <vue-seamless-scroll
        :data="images"
        :class-option="classOption"
        class="warp"
      >
        <ul class="ul-item">
          <li class="li-item" v-for="(item, index) in images" :key="index">
            <img :src="item" alt="" style="width: 120px; height: 120px" />
          </li>
        </ul>
      </vue-seamless-scroll>
    </div>

    <footer class="footer">
      <div style="color: rgb(102, 108, 110)">Project from Group 3</div>
      <div style="color: #fff; display: flex">
        <div style="padding-right: 20px; border-right: #fff solid 1px">
          Contact Us
        </div>
        <div style="padding-left: 20px">Group message</div>
      </div>
    </footer>
  </div>
</template>

<script>
import vueSeamlessScroll from "vue-seamless-scroll";

import BostonClock from "@/components/BostonClock.vue";
import WeatherDetail from "@/components/WeatherDetail.vue";
import MusicPlayer from "@/components/MusicPalyer.vue";

const data = require("../assets/data.json");
export default {
  name: "HomeView",
  components: {
    vueSeamlessScroll,
    BostonClock,
    WeatherDetail,
    MusicPlayer,
  },
  data() {
    return {
      data: data,
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
.el-aside {
  color: #333;
  padding: 20px 20px 20px 0;
}

.el-main {
  color: #333;
  padding: 5px;
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
.title {
  font-size: 64px;
  font-family: "warriot-Bold";
  color: #978f8f;
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
.footer {
  height: 80px;
  background-color: rgb(20, 30, 40);
  display: flex;
  align-items: center;
  padding: 0 200px 0 200px;
  justify-content: space-between;
}
.scroll_conainer {
  width: 100%;
  overflow: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.scroll_conainer::-webkit-scrollbar {
  display: none;
}

.warp {
  width: 130px * 9;
  height: 120px;
  margin: 0 auto;
  overflow: hidden;
}
ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
}
.ul-item {
  display: flex;
}
.li-item {
  width: 120px;
  height: 120px;
  margin-right: 10px;
  line-height: 120px;
  background-color: #999;
  color: #fff;
  text-align: center;
  font-size: 30px;
}
::v-deep .el-collapse-item .el-collapse-item__header {
  background-color: #ece8d9 !important;
}
::v-deep .el-collapse-item__content {
  padding-bottom: 0px;
}
::v-deep .el-collapse-item__wrap {
  background-color: #b7e4c7;
  border: none;
  border-radius: 10px;
}
</style>
