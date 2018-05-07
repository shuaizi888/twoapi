#_*_coding:utf-8_*_
import unittest
from interface_project.scenario.scenario_scripts import ScenarioTest
from interface_project.scenario.interface_scripts import InterfaceTest
import os,time,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN
from interface_project.library.emailstmp import EmailClass


if __name__=="__main__":
    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(InterfaceTest),unittest.TestLoader().loadTestsFromTestCase(ScenarioTest)]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yhleng"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()

    #发送测试报告To Email
    EmailClass().send
