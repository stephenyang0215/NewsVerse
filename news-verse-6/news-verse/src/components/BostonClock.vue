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
      seconds: 0,
      minutes: 0,
      hours: 0,
      timer: null,
      currentDate: new Date(),
      timeLoading: false,
    };
  },
  computed: {
    formattedDate() {
      const options = { year: "numeric", month: "long", weekday: "long" };
      return this.currentDate.toLocaleDateString("en-US", options);
    },
    formattedTime() {
      const paddedMinutes = String(this.minutes).padStart(2, "0");
      const paddedSeconds = String(this.seconds).padStart(2, "0");
      return `${this.hours}:${paddedMinutes}:${paddedSeconds}`;
    },
  },
  methods: {
    async getTimeData() {
      this.timeLoading = true;
      try {
        const res = await getTimeAPI();
        const localTime = new Date(res.dateTime);
        this.hours = localTime.getHours();
        this.minutes = localTime.getMinutes();
        this.seconds = localTime.getSeconds();
        this.currentDate = localTime;
        this.timeLoading = false;
      } catch (error) {
        console.error(error);
      }
    },
    startTimer() {
      this.timer = setInterval(() => {
        this.seconds += 1;

        if (this.seconds >= 60) {
          this.seconds = 0;
          this.minutes += 1;
        }

        if (this.minutes >= 60) {
          this.minutes = 0;
          this.hours += 1;
        }
      }, 1000);
    },
  },
  mounted() {
    this.getTimeData();
    this.startTimer();
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
  background-color: #b7e4c7;
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
