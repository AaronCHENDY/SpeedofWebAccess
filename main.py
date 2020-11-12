#Author Aaron CHEN 2020.11.11

from selenium import webdriver
import os
import datetime
from tkinter import *


def accessWeb(website):
    chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver) # 模拟打开浏览器
    driver.set_window_position(400,300)
    driver.set_window_size(400,600)
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
        return (consumetime.seconds/1.00)

    #print(starttime-endtime, type(starttime-endtime))
    driver.close

def avgaccess(website,trytimes):
    accesstime = []
    sum=0
    msg=""
    singletxt = " {0}  ".format(website)
    displaytxt(singletxt)
    for x in range(trytimes):
        accesstime.append(accessWeb(website))
        print("     第",x+1,"次打开网页",website,"时间为：",accesstime[x],"秒")
        singletxt="\t\t\t Try {0} : \t{1} s".format(x+1,accesstime[x])
        displaytxt(singletxt)
        sum=sum+accesstime[x]

    print("平均打开网页",website,"时间为：",round((sum/trytimes),2),"秒")
    avgtime=round((sum/trytimes),2)
    singletxt ="\n\t\t\t Average: \t{0} s ".format(avgtime)
    displaytxt(singletxt)
    return msg

def displaytxt(msg):

    global allmessage
    allmessage=str(allmessage) +"\n"+str(msg)

def mainaction():
    global allmessage
    allmessage=""
    for site in websites:
        txt=(avgaccess(site,int(accesstimes)))
        displaytxt(txt)
    Message(myWindow, text=allmessage, bg="#87CFFF", font=('Arial 10'),width=400).place(x=300,y=50)

def readwebsites():
    f = open('c:\\temp\web.txt', 'r')
    global websites
    websites=f.readlines()

def getaccesstimes(v):
    global accesstimes
    accesstimes=v

def initl_window():
    global myWindow
    myWindow = Tk()
    myWindow.title('Websites Access Time')
    myWindow.geometry('700x500')
    Message(myWindow, text=websites, bg="#FFFFAA", font=('Arial 10 bold'),width=250 ).place(x=20,y=30)
    Message(myWindow, text="Web Access Simulation！", bg="gray", font=('Arial 14 bold'), width=500).place(x=200,y=10)
    Button(text='Start', width=10, command=mainaction).place(x=50, y=300)
    Scale(myWindow, label='Times to try', from_=0, to=5, length=150, showvalue=1, tickinterval=1, resolution=1,
          orient=HORIZONTAL, command=getaccesstimes).place(x=50, y=200)

readwebsites()
initl_window()
allmessage=""
f = open('c:\\temp\web.txt', 'r')

myWindow.mainloop()
