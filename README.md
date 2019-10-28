# simple-wechat
令人崩溃的《计算机网络》实验，断断续续做了快一个月，终于完成了

## 运行环境配置
* 要求电脑本地有Anaconda，并且应将python.exe的路径加入Path环境变量中
    
## 服务器端的运行与关闭
* 打开system.py文件，解锁print(system('start/b python server.py'))，运行system.py，则服务器开始运行
* 若解锁print(system('taskkill /im python.exe /f'))并运行system.py，则服务器关闭
    
## 客户端的使用
* 在使用客户端之前，首先应将所有.py文件中的IP地址改为当前运行服务器的主机的IP地址
* 双击wechat.exe程序，首先会弹出一个黑框，然后会出现登录界面
* 只要关闭登录界面，则黑框消失，这表示客户端已经关闭
