#_*_coding:utf-8_*_
from interface_project.library.scripts import LogDebug
import time
import yaml
from interface_project.globalVar import gl
import os
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":\"1262797\",\"shop_id\":4101315464,\"cashier_id\":\"1196770051\",\"money\":\"100\",\"award_money2\":10,\"reward_money\":\"100\",\"is_diy\":true,\"charge_type\":1,\"remark\":\"beizhu\",\"biz_id\":\"37\",\"recommenderecode2\":9002}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
#payload = r"------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"biz_id\":123455,\"send_notification2\":false,\"cashier_id\":\"1196770051\"}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
'''
biz_location= payload.find('biz_id')
leftstr = payload[:biz_location]
rightstr = payload[biz_location:]

rightdou = rightstr.find(',')
print  leftstr
print rightstr
print 'biz_id\":%d%s'%(123455,rightstr[rightdou:])
'''
def replacePayload(old,field,val):
    field_location = old.find(field)
    if field_location != -1:
        leftstr = old[:field_location]
        rightstr = old[field_location:]
        rightdou = rightstr.find(',')
        LogDebug().info('查找字段:%s'%field)
        ret = r'%s%s":%d%s' % (leftstr,field,int(val), rightstr[rightdou:])
        LogDebug().info('字段找到并替换:%s'%ret)
        return ret
    else:
        LogDebug().error('%s:字段未找到.'%field)
        return old



data = {"cno":"1262797","shop_id":4101315464,"cashier_id":"1196770051","money":"100","award_money2":10,"reward_money":"100","is_diy":True,"charge_type":1,"remark":"beizhu","recommenderecode2":9002,"biz_id":"37"}


class tmpClass(object):
    def __init__(self):
        self.configPath =  gl.dataScenarioPath
        self.yamlPath = os.path.join(self.configPath,'ChargeAndDeal.yaml')


    def rndTimeStr(self):
        curTimeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()).encode('utf-8'))
        return curTimeStr.decode('utf-8')

    def writeYmal(self,data):
        fp = open(self.yamlPath,'a')
        yaml.dump(data,fp)

    def getYamlfield(self):
        f = open(self.yamlPath,'r')
        cont = f.read()
        ret = yaml.load(cont)
        return ret

if __name__=="__main__":
    #a = replacePayload(payload,'biz_id',456789)
    #print a
    #tmpClass().writeYmal(data)
    print tmpClass().getYamlfield()