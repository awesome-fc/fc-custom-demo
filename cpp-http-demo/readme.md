## 编译

- 第一次, 生成 C ++ 编译环境 image

```bash
$ docker build -t fc-cpp-centos-dev -f build-image/Dockerfile build-image
```

- 开发修改代码，对于 http 函数来说， 只需要修改 EchoHttpHandler::OnInvoke 里面的逻辑，体验可以先不用动这里的代码

```
void EchoHttpHandler::OnInvoke(const FcContext& context, const Pistache::Http::Request& req,
            Pistache::Http::ResponseWriter& response)
{
    response.send(Http::Code::Ok, EchoHttpHandler::mInitHandler + req.body());
}
```

- 编译代码

```bash
$ docker run  -it -v $(pwd):/tmp fc-cpp-centos-dev bash
$ scl enable devtoolset-7 bash
$ cd /tmp && ./build.sh
```

此时编译好的可执行文件都在 bin 目录下面了

## 生成 FC 需要的镜像

```bash
$ cd bin
$ docker build -t registry.cn-hangzhou.aliyuncs.com/fc-demo/test-cpp:v1 -f Dockerfile .
```
