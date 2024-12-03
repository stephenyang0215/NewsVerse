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
            <div style="width: 400px; margin-right: auto">
              <div class="title">News Verse</div>
            </div>
            <div v-if="this.$route.path === '/'">
              <el-input
                placeholder="Please enter keywords"
                v-model="filterWord"
                @keyup.native.enter="searchNews()"
                clearable
              >
                <i
                  slot="suffix"
                  class="el-input__icon el-icon-search"
                  @click="searchNews()"
                ></i>
              </el-input>
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
            style="color: #e54f6d; cursor: pointer"
          ></i>
        </div>
        <div
          v-if="!leftShow"
          @click="isLeftShow"
          style="margin-top: 25px; height: 20px"
        >
          <i
            class="el-icon-arrow-left"
            style="color: #e54f6d; cursor: pointer"
          ></i>
        </div>
        <el-aside v-if="leftShow">
          <el-card style="background-color: #e0e1dd; height: 98%">
            <div
              class="widget-font"
              style="font-size: 30px;font-weight:700;margin:20px;0px 20px 0px"
            >
              Widgets
            </div>
            <el-collapse accordion>
              <el-collapse-item>
                <template slot="title">
                  <div style="display: flex; align-items: center">
                    <i
                      class="el-icon-moon"
                      style="font-size: 24px; margin-right: 5px"
                    ></i>
                    <span style="font-family: LoraRegular; font-size: 18px"
                      >Weather</span
                    >
                  </div>
                </template>
                <div>
                  <WeatherDetail />
                </div>
              </el-collapse-item>
              <el-collapse-item>
                <template slot="title">
                  <div style="display: flex; align-items: center">
                    <i
                      class="el-icon-alarm-clock"
                      style="font-size: 24px; margin-right: 5px"
                    ></i
                    ><span style="font-family: LoraRegular; font-size: 18px"
                      >Time</span
                    >
                  </div>
                </template>
                <div>
                  <BostonClock />
                </div>
              </el-collapse-item>
              <el-collapse-item>
                <template slot="title">
                  <div style="display: flex; align-items: center">
                    <i
                      class="el-icon-data-line"
                      style="font-size: 24px; margin-right: 5px"
                    ></i
                    ><span style="font-family: LoraRegular; font-size: 18px"
                      >Shares</span
                    >
                  </div>
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
                  <div style="display: flex; align-items: center">
                    <i
                      class="el-icon-headset"
                      style="font-size: 24px; margin-right: 5px"
                    ></i
                    ><span style="font-family: LoraRegular; font-size: 18px"
                      >Music</span
                    >
                  </div>
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
              <img :src="item" alt="" style="width: 120px; height: 60px" />
            </li>
          </ul>
        </vue-seamless-scroll>
      </div>

      <footer class="footer">
        <div style="color: rgb(102, 108, 110)">Project from Group 3</div>
        <div style="color: #fff; display: flex">
          <div style="padding-right: 20px; border-right: #fff solid 1px">
            <el-link
              href="https://www.linkedin.com/in/abigail-gualda/"
              target="_blank"
              type="info"
              style="color: #fff; font-size: 16px"
              >Contact Us</el-link
            >
          </div>
          <div style="padding-left: 20px">
            <el-link
              href="https://github.com/stephenyang0215/NewsVerse/blob/main/README.md"
              target="_blank"
              type="info"
              style="color: #fff; font-size: 16px"
              >About us</el-link
            >
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import vueSeamlessScroll from "vue-seamless-scroll";

import BostonClock from "@/components/BostonClock.vue";
import WeatherDetail from "@/components/WeatherDetail.vue";
import MusicPlayer from "@/components/MusicPlayer.vue";

