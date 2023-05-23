from flask import Flask, request
import requests as r
import os
import time as t
import threading as thread
import XbotLib as Lib
import config
import zipfile

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