# project_infrastructure_vue2_element_scss

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Console error: Buttons must have discernible text: Element has no title attribute
The problem cause by ...\cs601_DeweiWang_term_project\node_modules\element-ui\packages\carousel\src\main.vue
the package does not give title for button attribute. Build by this package may meet that problem. To fix it, please type "title" in this file by own.