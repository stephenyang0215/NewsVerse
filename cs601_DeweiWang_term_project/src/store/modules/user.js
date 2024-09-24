const state = {
  userInfo: JSON.parse(localStorage.getItem('userInfo')) || null
}

const mutations = {
  SET_USER_INFO: (state, userInfo) => {
    state.userInfo = userInfo
    localStorage.setItem('userInfo', JSON.stringify(userInfo))
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
