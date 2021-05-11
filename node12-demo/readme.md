### 1. first download nodejs binary

```
sam@iZj6c895xh98:~/fc-custom-demo cd node12-demo
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo wget https://nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo tar -xvf  node-v12.13.0-linux-x64.tar.xz
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo rm node-v12.13.0-linux-x64.tar.xz
```

### 2. set PATH env in template.yml

```
'PATH': '/code/node-v12.13.0-linux-x64/bin:$PATH'
```

### 3. deploy and invoke

```bash
sam@iZj6c895xh98:~/fc-custom-demo cd node12-demo
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo  npm install
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo  fun deploy -y
...
sam@iZj6c895xh98:~/fc-custom-demo/node12-demo  fun invoke
...
```
