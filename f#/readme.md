## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 f# 编写 HTTP 函数示例, 您可以基于这个示例进行二次开发, 修改 FSharpDemo 中对应的 controller 即可。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd f#/http-demo/
sam@iZj6c895xh98:~/fc-custom-demo/f#/http-demo  make build
docker run --rm -it -v $(pwd):/tmp mcr.microsoft.com/dotnet/core/sdk:3.1 bash -c "cd /tmp/FSharpDemo && dotnet publish -r linux-x64 -c Release --self-contained true && cd /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/publish && mv FSharpDemo bootstrap && chmod +x bootstrap"
Microsoft (R) Build Engine version 16.7.2+b60ddb6f4 for .NET
Copyright (C) Microsoft Corporation. All rights reserved.

  Determining projects to restore...
  Restored /tmp/FSharpDemo/FSharpDemo.fsproj (in 19.53 sec).
  FSharpDemo -> /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/FSharpDemo.dll
  FSharpDemo -> /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/publish/
sam@iZj6c895xh98:~/fc-custom-demo/f#/http-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T17:08:56.021] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T17:08:56.125] [INFO ] [FC-DEPLOY] - Service: custom-demo already exists online.
[2021-07-26T17:08:56.225] [INFO ] [FC-DEPLOY] - Checking Function fsharpHttpFunc exists
[2021-07-26T17:08:56.263] [INFO ] [FC-DEPLOY] - Function: fsharpHttpFunc already exists online.
[2021-07-26T17:08:56.370] [INFO ] [FC-DEPLOY] - Checking Trigger http_t exists
[2021-07-26T17:08:56.430] [INFO ] [FC-DEPLOY] - Trigger: http_t already exists online.
📎 Using fc deploy type: sdk, If you want to deploy with pulumi, you can [s cli fc-default set deploy-type pulumi] to switch.
[2021-07-26T17:09:02.642] [INFO ] [FC-DEPLOY] - Checking Trigger http_t exists
[2021-07-26T17:09:02.696] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T17:09:02.696] [INFO ] [FC-DEPLOY] - Creating function: fsharpHttpFunc
[2021-07-26T17:09:02.696] [INFO ] [FC-DEPLOY] - Creating triggers: ["http_t"]
✔ Make service custom-demo success.
✔ Make function custom-demo/fsharpHttpFunc success.
✔ Make trigger custom-demo/fsharpHttpFunc/http_t success.
[2021-07-26T17:09:40.970] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T17:09:41.174] [INFO ] [FC-DEPLOY] - Checking Function fsharpHttpFunc exists
[2021-07-26T17:09:41.289] [INFO ] [FC-DEPLOY] - Checking Trigger http_t exists
[2021-07-26T17:09:41.359] [INFO ] [FC-DEPLOY] - Generated auto custom domain: fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T17:09:41.359] [INFO ] [FC-DEPLOY] - Creating custom domain: fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T17:09:42.190] [INFO ] [FC-DOMAIN] - Creating custom domain: fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net

Tips for next step
======================
....

fc-fsharp_demo-fc_fsharp:
  region: cn-hangzhou
  service:
    name: custom-demo
  function:
    name: fsharpHttpFunc
    runtime: custom
    handler: Program.main
    memorySize: 1024
    timeout: 3
  url:
    system_url: >-
      https://1986114430573743.cn-hangzhou.fc.aliyuncs.com/2016-08-15/proxy/custom-demo/fsharpHttpFunc/
    custom_domain:
      - domain: >-
          http://fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
  triggers:
    - type: http
      name: http_t
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/f#/http-demo $ curl http://fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
["hello","world"]
sam@iZj6c895xh98:~/fc-custom-demo/f#/http-demo $ curl http://fsharphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net/weatherforecast
[{"date":"2021-07-26T09:11:21.4051189+00:00","temperatureC":-8,"summary":"Cool","temperatureF":18},{"date":"2021-07-27T09:11:21.4226025+00:00","temperatureC":-17,"summary":"Freezing","temperatureF":2},{"date":"2021-07-28T09:11:21.4226134+00:00","temperatureC":-13,"summary":"Warm","temperatureF":9},{"date":"2021-07-29T09:11:21.4226141+00:00","temperatureC":29,"summary":"Cool","temperatureF":84},{"date":"2021-07-30T09:11:21.4226145+00:00","temperatureC":14,"summary":"Chilly","temperatureF":57}]
```
