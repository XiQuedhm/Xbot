getBotInfo = {
    "endPoint": "/get_bot_info",
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

sendPrivateMsg = {
    "endPoint": "/send_private_msg",
    "hasArg": True,
    "keys": ["user_id", "group_id", "message", "auto_escape"]
}