<template>
  <div id="app">
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <!-- <router-view /> -->
    <div class="home" v-if="true">
      <el-container>
        <el-container>
          <el-header style="display: flex; align-items: center; height: 100px">
            <div class="logo" @click="goHome">
              <img src="./assets/logo.png" alt="" width="90px" height="90px" />
            </div>
            <div style="width: 400px">
              <div class="title">News Verse</div>
            </div>
          </el-header>
          <el-main>
            <router-view />
          </el-main>
        </el-container>
        <div
          v-if="leftShow"
          @click="isLeftShow"
          style="margin-top: 25px; height: 20px"
        >
          <i
            class="el-icon-arrow-right"
            style="color: #fff; cursor: pointer"
          ></i>
        </div>
        <div
          v-if="!leftShow"
          @click="isLeftShow"
          style="margin-top: 25px; height: 20px"
        >
          <i
            class="el-icon-arrow-left"
            style="color: #fff; cursor: pointer"
          ></i>
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
  </div>
</template>

<script>
import vueSeamlessScroll from "vue-seamless-scroll";

import BostonClock from "@/components/BostonClock.vue";
import WeatherDetail from "@/components/WeatherDetail.vue";
import MusicPlayer from "@/components/MusicPlayer.vue";
const topNewsata = require("./assets/top_news.json");

export default {
  components: {
    vueSeamlessScroll,
    BostonClock,
    WeatherDetail,
    MusicPlayer,
  },
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
    goHome() {
      if (this.$route.path !== "/") {
        this.$router.push("/");
      }
    },
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@font-face {
  font-family: "warriot-Bold";
  src: url("./assets/font/warriot-Bold.ttf");
}
@font-face {
  font-family: "knorke";
  src: url("./assets/font/Knorke.ttf");
}
.home {
  background: #494949;
}

/* 光泽效果 */
.logo {
  position: relative;
  overflow: hidden;
  cursor: pointer;
}
.logo::after {
  content: "";
  position: absolute;
  top: 0;
  left: -75%;
  width: 50%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(255, 255, 255, 0.4),
    transparent
  );
  transform: skewX(-25deg);
}
.logo:hover::after {
  animation: shine 1s ease-in-out forwards;
}
@keyframes shine {
  0% {
    left: -75%;
  }
  100% {
    left: 125%;
  }
}

/* 旋转放大*/
/* .logo:hover {
  transform: scale(1.25) rotate(8deg);
  transition: transform 0.3s ease;
}
.el-aside {
  color: #333;
  padding: 20px 20px 20px 0;
} */

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

.title {
  font-size: 64px;
  font-family: "warriot-Bold";
  color: #978f8f;
  margin-top: 10px;
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
::v-deep .el-dialog {
  background-color: #ece8d9;
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
