getBotInfo = {
    "endPoint": "/get_login_info",
    "hasArg": False,
    "keys": []
}

setBotProfile = {
    "endPoint": "/set_qq_profile",
    "hasArg": True,
    "keys": ["nickname", "company", "email", "college", "personal_note"]
}

getStrangerInfo = {
    "endPoint": "/get_stranger_info",
    "hasArg": True,
    "keys": ["user_id"]
}

getFriendList = {
    "endPoint": "/get_friend_list",
    "hasArg": False,
    "keys": []
}

getUnidirectionalFriendList = {
    "endPoint": "/get_unidirectional_friend_list",
    "hasArg": False,
    "keys": []
}

#friend actions

delFriend = {
    "endPoint": "/delete_friend",
    "hasArg": True,
    "keys": ["user_id"]
}

delUnidirectionalFriend = {
    "endPoint": "/delete_unidirectional_friend",
    "hasArg": True,
    "keys": ["user_id"]
}

#messages

sendPrivateMsg = {
    "endPoint": "/send_private_msg",
    "hasArg": True,
    "keys": ["user_id", "group_id", "message", "auto_escape"]
}

sendGroupMsg = {
    "endPoint": "/send_group_msg",
    "hasArg": True,
    "keys": ["group_id", "message", "auto_escape"]
}

sendMsg = {
    "endPoint": "/send_msg",
    "hasArg": True,
    "keys": ["message_type", "user_id", "group_id", "message", "auto_escape"]
}

getMsg = {
    "endPoint": "/get_msg",
    "hasArg": True,
    "keys": ["message_id"]
}

delMsg = {
    "endPoint": "/delete_msg",
    "hasArg": True,
    "keys": ["message_id"]
}

markMsgRead = {
    "endPoint": "/mark_msg_as_read",
    "hasArg": True,
    "keys": ["message_id"]
}

getForwardMsg = {
    "endPoint": "/get_forward_msg",
    "hasArg": True,
    "keys": ["message_id"]
}

sendGroupForwardMsg = {
    "endPoint": "/send_group_forward_msg",
    "hasArg": True,
    "keys": ["group_id", "messages"]
}

sendPrivateForwardMsg = {
    "endPoint": "/send_private_msg",
    "hasArg": True,
    "keys": ["user_id", "messages"]
}

getGroupMsgHistory = {
    "endPoint": "/get_group_msg_history",
    "hasArg": True,
    "keys": ["group_id", "message_seq"]
}

#images

getImg = {
    "endPoint": "/get_image",
    "hasArg": True,
    "keys": ["file"]
}

canSendImg = {
    "endPoint": "/can_send_image",
    "hasArg": False,
    "keys": []
}

imgOCR = {
    "endPoint": "/ocr_image",
    "hasArg": True,
    "keys": ["image"]
}
