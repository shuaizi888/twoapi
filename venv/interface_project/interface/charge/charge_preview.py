#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json

class ChargeClass(object):

    url = 'http://api.beta.acewill.net/charge/preview'
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":\"1262797\",\"shop_id\":4101315464,\"cashier_id\":\"1196770051\",\"money\":\"100\",\"award_money2\":10,\"reward_money\":\"100\",\"is_diy\":true,\"charge_type\":1,\"remark\":\"beizhu\",\"recommenderecode2\":9002,\"biz_id\":\"37\"}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "6eb8950f-4839-3857-15e9-91a14c7e1663"
    }

    def __init__(self):
        pass


    #储值预览
    @property
    def chargePreview(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        return res.json()


if __name__=="__main__":
    print ChargeClass().chargePreview()