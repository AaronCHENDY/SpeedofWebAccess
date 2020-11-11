#Author Aaron CHEN 2020.11.11

from selenium import webdriver
import os
import datetime
from tkinter import *


def accessWeb(website):
    chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
    starttime = datetime.datetime.now()
    try:
        #website="http://www.decathlon.com.cn/"
        driver.get(website)  # 打开网址
    #driver.maximize_window()  # 窗口最大化（无关紧要哈）
        driver.close()
        endtime =datetime.datetime.now()
        consumetime=endtime-starttime
        #print ("打开",website,"网页时间为",consumetime.seconds,"秒")
    except:
        consumetime=100
        return consumetime

        #print ("打开网页时间为",consumetime,"秒")
    else:
        return consumetime.seconds

    #print(starttime-endtime, type(starttime-endtime))
    driver.close

def avgaccess(website,trytimes):
    accesstime = []
    sum=0
    msg=""
    singletxt = "访问网页 {0} 结果".format(website)
    displaytxt(singletxt)
    for x in range(trytimes):
        accesstime.append(accessWeb(website))
        print("     第",x+1,"次打开网页",website,"时间为：",accesstime[x],"秒")
        singletxt="\t\t 第 {0} 次时间为 {1} 秒".format(x+1,accesstime[x])
        displaytxt(singletxt)
        sum=sum+accesstime[x]

    print("平均打开网页",website,"时间为：",round((sum/trytimes),2),"秒")
    avgtime=round((sum/trytimes),2)
    singletxt ="\n\t平均时间为 {0} 秒 ".format(avgtime)
    displaytxt(singletxt)
    return msg

def displaytxt(msg):

    global allmessage
    allmessage=str(allmessage) +"\n"+str(msg)



allmessage=''
myWindow = Tk()
myWindow.title('Websites Access Time')
myWindow.geometry('800x600')


f=open('c:\\temp\web.txt','r')
websites=f.readlines()

for site in websites:
    txt=(avgaccess(site,2))
    displaytxt(txt)

Message(myWindow,text=allmessage, bg='gray', font=('Arial 12 bold'), width=800).pack()

myWindow.mainloop()

