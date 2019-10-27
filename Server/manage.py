from database import *

# bebavior management
def register(R,name,number,password):
	if isexist(R,number):
		return R
	return insert_u(R,name,number,password)

def login(R,number,password):
	u=get_u(R,number)
	if(u['password']==password):
		return '1'
	else:
		return '0'

def makefriend(R1,R2,number1,number2):
	if not(isexist(R2,number1) and isexist(R2,number2) and (not isfriend(R1,number1,number2))):
		return R1
	return insert_f(R1,R2,number1,number2)

def delfriend(R1,R2,number1,number2):
	if not(isexist(R2,number1) and isexist(R2,number2) and isfriend(R1,number1,number2)):
		return
	del_f(R1,number1,number2)

def showfriend(R1,R2,number):
	if not isexist(R2,number):
		return None
	return get_f(R1,number)

from time import time

def send_m(R1,R2,number1,number2,sentense):
	if not(isexist(R2,number1) and isexist(R2,number2)):
		return R1
	return insert_m(R1,R2,number1,number2,sentense,time())

def send_n(R1,R2,number1,number2):
	if not(isexist(R2,number1) and isexist(R2,number2)):
		return R1
	return insert_n(R1,R2,number1,number2)

def receive_m(R1,R2,number):
	if not isexist(R2,number):
		return None
	return get_m(R1,number,time()-1800)

def receive_n(R1,R2,number):
	if not isexist(R1,number):
		return None
	return get_n(R1,number)