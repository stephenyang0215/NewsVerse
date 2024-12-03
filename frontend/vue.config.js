const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api": {
        // 代理的标识符
        target: "https://60xoly3w79.execute-api.us-east-1.amazonaws.com", // 目标服务器
        changeOrigin: true, // 允许跨域
        pathRewrite: { "^/api": "" }, // 将 /api 替换为空，转发时去掉 /api
      },
    },
  },
});
