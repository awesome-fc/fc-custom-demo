## Introduction

#### Install and configure the latest version of funcraft
The following examples use the Fun tool for debugging and deploying functions. First install and configure the latest version of funcraft

``` bash
npm install @alicloud/fun -g
```
> You need to install nodejs 8.x or above

Before using, we need to configure first, by typing fun config, and then configure the Account ID, Access Key ID, Secret Access Key, and Default Region Name in turn according to the prompt:

![](https://img.alicdn.com/tfs/TB1qp7Oy7Y2gK0jSZFgXXc5OFXa-622-140.png)

#### Cloning sample project

``` bash
git clone https://github.com/awesome-fc/fc-custom-demo
```

> If you don't have git installed, you can type [https://github.com/awesome-fc/fc-custom-demo](https://github.com/awesome-fc/fc-custom-demo) into your browser and then click the download button to download directly.

#### Index

- [GO](#go)
- [Ruby](#ruby)
- [Powershell](#powershell)
- [F#](#FSharp)
- [TypeScript](#ts)
- [PHP74-Swoole](#php74)
- [Python37](#python37)

<a name="go"></a>
## GO

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd go-demo
rsong@iZj6c895xh98:~/fc-custom-demo/go-demo  make deploy
docker build -t fc-go-runtime  -f build-image/Dockerfile build-image
Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM golang:1.12.16-stretch
 ---> 7ad03a8aece5
...
Step 5/5 : RUN go get github.com/awesome-fc/golang-runtime
 ---> Using cache
 ---> 262e7f38ac05
Successfully built 262e7f38ac05
Successfully tagged fc-go-runtime:latest
docker run -it -v $(pwd):/tmp fc-go-runtime bash -c "go build -o /tmp/code//bootstrap /tmp/code/main.go"
chmod +x code/bootstrap
fun deploy -y
using template: template.yml
···
Waiting for service go_demo to be deployed...
        Waiting for function fc_go to be deployed...
                Waiting for packaging function fc_go code...
                The function fc_go has been packaged. A total of 1 file were compressed and the final size was 3.76 MB
        function fc_go deploy success
service go_demo deploy success
```

#### Invoke Function
``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/go-demo  fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: 4c1451b2-f29b-4554-87e5-126f3bc11fcf
2020-04-07T02:53:01.981Z: 4c1451b2-f29b-4554-87e5-126f3bc11fcf [INFO]  hello golang!
FC Invoke End RequestId: 4c1451b2-f29b-4554-87e5-126f3bc11fcf

Duration: 1.03 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 4.39 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```

<a name="ruby"></a>
## Ruby

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd ruby-demo
rsong@iZj6c895xh98:~/fc-custom-demo/ruby-demo  fun deploy -y
...
Waiting for service ruby-demo to be deployed...
        Waiting for function fc-ruby to be deployed...
                Waiting for packaging function fc-ruby code...
                The function fc-ruby has been packaged. A total of 4 files were compressed and the final size was 1.45 KB
        function fc-ruby deploy success
service ruby-demo deploy success
```

#### Invoke Function
``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/ruby-demo  fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: a9c4dc8a-4b5b-48e0-9a3f-70310531ae61
Hello World
FC Invoke End RequestId: a9c4dc8a-4b5b-48e0-9a3f-70310531ae61

Duration: 0.69 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 5.06 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```

<a name="powershell"></a>
## Powershell

#### Deploy Function

PowerShell adopts the form of third-party packaging. The code package will exceed 50M. The Fun tool installs the third-party package. At the same time, the corresponding function-dependent package can be automatically placed on the NAS. Only the first deployment needs to execute `fun install -v` and` fun nas sync`, if you just want to update the powershell script later, you only need the `fun deploy -y` update function.
 
```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd powershell-demo
rsong@iZj6c895xh98:~/fc-custom-demo/powershell-demo  fun install -v 
start installing function dependencies without docker

building powershell-demo/fc-powershell
Funfile exist, Fun will use container to build forcely
Step 1/7 : FROM registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.4
...
Step 7/7 : RUN fun-install apt-get install powershell
...
sha256:7c6476a3a4496bbf3da83bfb8966acc90fa94f4f8baccd248cd79c18c4fae409
Successfully built 7c6476a3a449
Successfully tagged fun-cache-965bbabb-ab6f-44e7-9910-7dd1df1d3c3e:latest
copying function artifact to /Users/songluo/gitpro/fc-custom-demo/powershell-demo
copy from container /mnt/auto/. to localNasDir

Install Success
rsong@iZj6c895xh98:~/fc-custom-demo/powershell-demo  fun nas sync
fun nas sync
using template: template.yml
starting upload /Users/songluo/gitpro/fc-custom-demo/powershell-demo/.fun/nas/auto-default/powershell-demo to nas://powershell-demo/mnt/auto/

start fun nas init...
...
Create local NAS directory of service powershell-demo:
        /Users/songluo/gitpro/fc-custom-demo/powershell-demo/.fun/nas/auto-default/powershell-demo
        /Users/songluo/gitpro/fc-custom-demo/powershell-demo/.fun/root
fun nas init Success
...
zipping /Users/songluo/gitpro/fc-custom-demo/powershell-demo/.fun/root
✔ upload done
unzipping file
✔ unzip done
✔ upload completed!
rsong@iZj6c895xh98:~/fc-custom-demo/powershell-demo  fun deploy -y
...
        Checking if nas directories /powershell-demo exists, if not, it will be created automatically
        Checking nas directories done ["/powershell-demo"]
        Waiting for function fc-powershell to be deployed...
                Waiting for packaging function fc-powershell code...
                The function fc-powershell has been packaged. A total of 2 files were compressed and the final size was 872 B
        function fc-powershell deploy success
service powershell-demo deploy success
...
```

#### Invoke Function

``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/ruby-demo  fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: cd30369e-7dfa-439c-a68d-7fe16d5a7e05
Hello World
FC Invoke End RequestId: cd30369e-7dfa-439c-a68d-7fe16d5a7e05

Duration: 54.13 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 133.70 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```

<a name="FSharp"></a>
## FSharp

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd FSharp-demo
rsong@iZj6c895xh98:~/fc-custom-demo/FSharp-demo  make deploy
make deploy
docker run -it -v $(pwd):/tmp mcr.microsoft.com/dotnet/core/sdk:3.1 bash -c "cd /tmp/FSharpDemo && dotnet publish -r linux-x64 -c Release --self-contained true && cd /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/publish && mv FSharpDemo bootstrap && chmod +x bootstrap"
Microsoft (R) Build Engine version 16.5.0+d4cbfca49 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restore completed in 15.2 sec for /tmp/FSharpDemo/FSharpDemo.fsproj.
  FSharpDemo -> /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/FSharpDemo.dll
  FSharpDemo -> /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/publish/
fun deploy -y
...
Waiting for service fsharp_demo to be deployed...
        Waiting for function fc_fsharp to be deployed...
                Waiting for packaging function fc_fsharp code...
                The function fc_fsharp has been packaged. A total of 338 files were compressed and the final size was 39.3 MB
                Waiting for HTTP trigger http_t to be deployed...
                triggerName: http_t
                methods: [ 'GET', 'POST', 'PUT', 'DELETE' ]
                url: https://1986114430573743.cn-hangzhou.fc.aliyuncs.com/2016-08-15/proxy/fsharp_demo/fc_fsharp/
                Http Trigger will forcefully add a 'Content-Disposition: attachment' field to the response header, which cannot be overwritten 
                and will cause the response to be downloaded as an attachment in the browser. This issue can be avoided by using CustomDomain.

                trigger http_t deploy success
        function fc_fsharp deploy success
service fsharp_demo deploy success

Detect 'DomainName:Auto' of custom domain 'my_domain'
Fun will reuse the temporary domain 16225220-1986114430573743.test.functioncompute.com, expired at 2020-04-17 10:07:00, limited by 1000 per day.

Waiting for custom domain my_domain to be deployed...
custom domain my_domain deploy success
```

#### Invoke Function
In this example, the ASP.NETCore project of F # is migrated to FC in one click, and you can directly use the HTTP client tool such as a browser or curl to invoke the function. directly curl to access the temporary domain name `16225220-1986114430573743.test.functioncompute.com` which is printed on the terminal in the previous step.

``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/FSharp-demo curl 16225220-1986114430573743.test.functioncompute.com/weatherforecast 
[{"date":"2020-04-07T07:46:29.4315198+00:00","temperatureC":49,"summary":"Hot","temperatureF":120},{"date":"2020-04-08T07:46:29.431527+00:00","temperatureC":11,"summary":"Bracing","temperatureF":51},{"date":"2020-04-09T07:46:29.4315276+00:00","temperatureC":45,"summary":"Bracing","temperatureF":112},{"date":"2020-04-10T07:46:29.431528+00:00","temperatureC":13,"summary":"Chilly","temperatureF":55},{"date":"2020-04-11T07:46:29.4315284+00:00","temperatureC":-8,"summary":"Mild","temperatureF":18}]  
```

<a name="ts"></a>
## TypeScript

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd ts-demo
rsong@iZj6c895xh98:~/fc-custom-demo/ts-demo  fun deploy -y
...
Waiting for service ts-demo to be deployed...
        Waiting for function fc-ts to be deployed...
                Waiting for packaging function fc-ts code...
                The function fc-ts has been packaged. A total of 336 files were compressed and the final size was 9.41 MB
        function fc-ts deploy success
service ts-demo deploy success
```

#### Invoke Function
``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/ts-demo  fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: 7ab0a86a-be32-4086-ac17-3ce0797cda41
Hello World
FC Invoke End RequestId: 7ab0a86a-be32-4086-ac17-3ce0797cda41

Duration: 13.48 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 162.38 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```

<a name="php74"></a>
## PHP74-Swoole

Support single instance multiple concurrency

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd php74-swoole-demo
rsong@iZj6c895xh98:~/fc-custom-demo/php74-swoole-demo  fun deploy -y
···
Waiting for service php74-swoole-demo to be deployed...
        Waiting for function fc-php74-swoole to be deployed...
                Waiting for packaging function fc-php74-swoole code...
                The function fc-php74-swoole has been packaged. A total of 2 files were compressed and the final size was 785 B
        function fc-php74-swoole deploy success
service php74-swoole-demo deploy success
```

#### Invoke Function

``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/php74-swoole-demo  fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: 2d7d089d-7a41-4d81-a932-01d452ead907
string(11) "Hello World"
FC Invoke End RequestId: 2d7d089d-7a41-4d81-a932-01d452ead907

Duration: 1.01 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 32.68 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```

<a name="python37"></a>
## Python37

Support single instance multiple concurrency

#### Deploy Function

```bash
rsong@iZj6c895xh98:~/fc-custom-demo cd python37-demo
rsong@iZj6c895xh98:~/fc-custom-demo/python37-demo  fun install -v
using template: template.yml
start installing function dependencies without docker

building python37-demo/fc-python37
Funfile exist, Fun will use container to build forcely
Step 1/3 : FROM registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-custom:build-1.9.4
 ---> 91c38ebf44f1
Step 2/3 : RUN fun-install pip install flask
 ---> Using cache
 ---> bc3e7d2a77c8
Step 3/3 : RUN fun-install pip install gunicorn
 ---> Using cache
 ---> 119fe14306b6
sha256:119fe14306b6548f9c4a8642cb214f7352ecb264e806ca8e000a8a6e1f0612ec
Successfully built 119fe14306b6
Successfully tagged fun-cache-9cf56df5-03b2-4119-9dab-69178cf590ff:latest
copying function artifact to /Users/songluo/tmp/fc-custom-demo/python37-demo

Install Success

rsong@iZj6c895xh98:~/fc-custom-demo/python37-demo fun deploy -y
···
Waiting for service python37-demo to be deployed...
        Waiting for function fc-python37 to be deployed...
                Waiting for packaging function fc-python37 code...
                The function fc-python37 has been packaged. A total of 369 files were compressed and the final size was 1.5 MB
        function fc-python37 deploy success
service python37-demo deploy success
```

#### Invoke Function

``` bash
rsong@iZj6c895xh98:~/fc-custom-demo/python37-demo   fun invoke -e "Hello World"
...
========= FC invoke Logs begin =========
FC Invoke Start RequestId: 3b34c887-e0d1-4015-afbd-63a387f6044c
b'Hello World'
FC Invoke End RequestId: 3b34c887-e0d1-4015-afbd-63a387f6044c

Duration: 3.17 ms, Billed Duration: 100 ms, Memory Size: 512 MB, Max Memory Used: 54.58 MB
========= FC invoke Logs end =========

FC Invoke Result:
Hello World
```