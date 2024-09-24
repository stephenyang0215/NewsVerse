/* eslint-disable quotes */
/* eslint-disable space-before-function-paren */
// vue.config.js

module.exports = {
  lintOnSave: 'warning', // 设置为 true 或 'warning' 时，eslint-loader 会将 lint 错误输出为编译警告。默认情况下，警告仅仅会被输出到命令行，且不会使得编译失败

  // 基于 webpack-chain 的 ChainableConfig 实例。允许对内部的 webpack 配置进行更细致的修改
  chainWebpack: (config) => {
    // 配置全局 scss 引用
    const oneOfsMap = config.module.rule('scss').oneOfs.store
    oneOfsMap.forEach((item) => {
      item
        .use('sass-resources-loader')
        .loader('sass-resources-loader')
        .options({
          // 全局变量文件路径，只有一个时可将数组省去
          resources: ['./src/styles/golbal-scss-var.scss']
        })
        .end()
    })
  },
  // 配置全局 scss 引用
  css: {
    loaderOptions: {
      // 给 sass-loader 传递选项
      sass: {
        // @/ 是 src/ 的别名
        // 所以这里假设你有 `src/assets/chenGolbal/chenGolbalcss.scss` 这个文件
        // 注意：在 sass-loader v7 中，这个选项名是 "data"
        prependData: `@import "~@/styles/golbal-scss-var.scss"`
      },
      // 默认情况下 `sass` 选项会同时对 `sass` 和 `scss` 语法同时生效
      // 因为 `scss` 语法在内部也是由 sass-loader 处理的
      // 但是在配置 `data` 选项的时候
      // `scss` 语法会要求语句结尾必须有分号，`sass` 则要求必须没有分号
      // 在这种情况下，我们可以使用 `scss` 选项，对 `scss` 语法进行单独配置
      scss: {
        prependData: `@import "~@/styles/golbal-scss-var.scss";`
      }
    }
  }
}
