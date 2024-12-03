<template>
  <div>
    <div v-if="weatherLoading">loading...</div>
    <div v-else class="weatherContent">
      <div class="weatherCity">{{ weatherData.name }}</div>
      <div class="weatherDetails">
        <img
          :src="iconUrl"
          alt="Weather icon"
          width="80px"
          height="80px"
          v-if="iconUrl"
        />
        <p>{{ temperature }}°C</p>
        <div class="tempRange">
          <span>{{ tempMax }}°C</span>
          <span>{{ tempMin }}°C</span>
        </div>
      </div>
      <div class="tempDescription">
        <div>{{ description }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { getweatherAPI } from "@/api/index";

export default {
  name: "WeatherDetail",
  data() {
    return {
      weatherData: {},
      temperature: null,
      description: "",
      iconUrl: "",
      tempMax: "",
      tempMin: "",
      weatherLoading: false,
    };
  },
  computed: {},
  methods: {
    async getweatherData() {
      this.weatherLoading = true;
      try {
        const res = await getweatherAPI();
        this.weatherData = res;
        const iconCode = res.weather[0].icon;
        this.temperature = res.main.temp;
        this.description = res.weather[0].description;
        this.iconUrl = `http://openweathermap.org/img/wn/${iconCode}@2x.png`;
        this.tempMax = res.main.temp_max;
        this.tempMin = res.main.temp_min;
        this.weatherLoading = false;
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.getweatherData();
  },
};
</script>

<style scoped>
.weatherContent {
  display: flex;
  flex-direction: column;
  padding: 20px;
}
.weatherCity {
  color: rgb(0, 27, 160);
  border-bottom: 1px solid rgb(0, 27, 160);
}
.weatherDetails {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.weatherDetails p {
  font-size: 16px;
}
.tempRange {
  display: flex;
  flex-direction: column;
}
.tempDescription {
  display: flex;
  font-size: 16px;
  font-weight: 700;
  padding: 0 0 0 20px;
}
</style>
