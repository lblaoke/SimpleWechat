from pandas import *

# define types and columns
user=DataFrame([[0,'fbd',0],[1,'yjj',1],[9,'lbl',9]],columns=['number','name','password'])
friend=DataFrame([[0,1,'yjj'],[1,0,'fbd'],[0,9,'lbl'],[9,0,'fbd']],columns=['number','number1','name1'])
message=DataFrame([[0,'hello world!',1,'yjj',10],[0,'现充',9,'lbl',20]],columns=['number','sentense','from','name','time'])
notice=DataFrame([[1,9,'lbl']],columns=['number','number1','name1'])

# save to HD
user.to_csv('user.csv',index=0)
friend.to_csv('friend.csv',index=0)
message.to_csv('message.csv',index=0)
notice.to_csv('notice.csv',index=0)