## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 python3.7 编写事件函数和 http 函数示例, 您可以基于这个示例进行二次开发，只需要修改 code 目录下面的 server.py 文件中的函数逻辑即可。

### 事件函数

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd python37/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/python37/event-demo  s build -d
[2021-07-26T21:53:55.688] [INFO ] [S-CLI] - Start ...
[2021-07-26T21:53:57.371] [INFO ] [FC-BUILD] - Build artifact start...
[2021-07-26T21:53:57.373] [INFO ] [FC-BUILD] - Use docker for building.
[2021-07-26T21:53:57.488] [INFO ] [FC-BUILD] - Build function using image: registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17
[2021-07-26T21:53:59.499] [INFO ] [FC-BUILD] - skip pulling image registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17...
[2021-07-26T21:54:21.826] [INFO ] [FC-BUILD] - Build artifact successfully.

Tips for next step
======================
...
End of method: build
sam@iZj6c895xh98:~/fc-custom-demo/python37/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: pyEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/pyEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function pyEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/python37/event-demo $ s invoke -e "{}"
[2021-07-26T21:57:05.029] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
...
Duration: 2.61 ms, Billed Duration: 3 ms, Memory Size: 1536 MB, Max Memory Used: 71.50 MB
========= FC invoke Logs end =========

FC Invoke Result:
{}


End of method: invoke
```

### HTTP 函数

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd python37/http-demo
sam@iZj6c895xh98:~/fc-custom-demo/python37/http-demo  s build -d
[2021-07-26T21:59:14.901] [INFO ] [S-CLI] - Start ...
[2021-07-26T21:59:16.280] [INFO ] [FC-BUILD] - Build artifact start...
[2021-07-26T21:59:16.282] [INFO ] [FC-BUILD] - Use docker for building.
[2021-07-26T21:59:16.462] [INFO ] [FC-BUILD] - Build function using image: registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17
[2021-07-26T21:59:17.692] [INFO ] [FC-BUILD] - skip pulling image registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.17...
[2021-07-26T21:59:40.796] [INFO ] [FC-BUILD] - Build artifact successfully.

Tips for next step
======================
...
End of method: build
sam@iZj6c895xh98:~/fc-custom-demo/python37/http-demo  s deploy -y
...
[2021-07-26T22:00:10.973] [INFO ] [FC-DEPLOY] - Generated auto custom domain: pyHttpFunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T22:00:10.973] [INFO ] [FC-DEPLOY] - Creating custom domain: pyHttpFunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T22:00:11.923] [INFO ] [FC-DOMAIN] - Creating custom domain: pyHttpFunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net

Tips for next step
======================
...

fc-python37-demo:
  region: cn-hangzhou
  service:
    name: custom-demo
  function:
    name: pyHttpFunc
    runtime: custom
    handler: index.handler
    memorySize: 1536
    timeout: 30
  url:
    system_url: >-
      https://1986114430573743.cn-hangzhou.fc.aliyuncs.com/2016-08-15/proxy/custom-demo/pyHttpFunc/
    custom_domain:
      - domain: >-
          http://pyHttpFunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
  triggers:
    - type: http
      name: http_t
sam@iZj6c895xh98:~/fc-custom-demo/python37/http-demo  curl  http://pyHttpFunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
Hello World!
```
