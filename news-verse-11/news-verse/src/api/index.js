import request from "@/utils/request";

export function getweatherAPI() {
  const API_KEY = "6857be6453cfd80ea1b1f25ea85f5068";
  const CITY = "Boston";
  const COUNTRY = "US";
  let data = {
    q: `${CITY},${COUNTRY}`,
    appid: API_KEY,
    units: "metric",
  };
  return request({
    url: `https://api.openweathermap.org/data/2.5/weather`,
    method: "get",
    params: data,
  });
}

export function getTimeAPI() {
  return request({
    url: `https://timeapi.io/api/Time/current/zone?timeZone=America/New_York`,
    method: "get",
  });
}
