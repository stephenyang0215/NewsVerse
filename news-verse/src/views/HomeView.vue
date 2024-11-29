<template>
  <div class="home">
    <el-container>
      <el-container>
        <el-header>
          <img
            :src="data.articles.L[0].M.urlToImage.S"
            alt=""
            width="50px"
            height="50px"
            style="float: left"
          />
        </el-header>
        <el-main>
          <div style="width: 400px">
            <div style="font-size: 64px">News Verse</div>
          </div>
          <el-card style="margin: 20px">
            <div style="width: 300px">
              <span style="font-size: 32px">tops news stories</span>
            </div>
            <div
              class="scroll_conainer"
              @mousedown="startDrag"
              @mousemove="onDrag"
              @mouseup="stopDrag"
              @mouseleave="stopDrag"
              ref="imgContent"
            >
              <div class="imgConent">
                <el-popover
                  v-for="(item, i) in data.articles.L"
                  :key="i"
                  placement="top-start"
                  width="200"
                  trigger="hover"
                  :content="item.M.title.S"
                >
                  <div
                    slot="reference"
                    style="
                      display: flex;
                      justify-content: center;
                      align-items: center;
                      margin-right: 80px;
                    "
                  >
                    <div
                      class="imgContainer"
                      :style="{
                        backgroundImage: 'url(' + item.M.urlToImage.S + ')',
                      }"
                    >
                      <div
                        style="
                          color: red;
                          font-size: 48px;
                          width: 250px;
                          height: 250px;
                          display: flex;
                          justify-content: center;
                          align-items: center;
                          position: relative;
                        "
                      >
                        <div>{{ i + 1 }}</div>
                      </div>
                    </div>
                    <div
                      v-if="!isDown[i]"
                      @click="downClick(i)"
                      style="cursor: pointer"
                    >
                      <i class="el-icon-arrow-down"></i>
                    </div>
                    <div
                      v-if="isDown[i]"
                      @click="downClick(i)"
                      style="cursor: pointer"
                    >
                      <i class="el-icon-arrow-up"></i>
                    </div>
                    <div v-if="isDown[i]" style="width: 390px">
                      <el-descriptions :title="item.M.title.S">
                        <el-descriptions-item label="description">{{
                          item.M.description.S
                        }}</el-descriptions-item>
                      </el-descriptions>
                    </div>
                  </div>
                </el-popover>
              </div>
            </div>
          </el-card>
          <el-card style="margin: 20px">
            <div class="categorier">
              <div class="categorier_title">Categorier</div>
              <el-row :gutter="5">
                <el-col :span="6">
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
                <el-col :span="6">
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
                <el-col :span="6">
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
                <el-col :span="6">
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
                <el-col :span="6">
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
                <el-col :span="6">
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
                <el-col :span="6">
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
      <div v-if="leftShow" @click="isLeftShow" style="margin: 10px">
        <i class="el-icon-arrow-right"></i>
      </div>
      <div v-if="!leftShow" @click="isLeftShow" style="margin: 10px">
        <i class="el-icon-arrow-left"></i>
      </div>
      <el-aside v-if="leftShow">aside</el-aside>
    </el-container>
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
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

const data = require("../assets/data.json");
export default {
  name: "HomeView",
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
    };
  },
  components: {},
  created() {
    console.log(this.data);
  },
  methods: {
    downClick(i) {
      console.log("click");
      this.$set(this.isDown, i, !this.isDown[i]);
    },
    startDrag(event) {
      this.isDragging = true;
      this.startX = event.clientX || event.touches[0].clientX; // 获取初始鼠标位置
      this.scrollLeft = this.$refs.imgContent.scrollLeft; // 获取当前滚动位置
    },
    onDrag(event) {
      if (!this.isDragging) return;
      event.preventDefault(); // 防止文本被选中
      const x = event.clientX || event.touches[0].clientX; // 获取当前鼠标位置
      const walk = (x - this.startX) * 1; // 计算拖动距离，这个数字可以调整以改变化滚动速度
      this.$refs.imgContent.scrollLeft = this.scrollLeft - walk; // 更新滚动位置
    },
    stopDrag() {
      this.isDragging = false; // 停止拖拽
    },
    isLeftShow() {
      console.log("1111");
      this.leftShow = !this.leftShow;
    },
  },
};
</script>

<style>
.el-aside {
  background-color: #d3dce6;
  color: #333;
}

.el-main {
  color: #333;
  padding: 5px;
}
.imgContainer {
  width: 250px;
  height: 250px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
  margin-right: 10px;
}
.imgConent {
  display: flex;
  flex-direction: row;
  margin: 10px 0 20px 34px;
  width: 2860px;
}
.categorier {
  margin: 10px 0 20px 34px;
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
</style>
