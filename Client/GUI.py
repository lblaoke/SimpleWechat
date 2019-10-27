from sys import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import*
from socket import *

# 定位服务器
serverName='172.23.77.52'
serverPort=12000

# 定义聊天界面
class chat(QWidget):
    number=''
    def __init__(self,num):
        self.number=num
        super().__init__()
    def start(self):
        self.initUI()
    def initUI(self):
        self.setGeometry(390,170,500,350)
        self.setWindowTitle('WeChat Chatting Room')
        self.setWindowIcon(QIcon('top_image.jpg'))
        # 发送按钮
        self.send_b=QPushButton('Send',self)
        self.send_b.setToolTip('To Send These To Him/Her')
        # 发送文件图片按钮
        self.fg_b=QPushButton('Send File/Image',self)
        self.fg_b.setToolTip('To Send A File/Image To Him/Her')
        # 输入文本框
        self.num=QLineEdit()
        self.send=QTextEdit()
        self.message=QLineEdit()

        layout=QFormLayout()
        layout.addRow('Number:',self.num)
        layout.addRow(self.send)
        layout.addRow('Messages:',self.message)
        layout.addRow(self.send_b)
        layout.addRow(self.fg_b)
        self.setLayout(layout)

        self.show()
        # 内部点击响应
        self.send_b.clicked.connect(self.send_b_c)
        self.fg_b.clicked.connect(self.fg_b_c)
    def send_b_c(self):
        n,m=self.num.text(),self.message.text()
        cmd='sdm_'+self.number+'_'+n+'_***_***_'+m
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        mm=self.send.toPlainText()
        self.send.setPlainText(mm+"\nMe: "+m+' ('+reply.decode()+')')
    def fg_b_c(self):
        openfile_name=QFileDialog.getOpenFileName(self,'Select A File')
        try:
            with open(openfile_name[0],"rb") as f:
                data=f.read()
            n=self.num.text()
            cmd='sdm_'+self.number+'_'+n+'_***_***_'
            cmd=cmd.encode()+data
            while True:
                try:
                    clientSocket=socket(AF_INET, SOCK_DGRAM)
                    clientSocket.sendto(cmd,(serverName,serverPort))
                    reply,addr=clientSocket.recvfrom(2048)
                    clientSocket.close()
                    break
                except:
                    continue
            mm=self.send.toPlainText()
            self.send.setPlainText(mm+'\nMe: ('+reply.decode()+')')
        except:
            mm=self.send.toPlainText()
            self.send.setPlainText(mm+'\nMe: (Sending Fails)')
            pass

# 定义好友
class friend(QWidget):
    number=''
    def __init__(self,number):
        self.number=number
        super().__init__()
    def start(self):
        self.initUI()
    def initUI(self):
        self.setGeometry(390,170,500,350)
        self.setWindowTitle('WeChat Friends Making')
        self.setWindowIcon(QIcon('top_image.jpg'))

        cmd='swfa_'+self.number+'_***_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        # 确认按钮
        self.make_b=QPushButton('Make Friends',self)
        self.make_b.setToolTip('To Send These To Him/Her')
        # 同意按钮
        self.agree_b=QPushButton('Agree',self)
        self.agree_b.setToolTip('To Agree This Application')
        # 删好友按钮
        self.del_b=QPushButton('Delete',self)
        self.del_b.setToolTip('To Delete This Friend')
        # 输入文本框
        self.num=QLineEdit()
        self.a=QLineEdit()
        self.d=QLineEdit()

        layout=QFormLayout()
        layout.addRow('Number:',self.num)
        layout.addRow(self.make_b)
        layout.addRow('Application:',self.a)
        layout.addRow(self.agree_b)
        layout.addRow('Number:',self.d)
        layout.addRow(self.del_b)
        self.setLayout(layout)

        self.a.setText(reply.decode())

        self.show()

        # 内部点击响应
        self.make_b.clicked.connect(self.make_b_c)
        self.agree_b.clicked.connect(self.agree_b_c)
        self.del_b.clicked.connect(self.del_b_c)
    def make_b_c(self):
        n=self.num.text()
        cmd='mkfa_'+self.number+'_'+n+'_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        self.num.setText(reply.decode())
    def agree_b_c(self):
        s=self.a.text()
        cmd='mkf_'+self.number+'_'+s[:s.find(':')]+'_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        self.a.setText(reply.decode())
    def del_b_c(self):
        cmd='dlf_'+self.number+'_'+self.d.text()+'_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        self.d.setText(reply.decode())

