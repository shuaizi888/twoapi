#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class DealClass(object):
    url = "http://api.beta.acewill.net/user/editusergrade"
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="req"\r\n\r\n{"cno":"1547201834925609","grade_id":"3001586","cashier_id":1216158497,"limit_time":1504195200}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="appid"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="ts"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="sig"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="v"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "6eb8950f-4839-3857-15e9-91a14c7e1663"
    }

    def __init__(self):
        pass


    #
    @property
    def userEditusergrade(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print json.dumps(DealClass().userEditusergrade).decode('unicode-escape')