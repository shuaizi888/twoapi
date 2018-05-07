#_*_coding:utf-8_*_
import requests
from interface_project.base import base_config
import json
from interface_project.library.excel import Excel
from interface_project.globalVar import gl
import os,time
import unittest
import yaml
from interface_project.library import scripts
from interface_project.interface.charge import charge_preview,charge_cancel,charge_commit
from interface_project.interface.Deal import deal_cancel,deal_commit,deal_preview
from interface_project.library import HTMLTESTRunnerCN

'''
点评微生活－API接口场景
'''
class ScenarioTest(unittest.TestCase):#点评微生活API接口
    '''点评微生活－API接口场景'''
    #初始化,setUp每个测试方法,执行一次;如果需要只执行一次使用setUpClass(cls)  需要classmethod修饰

    def setUp(self):
        self.configPath =  gl.configPath
        self.reportPath = gl.reportPath
        self.yamlPath = os.path.join(self.configPath,'config_scenario.yaml')
        self.scenarioRunTable = os.path.join(gl.configPath,'scenario_run_config.xlsx').decode('utf-8')

    '''
    #储值撤销场景:储值预览->储值提交->储值撤销
    '''
    def testChargeAndCancel(self):
        '''储值撤销场景:储值预览->储值提交->储值撤销'''
        yamlConfigPath = os.path.join(gl.dataScenarioPath,'ChargeAndCancel.yaml')
        scanorio_data = scripts.getYamlfield(yamlConfigPath)

        all_row_list = Excel(self.scenarioRunTable).getExcelDataByName()
        for row in all_row_list:
            #print row
            if str(row['Flag']).strip() =='Y' and str(row['PrimaryKey']).strip()=='chargeAndCancel': #执行标志
                preview = charge_preview.ChargeClass() #交易预览
                biz_id_01 = scripts.rndTimeStr()
                scanorio_data['ChargePreview']['biz_id'] = biz_id_01
                '''--------------------------split line----------------------'''
                preview.payload = scripts.MultipartFormData(scanorio_data['ChargePreview'])
                '''--------------------------split line----------------------'''
                commit = charge_commit.ChargeClass() #交易提交
                scanorio_data['ChargeCommit']['biz_id'] = biz_id_01
                commit.payload = scripts.MultipartFormData(scanorio_data['ChargeCommit']) #更新接口数据
                '''--------------------------split line----------------------'''
                cancel = charge_cancel.ChargeClass() #交易撤销
                scanorio_data['ChargeCancel']['biz_id'] = biz_id_01
                cancel.payload = scripts.MultipartFormData(scanorio_data['ChargeCancel']) #更新接口数据
                '''--------------------------split line----------------------'''

                self.assertEquals(preview.chargePreview['errcode'],0,preview.chargePreview['errmsg']) #交易预览断言
                self.assertEquals(commit.chargeCommit['errcode'], 0,commit.chargeCommit['errmsg']) #交易提交断言
                self.assertEquals(cancel.chargeCancel['errcode'], 0,cancel.chargeCancel['errmsg']) #交易撤销断言

    '''
    #自定义充值并消费储值业务场景:储值预览->储值提交->交易预览->交易提交->交易撤销
    '''
    def testChargeAndDeal(self):
        '''自定义充值并消费储值业务场景:储值预览->储值提交->交易预览->交易提交->交易撤销'''
        yamlConfigPath = os.path.join(gl.dataScenarioPath,'ChargeAndDeal.yaml')
        scanorio_data = scripts.getYamlfield(yamlConfigPath)


        all_row_list = Excel(self.scenarioRunTable).getExcelDataByName()
        for row in all_row_list:
            # print row
            if str(row['Flag']).strip() == 'Y' and str(row['PrimaryKey']).strip() == 'chargeAndDeal':  # 执行标志
                #场景顺序执行
                preview = charge_preview.ChargeClass()  # 储值预览
                biz_id_01 = scripts.rndTimeStr()
                #----修改数据----
                scanorio_data['ChargePreview']['biz_id'] = biz_id_01
                preview.payload = scripts.MultipartFormData(scanorio_data['ChargePreview']) #生成新数据
                '''--------------------------split line----------------------'''
                commit = charge_commit.ChargeClass()  # 储值提交
                scanorio_data['ChargeCommit']['biz_id'] = biz_id_01
                commit.payload = scripts.MultipartFormData(scanorio_data['ChargeCommit']) #生成新提交biz_id
                '''--------------------------split line----------------------'''
                dealPreview = deal_preview.DealClass() #消费预览
                biz_id_03 = scripts.rndTimeStr()
                scanorio_data['DealPreview']['biz_id'] = biz_id_03
                dealPreview.payload = scripts.MultipartFormData(scanorio_data['DealPreview'])
                '''--------------------------split line----------------------'''
                dealcommit = deal_commit.DealClass() #消费提交
                scanorio_data['DealCommit']['biz_id'] = biz_id_03
                dealcommit.payload = scripts.MultipartFormData(scanorio_data['DealCommit']) #更新接口数据
                '''--------------------------split line----------------------'''
                dealcancel = deal_cancel.DealClass() #消费取消
                scanorio_data['DealCancel']['biz_id'] = biz_id_03
                dealcancel.payload = scripts.MultipartFormData(scanorio_data['DealCancel']) #更新接口数据
                '''--------------------------split line----------------------'''


                #断言
                self.assertEquals(preview.chargePreview['errcode'], 0,preview.chargePreview['errmsg'])  # 储值预览断言
                self.assertEquals(commit.chargeCommit['errcode'], 0,commit.chargeCommit['errmsg'])  # 储值提交断言
                self.assertEquals(dealPreview.dealPreview['errcode'], 0,dealPreview.dealPreview['errmsg']) #消费预览断言
                self.assertEquals(dealcommit.dealCommit['errcode'], 0,dealcommit.dealCommit['errmsg']) #消费提交断言
                self.assertEquals(dealcancel.dealCancel['errcode'], 0,dealcancel.dealCancel['errmsg']) #消费取消断言

#

if __name__=="__main__":
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
    fp.close()