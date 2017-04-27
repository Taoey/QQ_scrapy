from tools import MyEmail,Mydb
if __name__ == '__main__':

    #数据库连接测试      //成功

    db=Mydb.connect()
    data={ "ok" : 1 }
    db.createCollection("mycollection")
    db.QQ.insert_one(
        {
            'qq':'741494582',
        }

    )


    #发送邮件模块测试

    # address_list=["741494582@qq.com"]
    #
    # etext="你最近好吗"
    # e=MyEmail()
    # e.send(address_list,etext)
    pass


