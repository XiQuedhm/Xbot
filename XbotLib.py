import os
import random as rd
import time as t
import re
import sys
import config

sudo = os.system
fileWay = config.workPath
#fileWay = '/root/go-cqhttp/Xbot/'
#fileWay = '/storage/emulated/0/Quark/Download/Xbot/'
#工作目录

class Load :
    #只有加载时会运行的函数归类到这里
    def loadPlugins():
    for folder in ['./plugins/', './builtinPlugins/']:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.zip'):
                    zip_file = os.path.join(root, file)
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(os.path.join('./cache/', os.path.splitext(file)[0]))
    return os.path.abspath('./cache/')
    #这个函数是ChatGPT写的，我也不太清楚咋运行的
    #不过，它是用来加载插件的
    
def runFunction(func, *args):
    t = threading.Thread(target=func, args=args)
    t.start()

def loadPluginsFunctions():
    data = {}
    plugins = [0, {}]
    commands = 0
    for root, dirs, files in os.walk('./cache/'):
        if root != './cache/':
            for file in files:
                if file.endswith('.py') and not file.endswith('.lib.py'):
                    name = os.path.splitext(file)[0]
                    file_path = os.path.join(root, file)
                    folder_path = os.path.abspath(root)
                    data[name] = [file_path, folder_path]
                    commands += 1
            folder_name = os.path.basename(root)
            plugins[0] += 1
            plugins[1][folder_name] = os.path.abspath(root)
    result = {'data': data, 'plugins': plugins, 'commands': commands}
    return result
    
class Internal :
    #和框架本身有关的类，其中定义运行时会调用的方法
    def updateJson(filePath, key=None, value=None):
    if value is None:
        value = key
        key = None
    data = {}
    if os.path.exists(filePath):
        with open(filePath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    if key:
        keys = key.replace('[', '.').replace(']', '').split('.')
        d = data
        for k in keys[:-1]:
            if k not in d:
                d[k] = {}
            d = d[k]
        d[keys[-1]] = value
    else:
        if not isinstance(data, list):
            data = []
        data.append(value)
    with open(filePath, 'w') as f:
        json.dump(data, f)
    return data
    #GPT写的
    #输入文件，键，值，直接更改
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