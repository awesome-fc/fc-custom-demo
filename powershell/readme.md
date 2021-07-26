## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 powershell 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/SimpleHttpServer.ps1 文件中的逻辑即可。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd powershell/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/powershell/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: powershellEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/powershellEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function powershellEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/powershell/event-demo $ s invoke -e "hello"
[2021-07-26T17:38:10.375] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: 000a2ae1-8cb1-4400-885c-a8b125c123ae
hello
FC Invoke End RequestId: 000a2ae1-8cb1-4400-885c-a8b125c123ae

Duration: 41.49 ms, Billed Duration: 42 ms, Memory Size: 512 MB, Max Memory Used: 93.91 MB
========= FC invoke Logs end =========

FC Invoke Result:
hello


End of method: invoke
```
