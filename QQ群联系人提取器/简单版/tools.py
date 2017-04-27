#coding = utf-8
#Web
from selenium import webdriver
from lxml import etree
import time
from models import QQ_group
import random
import codecs
#####################################


def get_freshList(dataList):
    '处理获得的list数据,清除多余的字符'
    freshList=[]
    for i in dataList:
        freshList.append("".join(i.replace('\n','').replace(' ','').replace('\t','')))

    return freshList

class MyWeb:

    def get_qq_group(self,user, password):

        chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox()
        #chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
        #driver = webdriver.PhantomJS()

        driver.get("http://qun.qq.com/member.html")

        IframeElement = driver.find_element_by_name("login_frame")
        driver.switch_to_frame(IframeElement)
        try:
            driver.find_element_by_xpath("//*[@id='bottom_qlogin']/a[1]").click()  # 登录界面
            driver.find_element_by_xpath("//*[@id='u']").send_keys(user)
            driver.find_element_by_xpath("//*[@id='p']").send_keys(password)

            driver.find_element_by_xpath("//*[@id='login_button']").click()  # 点击登录
            time.sleep(2)

            driver.switch_to_default_content()  # 防止出现TypeError: can't access dead object 错误特别重要

            web_data = driver.page_source
            selector = etree.HTML(web_data)
        except Exception as e:
            print("登录失败,请检查QQ号和账号及网络状态")


        try:
            qq_numbers= selector.xpath("//li[@data-id]/@data-id")  # 获取所有的QQ群组号码和名称
            qq_names= selector.xpath("//li[@data-id]/@title")
            qq_group=""
            for qq_name, qq_number in zip(qq_names, qq_numbers):
                # print("%-20s  %-13s " % (qq_name, qq_number))
                # print("\n")
                qq_group+="%-20s  %-13s " % (qq_name, qq_number)+"\n\n"
                f = codecs.open("D:\qq_group.txt", "w", "utf-8")
                f.write(qq_group)
                f.close()
            print("数据保存完毕,请打开'D:\qq_group.txt'查看全部数据")

        except Exception as e:
            print(e)
            print("QQ服务器又讨厌咱了,换个qq号或者等下再试吧")
        driver.quit()








    def get_qq_nums(self,user,password,qq_group):
        chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox()
        #chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
        #driver = webdriver.PhantomJS()
        driver.get("http://qun.qq.com/member.html#gid={}".format(qq_group))

        IframeElement = driver.find_element_by_name("login_frame")
        driver.switch_to_frame(IframeElement)

        driver.find_element_by_xpath("//*[@id='bottom_qlogin']/a[1]").click()  # 登录界面
        driver.find_element_by_xpath("//*[@id='u']").send_keys(user)
        driver.find_element_by_xpath("//*[@id='p']").send_keys(password)

        driver.find_element_by_xpath("//*[@id='login_button']").click()  # 点击登录
        time.sleep(2)

        driver.switch_to_default_content()  # 防止出现TypeError: can't access dead object 错误特别重要
        time.sleep(2)
        web_data = driver.page_source
        selector = etree.HTML(web_data)
        try:
            people_num = selector.xpath("//*[@id='groupMemberNum']/text()")  # 获取群组人数量
            people_num = int(people_num[0])
        except Exception as e:
            print("你的网貌似不太好啊,找个好点的网,兄台")

        count = 1
        for _ in range(int(people_num / 20)):
            js = "var q=document.documentElement.scrollTop=500000"
            driver.execute_script(js)
            time.sleep(random.randint(2, 6))
            print("正在爬取第"+str(count)+"页...")
            count += 1

        web_data = driver.page_source  # 重新获取网页源代码
        selector = etree.HTML(web_data)

        people_nicks = selector.xpath("//tbody[@class='list']/tr/td[3]/span/text()")  # 获取昵称
        people_nicks = get_freshList(people_nicks)

        people_names=selector.xpath("//tbody[@class='list']/tr/td[4]/span/text()")     #获取群名片                                  #获取群名片
        people_names=get_freshList(people_names)

        people_QQs = selector.xpath("//tbody[@class='list']/tr/td[5]/text()")  # 获取qq号
        people_QQs = get_freshList(people_QQs)

        people_sexs = selector.xpath("//tbody[@class='list']/tr/td[6]/text()")  # 获取性别
        people_sexs = get_freshList(people_sexs)

        people_ages = selector.xpath("//tbody[@class='list']/tr/td[7]/text()")  # 获取Q龄
        people_ages = get_freshList(people_ages)

        people_grades = selector.xpath("//tbody[@class='list']/tr/td[9]/text()")  # 获取活跃度
        people_grades = get_freshList(people_grades)

        # 保存邮箱数据
        count=0
        qq_email=""
        for count in range(len(people_QQs)):
            qq_email+=people_QQs[count]+"@qq.com;"
            if((count-1) % 50==0):
                qq_email+="\n\n\n"
        f=codecs.open("D:\qq_email.txt","w","utf-8")
        f.write(qq_email)
        f.close()
        print("数据保存完毕,请打开'D:\qq_email.txt'查看邮箱数据")

        #保存联系人所有信息
        count=0
        qq_data=""
        for count in range(len(people_QQs)):
            qq_data+="%-20s %-20s %-13s  " % (people_names[count],people_nicks[count],people_QQs[count])+"\n\n"
        f = codecs.open("D:\qq_data.txt", "w", "utf-8")
        f.write(qq_data)
        f.close()
        print("数据保存完毕,请打开'D:\qq_data.txt'查看全部数据")


        driver.quit()

        pass