# 定义主界面
class main(QWidget):
    num=''
    def __init__(self,num):
        self.num=num
        super().__init__()
    def start(self):
        self.initUI()
    def initUI(self):
        self.setGeometry(390,170,500,350)
        self.setWindowTitle('WeChat')
        self.setWindowIcon(QIcon('top_image.jpg'))
        # 显示好友列表
        cmd1='swf_'+self.num+'_***_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd1.encode(),(serverName,serverPort))
                reply1,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        # 添加好友按钮
        self.friend_b=QPushButton('Friends Manage',self)
        self.friend_b.setToolTip('To Manage Your Friend List')
        # 新消息按钮
        self.message_b=QPushButton('New Messages',self)
        self.message_b.setToolTip('To Check For New Messages')
        # 聊天按钮
        self.chat_b=QPushButton('Chat With Friends',self)
        self.chat_b.setToolTip('To Send Messages To Your Friends')

        self.f=QTextEdit()
        self.m=QTextEdit()

        layout=QFormLayout()
        layout.addRow('Friends:',self.f)
        layout.addRow(self.chat_b)
        layout.addRow(self.friend_b)
        layout.addRow('Messages:',self.m)
        layout.addRow(self.message_b)
        self.setLayout(layout)

        self.f.setPlainText(reply1.decode())

        self.show()
        # 内部点击响应
        self.message_b.clicked.connect(self.message_b_c)
    def message_b_c(self):
        cmd='swm_'+self.num+'_***_***_***_***'
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        reply=reply.decode()
        self.m.setPlainText(reply)

# 定义注册界面
class register(QWidget):
    na,nu,p='','',''
    def __init__(self):
        super().__init__()
    def start(self):
        self.initUI()
    def initUI(self):
        self.setGeometry(390,170,500,350)
        self.setWindowTitle('WeChat Register')
        self.setWindowIcon(QIcon('top_image.jpg'))

        self.sure_b=QPushButton('OK',self)
        self.sure_b.setToolTip('To Register A New Account')

        self.name=QLineEdit()
        self.num=QLineEdit()
        self.passwd=QLineEdit()

        layout=QFormLayout()
        layout.addRow('Name:',self.name)
        layout.addRow('Number:',self.num)
        layout.addRow('Password:',self.passwd)
        layout.addRow(self.sure_b)
        self.setLayout(layout)

        self.show()
        
        self.sure_b.clicked.connect(self.sure_b_c)
    def sure_b_c(self):
        na,nu,p=self.name.text(),self.num.text(),self.passwd.text()
        cmd='regu_'+nu+'_***_'+p+'_'+na+'_***'
        self.na,self.nu,self.p=na,nu,p
        while True:
            try:
                clientSocket=socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(cmd.encode(),(serverName,serverPort))
                reply,addr=clientSocket.recvfrom(2048)
                clientSocket.close()
                break
            except:
                continue
        reply=reply.decode()
        self.name.setText(reply)
        self.num.setText(reply)
        self.passwd.setText(reply)

# 定义登录界面
class login(QWidget):
    re_s=''
    def __init__(self):
        super().__init__()
    def start(self):
        self.initUI()
    def initUI(self):
        self.setGeometry(390,170,500,350)
        self.setWindowTitle('WeChat Login')
        self.setWindowIcon(QIcon('top_image.jpg'))
        # 登录按钮
        self.login_b=QPushButton('Login',self)
        self.login_b.setToolTip('To Login For Social Life')
        # 注册按钮
        self.register_b=QPushButton('Register',self)
        self.register_b.setToolTip('To Register A New Account')
        # 输入文本框
        self.num=QLineEdit()
        self.passwd=QLineEdit()

        layout=QFormLayout()
        layout.addRow('Number:',self.num)
        layout.addRow('Password:',self.passwd)
        layout.addRow(self.login_b)
        layout.addRow(self.register_b)
        self.setLayout(layout)

        self.show()