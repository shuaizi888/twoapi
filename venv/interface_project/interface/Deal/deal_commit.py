#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class DealClass(object):
    url = "http://api.beta.acewill.net/deal/commit"
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="req"\r\n\r\n{"biz_id":"8035","send_notification":true,"verify_code":"000000"}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="appid"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="ts"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="sig"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="v"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "cea4a6cd-24f7-14ab-71bc-282418bb6735"
    }

    def __init__(self):
        pass


    #消费预览
    @property
    def dealCommit(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print DealClass().dealCommit()