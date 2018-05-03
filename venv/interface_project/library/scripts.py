#_*_coding:utf-8_*_
from log import LogDebug
import time
import yaml
'''
替换，post数据中的biz_id
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


'''
#日期时间串
'''
def rndTimeStr():
    curTimeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()).encode('utf-8'))
    LogDebug().info('生成日期时间串%s'%curTimeStr)
    return curTimeStr.decode('utf-8')

'''
写yaml内容
'''
def writeYmal(yamlPath,data):
    fp = open(yamlPath,'w')
    yaml.dump(data,fp)
    fp.close()



'''
读yaml文件
'''
def getYamlfield(yamlpath):
    f = open(yamlpath,'r')
    cont = f.read()
    ret = yaml.load(cont)
    f.close()
    return ret

'''
更新接口测试数据
'''
def loadTestData(payload):
    left_location = payload.find('{')
    right_location = payload.rfind('}')

    leftstr = payload[:left_location]
    rightstr = payload[right_location+1:]

    newPayload = leftstr + json.dumps(payload2) + rightstr
    return newPayload

