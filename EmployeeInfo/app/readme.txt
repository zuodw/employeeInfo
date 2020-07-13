0. cnpm安装
    npm install -g cnpm --registry=https://registry.npm.taobao.org

    npm install webpack-dev-server -g

1. vue project创建：
    1. npm install -g vue-cli
    2. web文件夹下 vue init webpack employee-info-web
    3. cd employee-info-web
    4. npm run dev

2. 安装ElementUI依赖
    cnpm install element-ui --save
    cnpm install element-theme -g (使用全局安装，后面使用少坑)
    cnpm install element-theme-chalk -D
    cnpm install file-loader --save

    项目中：main.js中
    import ElementUI from 'element-ui'
    import 'element-ui/lib/theme-chalk/index.css'

3. 安装axios支持
    cnpm install axios
    npm install --save axios vue-axios

    项目index.js中
    import axios from 'axios'
    Vue.prototype.$axios = axios

    Vue组件中使用的时候： Vue.$axios

4.  打包项目路径修改：
    web/employee-info-web/config/index.js修改以下：
    index: path.resolve
    assetsRoot: path.resolve

5.  打包
    npm run build