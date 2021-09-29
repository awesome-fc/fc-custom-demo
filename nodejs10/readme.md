## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 nodejs10 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/server.js 文件中的逻辑即可。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd nodejs10/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/nodejs10/event-demo  s build -d

sam@iZj6c895xh98:~/fc-custom-demo/nodejs10/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: node10EventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/node10EventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function node10EventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/nodejs10/event-demo $ s invoke -e "hello"
[2021-07-26T17:34:12.610] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
...
Duration: 1.54 ms, Billed Duration: 2 ms, Memory Size: 1024 MB, Max Memory Used: 14.74 MB
========= FC invoke Logs end =========

FC Invoke Result:
OK


End of method: invoke
```
