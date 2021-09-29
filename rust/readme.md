## 简介

### 安装和配置最新版本的 Serverless-Devs

#### 安装

[安装教程](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Install-tutorial.md)

#### 配置

[Setting-up-credentials](https://github.com/devsapp/fc/blob/main/docs/Getting-started/Setting-up-credentials.md)

这里展示了 powershell 编写事件函数示例, 您可以基于这个示例进行二次开发，只需要修改 code/SimpleHttpServer.ps1 文件中的逻辑即可。

#### Deploy Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd rust/event-demo/
sam@iZj6c895xh98:~/fc-custom-demo/rust/event-demo  make build
...
docker run --rm -it -v $(pwd):/opt/rust-demo fc-rust-env bash -c "cd /opt/rust-demo/bootstrap && cargo build"
    Updating `https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git` index
...
mkdir -p pkg
cp bootstrap/target/debug/bootstrap pkg/
sam@iZj6c895xh98:~/fc-custom-demo/rust/event-demo  s deploy -y
[2021-07-26T16:52:38.564] [INFO ] [S-CLI] - Start ...
[2021-07-26T16:52:40.699] [INFO ] [FC-DEPLOY] - Using region: cn-hangzhou
...
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating service: custom-demo
[2021-07-26T16:52:42.618] [INFO ] [FC-DEPLOY] - Creating function: rustEventFunc
✔ Make service custom-demo success.
✔ Make function custom-demo/rustEventFunc success.
[2021-07-26T16:52:43.792] [INFO ] [FC-DEPLOY] - Checking Service custom-demo exists
[2021-07-26T16:52:43.848] [INFO ] [FC-DEPLOY] - Checking Function rustEventFunc exists

Tips for next step
======================
....
```

#### Invoke Function

```bash
sam@iZj6c895xh98:~/fc-custom-demo/rust/event-demo $ s invoke -e "hello"
[2021-07-26T17:54:36.697] [INFO ] [S-CLI] - Start ...
========= FC invoke Logs begin =========
FC Invoke End RequestId: 7244b31e-c3ba-424f-9103-2f8841ebfcc1
Duration: 3.13 ms, Billed Duration: 4 ms, Memory Size: 512 MB, Max Memory Used: 7.19 MB
========= FC invoke Logs end =========

FC Invoke Result:
Rust demo function invoked.


End of method: invoke
```

### Deep Dive

**Q: What's the genral procedure?**

A: To implement a custom runtime, the key component is a file named `bootstrap`, a binary or an executable script. It should start an HTTP server that listens on port `9000` and serve the HTTP requests on the following paths.

- `/invoke`: The handler for event trigger.
- `/http-invoke`: The handler for HTTP trigger.
- `/initialize`: The handler of initialization.

Behind the curtain, the FC (Function Compute) system will execute the `bootstrap`, connect to it through port 9000, and relay the request to it via HTTP.

**Q: What is `Dockerfile.build` for?**

A: It is noteworthy that the `bootstrap` will be executed in [a specific environment](https://github.com/aliyun/fc-docker/blob/master/custom/build/Dockerfile) ([more details](https://help.aliyun.com/document_detail/132044.html#h2-u6267u884Cu73AFu58833) in the doc), so we have to build the binary in the same environment. Hence we define the `Dockerfile.build` based on it and later compile the Rust code inside.

**Q: What will be uploaded?**

A: `make build` will create a directory named `pkg` and place the newly-created `bootstrap` into it. Then the `fun` CLI will automatically package `pkg` and deploy it onto FC.

**Q: Usage outside China?**

A: Currently, `Dockerfile.build` heavily relies on Chinese mirror for speeding up the installation. Specifically, Line 9-16 are the mirrors for Debian APT sources and Line 24-25 for installing Rust. Similarly, the `bootstrap/.cargo/config.toml` has also set a mirror source. Replace them with your local mirrors if you are residing outside China.
