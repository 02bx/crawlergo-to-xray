**操作步骤（以ubuntu 64位操作系统为例）**

**一、运行xray可执行文件生成如下文件并配置**

1. ca.crt
2. ca.key
3. config.yaml

**二、依次启动webhook、xray、crawlergo**

（1）启动webhook并查看日志（需要自行修改代码中的配置）

1. nohup python3 webhook.py > webhook.log 2>&1 &
2. tail -f webhook.log

（2）启动xray并查看日志（需要自行修改xray的配置文件以及命令行中的的配置，建议在xray里面配置username和password）

1. nohup ./xray_linux_amd64  webscan  --listen 0.0.0.0:[xray_port]   --webhook-output http://127.0.0.1:[webhook_port]/webhook   --html-output  xray.html   >   xray.log    2>&1 &
2. tail -f  xray.log

（3）启动crawlergo并查看日志（需要自行修改代码中的配置）

1.  nohup python3 crawlergo.py  >   crawlergo.log 2>&1 &
2.  tail -f crawlergo.log



**参考资料：**

1. crawlergo（crawlergo是一个使用`chrome headless`模式进行URL入口收集的动态爬虫），可参考：https://github.com/0Kee-Team/crawlergo

   

2. crawlergo可执行文件来源：https://github.com/0Kee-Team/crawlergo/releases/download/v0.3.0/crawlergo_linux_amd64.zip

   

3. xray（一款功能强大的安全评估工具），可参考：https://github.com/chaitin/xray

   

4. xray_linux_amd64可执行文件来源：https://github.com/chaitin/xray/releases/download/0.21.8/xray_linux_amd64.zip

   

5. Server酱（一款就是从服务器推报警和日志到手机的工具），可参考http://sc.ftqq.com/3.version

   

6. 其他参考：https://github.com/timwhitez/crawlergo_x_XRAY







