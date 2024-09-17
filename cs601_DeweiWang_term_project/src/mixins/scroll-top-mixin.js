export default {
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      vm.$nextTick(() => {
        const scrollTop = to.meta.scrollTop
        document.documentElement.scrollTo(0, scrollTop)
      })
    })
  },

  beforeRouteLeave(to, from, next) {
    const scrollTop = document.documentElement.scrollTop
    from.meta.scrollTop = scrollTop
    next()
  }
}
