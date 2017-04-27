import getpass
from tools import MyEmail,Mydb,MyWeb
from models import QQ_group
from pymongo import MongoClient


if __name__ == '__main__':

    run =True
    while run :
        try:
            #获取用户数据
            qq_num=input("兄台,请输入你的QQ号:")
            qq_password=getpass.getpass('然后,你的密码(密码不显示哦):')
            my_web = MyWeb()
            you_group = input("你的qq群组qq号:")
            my_web.get_qq_nums(qq_num, qq_password, you_group)
            run=False
        except Exception as e:
            print("不正确输入账号密码是不行滴,重来一遍吧")
            print(e)
        choice=input("是否要继续:(Y/N)")
        if choice=="N":
            run=False
        else:
            run=True







