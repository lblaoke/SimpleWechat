from pandas import *

# get data
def get_u(R,number):
	k=R[R.number==number].index.tolist()[0]
	return R.loc[k]

def get_f(R,number):
	return R[R.number==number][['name1','number1']]

def get_m(R,number,time):
	return R[(R.number==number)&(R.time>=time)][['sentense','name','time']]

def get_n(R,number):
	k=R[R.number==number].index.tolist()[0]
	try:
		return R.loc[k]
	except:
		return None

# put new data
def insert_u(R,name,number,password):
	new=DataFrame({'number':number,'name':name,'password':password},index=[1])
	return R.append(new,ignore_index=True)

def insert_f(R1,R2,number1,number2):
	k1=R2[R2.number==number1].index.tolist()[0]
	k2=R2[R2.number==number2].index.tolist()[0]
	new1=DataFrame({'number':number1,'number1':number2,'name1':R2.loc[k2]['name']},index=[1])
	new2=DataFrame({'number':number2,'number1':number1,'name1':R2.loc[k1]['name']},index=[1])
	R1=R1.append(new1,ignore_index=True)
	return R1.append(new2,ignore_index=True)

def insert_m(R1,R2,number1,number2,sentense,time):
	k=R2[R2.number==number1].index.tolist()[0]
	new=DataFrame({'number':number2,'sentense':sentense,'from':number1,'name':R2.loc[k]['name'],'time':time},index=[1])
	return R1.append(new,ignore_index=True)

def insert_n(R1,R2,number1,number2):
	k=R2[R2.number==number1].index.tolist()[0]
	new=DataFrame({'number':number2,'number1':number1,'name1':R2.loc[k]['name']},index=[1])
	return R1.append(new,ignore_index=True)

# remove data
def del_u(R,number):
	k=R[R.number==number].index.tolist()[0]
	R.drop(k,inplace=True)

def del_f(R,number1,number2):
	k1=R[(R.number==number1)&(R.number1==number2)].index.tolist()[0]
	k2=R[(R.number==number2)&(R.number1==number1)].index.tolist()[0]
	if k1>k2:
		k1,k2=k2,k1
	R.drop(k2,inplace=True)
	R.drop(k1,inplace=True)

def del_n(R,number,number1):
	lk=R[(R.number==number)&(R.number1==number1)].index.tolist()
	lk.reverse()
	for k in lk:
		R.drop(k,inplace=True)

# status check
def isexist(R,number):
	return R[R.number==number].shape[0]
	
def isfriend(R,number1,number2):
	return R[(R.number==number1)&(R.number1==number2)].shape[0]