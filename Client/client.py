from sys import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import*
from socket import *
from GUI import *

# 定位服务器
serverName='172.23.77.52'
serverPort=12000

# 打开系统窗口调用
window=QApplication(argv)

# 运行各个窗口
ex_login=login()
ex_register=register()
ex_main=main('0')
ex_chat=chat('0')
ex_friend=friend('0')

def login_c():
	number=ex_login.num.text()
	passwd=ex_login.passwd.text()
	cmd='lgin_'+number+'_***_'+passwd+'_***_***'
	while True:
		try:
			clientSocket=socket(AF_INET, SOCK_DGRAM)
			clientSocket.sendto(cmd.encode(),(serverName,serverPort))
			reply,addr=clientSocket.recvfrom(2048)
			clientSocket.close()
			break
		except:
			continue
	if reply.decode()=='1':
		ex_main.num=number
		ex_main.start()
		ex_chat.number=number
		ex_friend.number=number
		ex_main.friend_b.clicked.connect(ex_friend.start)
		ex_main.chat_b.clicked.connect(ex_chat.start)

# 启动登录界面
ex_login.start()

ex_login.register_b.clicked.connect(ex_register.start)
ex_login.login_b.clicked.connect(login_c)

# 关闭系统窗口调用
exit(window.exec_())