# 定义服务器参数
from socket import *

serverPort=12000 # 服务器指定的端口

# 将数据库加载入内存
from pandas import *
from database import *
from manage import *

user=read_csv('user.csv')
friend=read_csv('friend.csv')
message=read_csv('message.csv')
notice=read_csv('notice.csv')

# 处理命令
for i in range(1,200):
	# 接收命令
	serverSocket=socket(AF_INET,SOCK_DGRAM)
	serverSocket.bind(('',serverPort))
	cmd,addr=serverSocket.recvfrom(2048)
	cmd=cmd.decode()
	cmd=cmd.split('_')
	# 根据命令头部操作
	reply=''
	
	if cmd[0]=='regu':
		# 注册
		try:
			user=register(user,cmd[4],int(cmd[1]),int(cmd[3]))
			reply+='Register Succeeds'
		except:
			reply+='Register Fails'

	elif cmd[0]=='lgin':
		# 登录
		try:
			reply+=login(user,int(cmd[1]),int(cmd[3]))
		except:
			reply+='0'

	elif cmd[0]=='mkfa':
		# 发送好友申请
		try:
			notice=send_n(notice,user,int(cmd[1]),int(cmd[2]))
			reply+='Please Wait For Agreement'
		except:
			reply+='Application Denied'

	elif cmd[0]=='mkf':
		# 添加好友
		try:
			friend=makefriend(friend,user,int(cmd[1]),int(cmd[2]))
			reply+='Friends Making Succeeds'
		except:
			reply+='Friends Making Fails'

	elif cmd[0]=='dlf':
		try:
			delfriend(friend,user,int(cmd[1]),int(cmd[2]))
			reply+='Friend Deletion Succeeds'
		except:
			reply+='Friend Deletion Fails'

	elif cmd[0]=='sdm':
		# 发送信息
		try:
			message=send_m(message,user,int(cmd[1]),int(cmd[2]),cmd[5])
			reply+='Message Sending Succeeds'
		except:
			reply+='Message Sending Fails'

	elif cmd[0]=='swm':
		# 更新信息
		while True:
			try:
				m=receive_m(message,user,int(cmd[1]))
				ix=m.index.tolist()
				for i in ix:
					s=m.loc[i]['name']+' GMT'+str(m.loc[i]['time'])+':'+m.loc[i]['sentense']+'\n'
					reply+=s
				reply=reply[:-1]
				break
			except:
				continue

	elif cmd[0]=='swf':
		# 更新好友列表
		while True:
			try:
				f=showfriend(friend,user,int(cmd[1]))
				ix=f.index.tolist()
				for i in ix:
					s=f.loc[i]['name1']+':'+str(f.loc[i]['number1'])+'\n'
					reply+=s
				reply=reply[:-1]
				break
			except:
				continue

	elif cmd[0]=='swfa':
		# 更新信息
		while True:
			try:
				n=receive_n(notice,user,int(cmd[1]))
				try:
					reply+=str(n['number1'])+':'+n['name1']
					del_n(notice,int(cmd[1]),n['number1'])
				except:
					pass
				break
			except:
				continue

	else:
		# 处理恶意攻击
		reply+='Illegel Command'
	# 发送回复消息
	serverSocket.sendto(reply.encode(),addr)
	serverSocket.close()
	# 定期备份
	if not i%20:
		try:
			user.to_csv('user.csv',index=0)
			friend.to_csv('friend.csv',index=0)
			message.to_csv('message.csv',index=0)
			notice.to_csv('notice.csv',index=0)
		except:
			pass