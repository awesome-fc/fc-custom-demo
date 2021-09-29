## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 c++ 编写事件函数和 http 函数示例, 您可以基于这个示例进行二次开发，只需要修改 sample/src/handlers 下面的 cpp 文件中的函数逻辑即可。

### 事件函数

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd cpp/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/cpp/event-demo  make build
docker build -t fc-cpp-runtime  -f build-image/Dockerfile build-image
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM aliyunfc/runtime-custom:base
 ---> 2be79dda5969
Step 2/3 : RUN apt-get update
 ---> Using cache
 ---> ca99ebf882ca
Step 3/3 : RUN apt-get install -y cmake
 ---> Using cache
 ---> e9b28b6d7374
Successfully built e9b28b6d7374
Successfully tagged fc-cpp-runtime:latest
docker run --rm -it -v $(pwd):/tmp fc-cpp-runtime bash -c "cd /tmp && ./build.sh"
...
-- Configuring done
-- Generating done
-- Build files have been written to: /tmp/sample/release
Scanning dependencies of target bootstrap
[ 33%] Building CXX object CMakeFiles/bootstrap.dir/src/register_handler.cpp.o
[ 66%] Building CXX object CMakeFiles/bootstrap.dir/src/handlers/event_handler.cpp.o
[100%] Linking CXX executable /tmp/bin/bootstrap
[100%] Built target bootstrap
sam@iZj6c895xh98:~/fc-custom-demo/cpp/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: cppEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/cppEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function cppEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/cpp/event-demo $ s invoke -e "hellocpp"
[2021-07-26T16:48:59.701] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
/invoke is called.
FC Invoke Start RequestId: e51175b5-c9ef-4476-a4b2-ab792612459d
2021-07-26T08:49:00 e51175b5-c9ef-4476-a4b2-ab792612459d [INFO] handling invoke
FC Invoke End RequestId: e51175b5-c9ef-4476-a4b2-ab792612459d

Duration: 0.79 ms, Billed Duration: 1 ms, Memory Size: 512 MB, Max Memory Used: 2.04 MB
========= FC invoke Logs end =========

FC Invoke Result:
hellocpp


End of method: invoke
```

### HTTP 函数

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd cpp/http-demo/
sam@iZj6c895xh98:~/fc-custom-demo/cpp/http-demo  make build
...
sam@iZj6c895xh98:~/fc-custom-demo/cpp/http-demo  s deploy -y
[2021-07-26T16:58:23.779] [INFO ] [FC-DEPLOY] - Using customDomain: auto: fc will try to generate related custom domain resources automatically
...
[2021-07-26T16:58:27.450] [INFO ] [FC-DEPLOY] - Generated auto custom domain: cpphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T16:58:27.450] [INFO ] [FC-DEPLOY] - Creating custom domain: cpphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
[2021-07-26T16:58:30.038] [INFO ] [FC-DOMAIN] - Creating custom domain: cpphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
...
fc-cpp_http_demo-fc_cpp_http:
  region: cn-hangzhou
  service:
    name: custom-demo
  function:
    name: cppHttpFunc
    runtime: custom
    handler: http.handler
    memorySize: 512
    timeout: 3
  url:
    system_url: >-
      https://1986114430573743.cn-hangzhou.fc.aliyuncs.com/2016-08-15/proxy/custom-demo/cppHttpFunc/
    custom_domain:
      - domain: >-
          http://cpphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net
  triggers:
    - type: http
      name: http_t
sam@iZj6c895xh98:~/fc-custom-demo/cpp/http-demo  curl  http://cpphttpfunc.custom-demo.1986114430573743.cn-hangzhou.fc.devsapp.net -d "hellocpp"
hellocpp
```
