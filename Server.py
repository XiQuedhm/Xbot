from flask import Flask, request
import requests as r
import os
import time as t
import threading as thread
import XbotLib as Lib
import config
import zipfile

load = Lib.Load
inter = Lib.Internal
bot = Lib.Request
sudo = os.system
startTime = t.time()

true = True
false = False

inter.logInput(0, "アトリは、高性能ですから!")
time1 = t.time()
count = load.load()
time2 = t.time()
inter.logInput(0, "共加载了"+str(count)+"个插件，耗时"+str(time2-time1)+"秒")

with open("./data/blackList.json", "r") as file :
    blackList = list(file.read())

blackList = Lib.user.black

app = Flask('Xbot')
@app.route('/', methods=["POST"])
def postData():
    data = request.get_json()
    eventType = data['post_type']
    if eventType == "request" :
        if config.doAutoAcceptFriendRequest or config.doAutoAcceptGroupRequest:
            back = "true"
        else :
            back = "false"
        UsrID = data["user_id"]
        if UsrID in blackList:
            back = "false"
        flag = data["flag"]
        if data["Post_Request_Type"] == "friend" :
            endPoint = "/set_friend_add_request"
        elif data["type"] == "invite" :
            endPoint = "/set_group_add_request"
        url = Lib.url+endPoint+"?flag="+flag+"&approve="+back
        if back:
            back = "同意"
        else:
            back = "拒绝"
        r.get(url)
        inter.logInput(1, back+"了来自"+UsrID+"的好友/群请求")
        
    if eventType == 'message' :
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
    elif eventType == "notice" :
        pass
    elif eventType == "meta_event" :
        pass
        
    
    return "OK"
    
if __name__ == '__main__':
    print(startTime)
    app.run(host='127.0.0.1',port=config.listenPort)