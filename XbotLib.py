import os
import random as rd
import time as t
import re
import sys

sudo = os.system
fileWay = '/root/go-cqhttp/Xbot/'
fileWay = '/storage/emulated/0/Quark/Download/Xbot/'
#工作目录

class Internal :
    #和框架本身有关的类，其中定义运行时会调用的方法
    def logInput(logType,logBody):
        #用来写运行日志的方法
        logType = str(logType)
        logTypeMap={
            "0": "[main]",
            "1": "[info]",
            "2": "[error]",
            "3": "[warning]",
            "4": "[comment]",
            "5": "[other]"
        }
        if logType in logTypeMap :
            logType = logTypeMap[logType]
        else :
            logType = "["+logType+"]"
        logList = os.listdir(Internal.fileWay+'logs/')
        #解析输入的日志类型
        localTime = t.localtime()
        todayLogFileName = str(localTime[0])+"-"+str(localTime[1])+"-"+str(localTime[2])+".log"
        #查看时间和创建文件名
        if todayLogFileName in logList :
            doWriteFileHead = False
        else :
            doWriteFileHead = True
        #检查文件是否已存在
        with open(todayLogFileName,"a") as logFile:
            if doWriteFileHead :
                content = "[info]Log created at "+str(t.time()//1)+" by botsheel named Xbot\n"+logType+logBody+"\n"
            else :
                content = logType+logBody+"\n"
            #生成日志头和内容
            logFile.write(content)
            #写入
        return content
        #方法返回写入的内容

class Request :
    #和go-cqhttp有关的类，其中定义发送信息，图片等时调用的方法
    def passs() :
        pass
        return ""

if __name__ == "__main__" :
    print(Internal.logInput(4,'test'))