export default {
  components: {
    vueSeamlessScroll,
    BostonClock,
    WeatherDetail,
    MusicPlayer,
  },
  data() {
    return {
      categorier: [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
      ],
      leftShow: true,
      images: [
        require("@/assets/1.png"),
        require("@/assets/2.png"),
        require("@/assets/3.png"),
        require("@/assets/4.png"),
        require("@/assets/5.png"),
        require("@/assets/6.png"),
        require("@/assets/7.jpeg"),
        require("@/assets/8.png"),
        require("@/assets/9.png"),
        require("@/assets/10.png"),
        require("@/assets/11.png"),
        require("@/assets/12.png"),
        require("@/assets/13.jpeg"),
        require("@/assets/14.png"),
        require("@/assets/15.png"),
        require("@/assets/16.png"),
        require("@/assets/17.png"),
        require("@/assets/18.png"),
        require("@/assets/19.png"),
        require("@/assets/20.png"),
        require("@/assets/21.webp"),
        require("@/assets/22.png"),
        require("@/assets/23.png"),
        require("@/assets/24.jpeg"),
        require("@/assets/25.png"),
        require("@/assets/26.png"),
        require("@/assets/27.jpg"),
        require("@/assets/28.png"),
        require("@/assets/29.png"),
        require("@/assets/30.png"),
        require("@/assets/31.png"),
        require("@/assets/32.jpeg"),
        require("@/assets/33.png"),
        require("@/assets/34.jpeg"),
        require("@/assets/35.jpeg"),
        require("@/assets/36.png"),
        require("@/assets/37.png"),
        require("@/assets/38.png"),
        require("@/assets/39.png"),
        require("@/assets/40.jpeg"),
        require("@/assets/41.png"),
        require("@/assets/42.png"),
        require("@/assets/43.png"),
        // require("@/assets/44.png"),
        require("@/assets/45.png"),
        require("@/assets/46.png"),
        require("@/assets/47.png"),
        require("@/assets/48.jpeg"),
        require("@/assets/49.png"),
        require("@/assets/50.png"),
        require("@/assets/51.png"),
        require("@/assets/52.jpeg"),
        require("@/assets/53.png"),
        require("@/assets/54.png"),
        require("@/assets/55.png"),
        require("@/assets/56.png"),
        require("@/assets/57.png"),
        require("@/assets/58.jpeg"),
        require("@/assets/59.png"),
        require("@/assets/60.png"),
        require("@/assets/61.jpeg"),
        require("@/assets/62.png"),
        require("@/assets/63.png"),
        require("@/assets/64.png"),
        require("@/assets/65.png"),
        require("@/assets/66.png"),
        require("@/assets/67.png"),
        require("@/assets/68.png"),
        require("@/assets/69.png"),
        require("@/assets/70.png"),
      ],
      classOption: {
        limitMoveNum: 69,
        direction: 3,
        step: 0.5,
      },
      stockdio_events: true,
      filterWord: "",
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
    goHome() {
      if (this.$route.path !== "/") {
        this.$router.push("/");
      }
    },
    searchNews() {
      this.$router.push({
        path: "/about",
        query: {
          title: this.filterWord,
        },
      });
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
@font-face {
  font-family: "RobotoBlack";
  src: url("./assets/font/Roboto-Black.ttf");
}
@font-face {
  font-family: "LoraRegular";
  src: url("./assets/font/Lora-Regular.ttf");
}
.home {
  background-color: #0d1b2a !important;
}

::v-deep .el-collapse-item__arrow {
  color: #e54f6d; /* 替换为你想要的颜色 */
}

.widget-font {
  font-family: "RobotoBlack";
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
  height: 60px;
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
  height: 60px;
  margin-right: 10px;
  line-height: 60px;
  background-color: #999;
  color: #fff;
  text-align: center;
  font-size: 30px;
}
::v-deep .el-collapse-item .el-collapse-item__header {
  background-color: #e0e1dd !important;
  /* border: none; */
  height: 80px;
}
::v-deep .el-collapse-item__content {
  padding-bottom: 0px;
}
::v-deep .el-collapse-item__wrap {
  background-color: #e2bdc1;
  border: none;
  border-radius: 10px;
}
::v-deep .el-dialog {
  background-color: #e0e1dd;
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
::v-deep .el-dialog__body {
  padding: 30px 40px;
}
</style>
