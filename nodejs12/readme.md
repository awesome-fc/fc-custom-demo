## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 nodejs12 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/server.js 文件中的逻辑即可。

nodejs14 同理， 就是先将 node 二进制下载下来， 打包到代码包中， 同时将 node 所在的 bin 目录加载到环境变量 PATH 中， 见 s.yaml 中的：

```
PATH: /code/node-v12.13.0-linux-x64/bin:$PATH
```

### 1. 下载二进制的 nodejs

```
sam@iZj6c895xh98:~/fc-custom-demo cd node12-demo/code
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo/code wget http://nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo/code tar -xvf  node-v12.13.0-linux-x64.tar.xz
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo/code rm node-v12.13.0-linux-x64.tar.xz
```

### 2. 在 s.yaml 文件中设置环境变量 PATH

```
'PATH': '/code/node-v12.13.0-linux-x64/bin:$PATH'
```

### 3. 部署函数

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd nodejs12/event-demo
sam@iZj6c895xh98:~/fc-custom-demo/nodejs12/event-demo  s build -d
[2021-07-26T18:04:02.932] [INFO ] [S-CLI] - Start ...
[2021-07-26T18:04:04.540] [INFO ] [FC-BUILD] - Build artifact start...
[2021-07-26T18:04:04.542] [INFO ] [FC-BUILD] - Use docker for building.
[2021-07-26T18:04:04.552] [INFO ] [FC-BUILD] - Build function using image: registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17
[2021-07-26T18:04:05.771] [INFO ] [FC-BUILD] - skip pulling image registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17...
[2021-07-26T18:04:42.684] [INFO ] [FC-BUILD] - Build artifact successfully.

Tips for next step
======================
...
End of method: build
sam@iZj6c895xh98:~/fc-custom-demo/nodejs12/event-demo  s deploy -y
...
[2021-07-26T18:05:14.342] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T18:05:14.343] [INFO ] [FC-DEPLOY] - Creating function: node12EventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/node12EventFunc success.
[2021-07-26T18:05:35.138] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T18:05:35.361] [INFO ] [FC-DEPLOY] - Checking Function node12EventFunc exists
...
```

### 4. 调用函数

```bash
sam@iZj6c895xh98:~/fc-custom-demo/nodejs12/event-demo  s invoke -e "hello"
[2021-07-26T18:06:23.272] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
...
Duration: 3.12 ms, Billed Duration: 4 ms, Memory Size: 1024 MB, Max Memory Used: 55.65 MB
========= FC invoke Logs end =========

FC Invoke Result:
OK


End of method: invoke
```
