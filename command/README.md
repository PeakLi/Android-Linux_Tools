# windows ubuntu socket命令共享
windows目录 为windows下运行
ubuntu 目录放置服务器内

1. 首先配置windows目录下脚本，windows下运行，需要python环境
```
python server.py
```

2. 随后配置ubuntu目录下脚本，服务器运行
```
nohup python command_execute_client.py &
```

3. 配置 f 命令内目录 为自己服务器目录，随后移动到服务器
/usr/bin 目录下


最后即可直接用 
f o . 
f sub .
f bird.mk 等命令
并自定义其他命令


