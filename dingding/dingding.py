# coding=utf-8
import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=b2f297dd9a99512a6aa41fb6a92ca58a5a019396feba7087ba264575c564d01c'
HEADERS = {
"Content-Type": "application/json ;charset=utf-8 "
}
String_textMsg = {\
"msgtype": "text",\
"text": {"content": '小小人是傻子'}}
String_textMsg = json.dumps(String_textMsg)
res = requests.post(url, data=String_textMsg, headers=HEADERS)
print(res.text)