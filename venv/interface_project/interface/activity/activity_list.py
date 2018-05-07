
#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class ChargeClass(object):
    url = "http://api.beta.acewill.net/activity/list"

    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":1262797,\"shop_id\":1786077185}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "ef8af663-f169-d762-61f8-6909da74ade2"
    }

    def __init__(self):
        pass


    #储值预览
    @property
    def activityList(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print json.dumps(ChargeClass().activityList).decode('unicode-escape')