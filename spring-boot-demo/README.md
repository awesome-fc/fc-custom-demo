## Spring Boot template for Custom Runtime

### 本地运行

前置条件: 本地安装了 Open JDK 1.8


** 编译 **
```bash
$ ./mvnw package
```

** 部署 **
```bash
$ fun local start my_domain

using template: template.yml
CustomDomain my_domain of springboot/helloworld was registered
        url: http://localhost:8000/
        methods: [ 'GET', 'POST', 'PUT' ]
        authType: ANONYMOUS

function compute app listening on port 8000!
```

使用浏览器打开 http://localhost:8000/ ， 显示包含“Hello, World!”的页面。

### 部署

```bash
$ fun deploy

...
Waiting for service springboot to be deployed...
        Waiting for function helloworld to be deployed...
                Waiting for packaging function helloworld code...
                The function helloworld has been packaged. A total of 3 files were compressed and the final size was 14.33 MB
                Waiting for HTTP trigger httpTrigger to be deployed...
                triggerName: httpTrigger
                methods: [ 'GET', 'POST', 'PUT' ]
                trigger httpTrigger deploy success
        function helloworld deploy success
service springboot deploy success

Detect 'DomainName:Auto' of custom domain 'my_domain'
Request a new temporary domain ...
The assigned temporary domain is http://46655565-1986114430573743.test.functioncompute.com，expired at 2021-04-04 14:59:25, limited by 1000 per day.
```

### 访问函数

```
$ curl -v http://46655565-1986114430573743.test.functioncompute.com

> GET / HTTP/1.1
> Host: 46655565-1986114430573743.test.functioncompute.com
> User-Agent: curl/7.64.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Access-Control-Expose-Headers: Date,x-fc-request-id,x-fc-error-type,x-fc-code-checksum,x-fc-invocation-duration,x-fc-max-memory-usage,x-fc-log-result,x-fc-invocation-code-version
< Content-Length: 13
< Content-Type: text/plain;charset=UTF-8
< X-Fc-Code-Checksum: 8251929770646990123
< X-Fc-Invocation-Duration: 175
< X-Fc-Invocation-Service-Version: LATEST
< X-Fc-Max-Memory-Usage: 141.65
< X-Fc-Request-Id: 81853de8-a084-45fb-b8b1-e91c6c37dfc9
< Date: Thu, 25 Mar 2021 07:03:09 GMT
< 
* Connection #0 to host 46655565-1986114430573743.test.functioncompute.com left intact
Hello, World!
```