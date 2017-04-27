#coding=utf-8

from pymongo import MongoClient

#连接数据库
client=MongoClient()
db=client.Taoey

man=0
woman=0
what=0
q=db.QQ_people.find()

data=[]
for i in q:
    if i["_sex"]=='男':
        man+=1
    elif i["_sex"]=='女':
        woman+=1
    else:
        what+=1
data.append(man)
data.append(woman)
data.append(what)
print(data)
input()

