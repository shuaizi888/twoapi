#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json
from interface_project.library.excel import Excel
from interface_project.globalVar import gl
import os,time
import unittest
import yaml
from interface_project.interface.charge import charge_preview,charge_cancel,charge_commit
from interface_project.interface.Deal import deal_cancel,deal_commit,deal_preview
from interface_project.library import HTMLTESTRunnerCN

class ScenarioTest(unittest.TestCase):
    def setUp(self):
        self.configPath =  gl.configPath
        self.reportPath = gl.reportPath
        self.yamlPath = os.path.join(self.configPath,'config_scenario.yaml')
        self.scenarioData = os.path.join(gl.dataScenarioPath,'scenario.xlsx').decode('utf-8')

    #储值撤销场景:储值预览->储值提交->储值撤销
    def testChargeAndCancel(self):
        all_row_list = Excel(self.scenarioData).getExcelDataByName()
        for row in all_row_list:
            #print row
            if str(row['Flag']).strip() =='Y' and str(row['PrimaryKey']).strip()=='chargeAndCancel': #执行标志
                preview = charge_preview.ChargeClass() #交易预览
                commit = charge_commit.ChargeClass() #交易提交
                cancel = charge_cancel.ChargeClass() #交易撤销


                self.assertEquals(preview.chargePreview['errcode'],8008) #交易预览断言
                self.assertEquals(commit.chargeCommit['errcode'], 0) #交易提交断言
                self.assertEquals(cancel.chargeCancel['errcode'], 0) #交易撤销断言


    #自定义充值并消费储值业务场景:储值预览->储值提交->交易预览->交易提交->交易撤销
    def testChargeAndDeal(self):
        all_row_list = Excel(self.scenarioData).getExcelDataByName()
        for row in all_row_list:
            # print row
            if str(row['Flag']).strip() == 'Y' and str(row['PrimaryKey']).strip() == 'chargeAndDeal':  # 执行标志
                preview = charge_preview.ChargeClass()  # 储值预览
                commit = charge_commit.ChargeClass()  # 储值提交
                dealPreview = deal_preview.DealClass() #消费预览
                dealcommit = deal_commit.DealClass() #消费提交
                dealcancel = deal_cancel.DealClass() #消费取消



                self.assertEquals(preview.chargePreview['errcode'], 8009)  # 储值预览断言
                self.assertEquals(commit.chargeCommit['errcode'], 0)  # 储值提交断言
                self.assertEquals(dealPreview.dealPreview['errcode'], 3011) #消费预览断言
                self.assertEquals(dealcommit.dealCommit['errcode'], 3036) #消费提交断言
                self.assertEquals(dealcancel.dealCancel['errcode'], 0) #消费取消断言


class tmpClass(object):
    def __init__(self):
        self.configPath =  gl.configPath
        self.yamlPath = os.path.join(self.configPath,'config_scenario.yaml')


    def rndTimeStr(self):
        curTimeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()).encode('utf-8'))
        return curTimeStr.decode('utf-8')

    def writeYmal(self,data):
        fp = open(self.yamlPath,'a')
        yaml.dump(data,fp)

    def getYamlfield(self,yamlpath):
        f = open(yamlpath,'r')
        cont = f.read()
        ret = yaml.load(cont)
        return ret

if __name__=="__main__":
    #unittest.main()
    #tmpClass().rndTimeStr()
    '''
    tcodePath = os.path.join(gl.dataPath,'t-code')
    yamlPath = os.path.join(os.path.abspath(tcodePath), 'charge_interface.yaml')
    print yamlPath
    print tmpClass().getYamlfield(yamlPath)['payload']
    '''

    suite = unittest.TestSuite()
    tests = [ScenarioTest('testChargeAndCancel'),ScenarioTest('testChargeAndDeal')]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath,'Report.html') #确定生成报告的路径
    #filePath ='F:\\Report.html'

    print filePath

    fp = file(filePath,'wb')

    runner = HTMLTESTRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'详细测试用例结果',    #不传默认为空
        tester=u"yhleng"     #测试人员名字，不传默认为QA
        )
    #运行测试用例
    runner.run(suite)
