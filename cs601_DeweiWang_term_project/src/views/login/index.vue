<template>
  <div class="login-container">
    <el-divider> <h3 class="title">· Log in ·</h3></el-divider>
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" autocomplete="on" label-position="left">
      <el-form-item prop="userName">
        <el-input
          v-model.trim="loginForm.userName"
          prefix-icon="el-icon-user"
          placeholder="Input User Name"
          name="User Name"
          type="text"
          tabindex="1"
          autocomplete="on"
          ref="userName"
          clearable
        />
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="Caps Lock" placement="right" manual>
        <el-form-item prop="password">
          <el-input
            ref="password"
            v-model.trim="loginForm.password"
            name="password"
            type="password"
            show-password
            placeholder="Password"
            prefix-icon="el-icon-lock"
            tabindex="2"
            autocomplete="on"
            clearable
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleLogin"
          ></el-input>
        </el-form-item>
      </el-tooltip>

      <el-button type="primary" style="width: 100%; margin-bottom: 30px" title="button" @click.native.prevent="handleLogin">Log in</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      loginForm: {
        userName: '',
        password: ''
      },
      loginRules: {
        userName: [{ required: true, trigger: 'blur', message: 'Required' }],
        password: [{ required: true, trigger: 'blur', message: 'Required' }]
      },
      capsTooltip: false
    }
  },

  mounted() {
    if (this.loginForm.userName === '') {
      this.$refs.userName.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },

  methods: {
    // when caps lock
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && key >= 'A' && key <= 'Z'
    },

    // log in
    handleLogin() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.$store.commit('user/SET_USER_INFO', { userName: this.loginForm.userName })
          const { originPath } = this.$route.query
          if (originPath) {
            this.$router.push({
              path: originPath
            })
          } else {
            this.$router.push('/plate')
          }
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/components/login.scss';
</style>
