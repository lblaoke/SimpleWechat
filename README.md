# simple-wechat
令人崩溃的《计算机网络》实验，断断续续做了快一个月，终于完成了

1.运行环境配置：
    要求电脑本地有Anaconda，并且应将python.exe的路径加入Path环境变量中。
    
1.服务器端的运行与关闭：
    打开system.py文件，解锁print(system('start/b python server.py'))，运行system.py，则服务器开始运行。
    若解锁print(system('taskkill /im python.exe /f'))并运行system.py，则服务器关闭。
    
2.客户端的使用：
    双击wechat.exe程序，首先会弹出一个黑框，然后会出现登录界面。
    只要关闭登录界面，则黑框消失，这表示客户端已经关闭。