
#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class ChargeClass(object):
    url = "http://api.beta.acewill.net/coupon/adjust"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":\"2121261517181\",\"shop_id\":1429830612,\"operate_id\":1239332226,\"c2uIds\":[\"1573228940658295\",\"1567805266085908\"],\"remark\":'api核销'}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "e7adb14c-d3f8-dd72-f160-1f0e95644be8"
    }
    def __init__(self):
        pass


    #
    @property
    def couponAdjust(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print json.dumps(ChargeClass().couponAdjust).decode('unicode-escape')