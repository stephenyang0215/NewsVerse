<template>
  <div class="time-container">
    <div v-if="timeLoading">loading...</div>
    <div v-else class="date-info">
      <div class="weatherCity">Boston</div>
      <h2>{{ formattedDate }}</h2>
      <h3>{{ formattedTime }}</h3>
    </div>
  </div>
</template>

<script>
import { getTimeAPI } from "@/api/index";

export default {
  data() {
    return {
      currentDate: new Date(),
      timeLoading: false,
      timer: null,
    };
  },
  computed: {
    formattedDate() {
      const options = { year: "numeric", month: "long", weekday: "long" };
      return this.currentDate.toLocaleDateString("en-US", options);
    },
    formattedTime() {
      const hours = this.currentDate.getHours();
      const minutes = String(this.currentDate.getMinutes()).padStart(2, "0");
      const seconds = String(this.currentDate.getSeconds()).padStart(2, "0");
      return `${hours}:${minutes}:${seconds}`;
    },
  },
  methods: {
    async getTimeData() {
      this.timeLoading = true;
      try {
        const res = await getTimeAPI();
        this.currentDate = new Date(res.dateTime);
        this.timeLoading = false;

        // 确保定时器从精确时间点开始
        this.startTimer();
      } catch (error) {
        console.error(error);
      }
    },
    startTimer() {
      // 每秒更新当前时间
      this.timer = setInterval(() => {
        this.currentDate = new Date(this.currentDate.getTime() + 1000);
      }, 1000);
    },
    syncWithSystemTime() {
      // 定期用系统时间校正以避免长时间运行误差
      this.getTimeData();
    },
  },
  mounted() {
    this.getTimeData();

    // 每隔10分钟重新同步时间
    setInterval(() => {
      this.syncWithSystemTime();
    }, 10 * 60 * 1000);
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
};
</script>

<style scoped>
.time-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Arial", sans-serif;
  background-color: #e2bdc1;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.date-info {
  text-align: center;
}

.weatherCity {
  color: rgb(0, 27, 160);
  border-bottom: 1px solid rgb(0, 27, 160);
}

h2 {
  margin: 0;
  font-size: 24px;
  color: #333;
}

h3 {
  margin: 0;
  font-size: 20px;
  color: #666;
}
</style>
