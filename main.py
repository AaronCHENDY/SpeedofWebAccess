#Author Aaron CHEN 2020.11.11

from selenium import webdriver
import os
import datetime
from tkinter import *
allmessage=''

def accessWeb(website):
    chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器

    try:
        starttime = datetime.datetime.now()
        driver.get(website)  # 打开网址
    #driver.maximize_window()  # 窗口最大化
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
    singletxt = "尝试访问 {0} {1}次，时间如下".format(website,trytimes)
    displaytxt(singletxt)
    for x in range(trytimes):
        accesstime.append(accessWeb(website))
        print("     第",x+1,"次打开网页",website,"时间为：",accesstime[x],"秒")
        singletxt="\t\t 第 {0} 次耗时 {1} 秒".format(x+1,accesstime[x])
        displaytxt(singletxt)
        sum=sum+accesstime[x]

    print("平均打开网页",website,"时间为：",round((sum/trytimes),2),"秒")
    avgtime=round((sum/trytimes),2)
    singletxt ="\n\t平均耗时为 {0} 秒 ".format(avgtime)
    displaytxt(singletxt)
    return msg

def displaytxt(msg):

    global allmessage
    allmessage=str(allmessage) +"\n"+str(msg)





def mainaction():

    f=open('c:\\temp\web.txt','r')
    websites=f.readlines()

    for site in websites:
        txt=(avgaccess(site,3))
        displaytxt(txt)
    Message(myWindow, text=allmessage, bg="#87CEEB", font=('Arial 12 bold'), width=600).pack()

myWindow = Tk()
myWindow.title('Websites Access Time')
myWindow.geometry('800x600')

Message(myWindow,text="开始测速！", bg="#87CEEB", font=('Arial 12 bold'),width=600).pack()
Button(text='提交', width=10,command=mainaction).pack()

myWindow.mainloop()
