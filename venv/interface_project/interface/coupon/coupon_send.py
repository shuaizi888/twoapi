
#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class ChargeClass(object):
    url = "http://api.beta.acewill.net/coupon/send"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":\"1261358\",\"template_id\":8890544,\"amount\":1,\"biz_id\":40,\"shop_id\":\"1112645845\"}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "6518dd4a-0e81-da2d-6bf1-0172ef306ded"
    }
    def __init__(self):
        pass


    #
    @property
    def couponSend(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print json.dumps(ChargeClass().couponSend).decode('unicode-escape')