## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 lua 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/main.lua 文件中的逻辑即可。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd lua/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/lua/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: luaEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/luaEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function luaEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/lua/event-demo $ s invoke -e "hello"
[2021-07-26T17:31:45.893] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
FC Initialize Start RequestId: df8dda55-f0df-4071-80d1-378efdef11bc, client: 21.0.3.254, server: , request: "POST /initialize HTTP/1.1", host: "21.0.3.2:9000"
2021/07/26 09:31:47 [notice] 8#8: *2 [lua] main.lua:16: init, client: 21.0.3.254, server: , request: "POST /initialize HTTP/1.1", host: "21.0.3.2:9000"
2021/07/26 09:31:47 [notice] 8#8: *2 [lua] main.lua:18: FC Initialize End RequestId: df8dda55-f0df-4071-80d1-378efdef11bc, client: 21.0.3.254, server: , request: "POST /initialize HTTP/1.1", host: "21.0.3.2:9000"
21.0.3.2 21.0.3.254 0.000 [26/Jul/2021:09:31:47 +0000] "POST /initialize HTTP/1.1" 200 11 "-" "Go-http-client/1.1" "-" df8dda55-f0df-4071-80d1-378efdef11bc
2021/07/26 09:31:47 [info] 8#8: epoll_wait() failed (4: Interrupted system call)
2021/07/26 09:31:47 [notice] 8#8: *3 [lua] main.lua:23: FC Invoke Start RequestId: df8dda55-f0df-4071-80d1-378efdef11bc, client: 21.0.3.254, server: , request: "POST /invoke HTTP/1.1", host: "21.0.3.2:9000"
2021/07/26 09:31:47 [notice] 8#8: *3 [lua] main.lua:26: hello, client: 21.0.3.254, server: , request: "POST /invoke HTTP/1.1", host: "21.0.3.2:9000"
2021/07/26 09:31:47 [notice] 8#8: *3 [lua] main.lua:28: FC Invoke End RequestId: df8dda55-f0df-4071-80d1-378efdef11bc, client: 21.0.3.254, server: , request: "POST /invoke HTTP/1.1", host: "21.0.3.2:9000"
21.0.3.2 21.0.3.254 0.000 [26/Jul/2021:09:31:47 +0000] "POST /invoke HTTP/1.1" 200 16 "-" "Go-http-client/1.1" "-" df8dda55-f0df-4071-80d1-378efdef11bc

Duration: 1.45 ms, Billed Duration: 2 ms, Memory Size: 1024 MB, Max Memory Used: 9.63 MB
========= FC invoke Logs end =========

FC Invoke Result:
hello



End of method: invoke
```
