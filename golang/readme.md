## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 golang 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/main.go 文件中的逻辑即可。

> 如果您想增加依赖新的 go lib, 修改 build-image 中的 Dockerfile, 增加新的 go get 即可， 或者您修改 Dockerfile， 使用 gomod 管理依赖。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd golang/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/golang/event-demo  make build
docker build -t fc-go-runtime  -f build-image/Dockerfile build-image
Sending build context to Docker daemon  2.048kB
Step 1/5 : FROM golang:1.12.16-stretch
 ---> 7ad03a8aece5
...
Step 5/5 : RUN go get github.com/awesome-fc/golang-runtime
 ---> Using cache
 ---> 74746b35f154
Successfully built 74746b35f154
Successfully tagged fc-go-runtime:latest
docker run --rm -it -v $(pwd):/tmp fc-go-runtime bash -c "go build -o /tmp/code//bootstrap /tmp/code/main.go"
chmod +x code/bootstrap
sam@iZj6c895xh98:~/fc-custom-demo/golang/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: goEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/goEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function goEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/golang/event-demo $ s invoke -e "hello"
[2021-07-26T17:16:14.812] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
FC Initialize Start RequestId: faf356b1-a686-40a4-a595-e88591700bc3
2021-07-26T09:16:16.607Z: faf356b1-a686-40a4-a595-e88591700bc3 [INFO]  init golang!
FC Initialize End RequestId: faf356b1-a686-40a4-a595-e88591700bc3
FC Invoke Start RequestId: faf356b1-a686-40a4-a595-e88591700bc3
2021-07-26T09:16:16.612Z: faf356b1-a686-40a4-a595-e88591700bc3 [INFO]  hello golang!
FC Invoke End RequestId: faf356b1-a686-40a4-a595-e88591700bc3

Duration: 1.03 ms, Billed Duration: 2 ms, Memory Size: 512 MB, Max Memory Used: 11.75 MB
========= FC invoke Logs end =========

FC Invoke Result:
hello


End of method: invoke
```
