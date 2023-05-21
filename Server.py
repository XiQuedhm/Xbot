from flask import Flask, request
import requests as r
import os
import time as t
import threading as thread
import XbotLib as Lib
import zipfile

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
    
#def loadPluginsFunctions():
#    for root, dirs, files in os.walk('./cache/'):
#        for file in files:
#            if file == 'main.py':
#                with open(os.path.join(root, file)) as f:
#                    code = f.read()
#                    exec(code)

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

print('正在加载插件')
loadPlugins()
print('アトリは、高性能ですから!')

inter = Lib.Internal
bot = Lib.Request
sudo = os.system
startTime = t.time()

app = Flask('Xbot')
@app.route('/', methods=["POST"])
def postData():
    data = request.get_json()
    eventType = data['post_type']
    if eventType == message :
        eventMessageTpye = data['message_type']
        eventMessageID = data['message_id']
        eventMessageSenderID = data['user_id']
        eventMessage = data['raw_message']
        eventMessageSender = data['sender']
        eventMessageSenderNickname = eventMessageSender['nickname']
        if eventMessageTpye == 'group':
            eventMessageGroupID = data['group_id']
            eventMessageSenderCard = eventMessageSender['card']
            eventMessageSenderTitle = eventMessageSender['title']
            eventMessageSenderRole = eventMessageSender['role']
            eventMessageSenderLevel = eventMessageSender['level']
    elif True :
        pass
        
    
    return "OK"
    
if __name__ == '__main__':
    print(startTime)
    app.run(host='127.0.0.1',port=63254)