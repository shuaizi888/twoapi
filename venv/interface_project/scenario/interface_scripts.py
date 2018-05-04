#_*_coding:utf-8_*_
import unittest
from interface_project.interface import charge,credit,Deal,grade,manage,user
from interface_project.interface.charge import charge_today,charge_receipt,charge_change

class InterfaceTest(unittest.TestCase):
    '''单个接口测试-数据无依赖'''
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testChargetoday(self):
        '''交易模块接口/charge/today'''
        today = charge_today.ChargeClass()
        #断言
        self.assertEqual(today.chargeToday['errcode'],0,today.chargeToday['errmsg']) #断言 /charge/today

    def testChargeReceipt(self):
        '''交易模块接口/charge/receipt'''
        receipt = charge_receipt.ChargeClass()
        #断言
        self.assertEqual(receipt.chargeReceipt['errcode'], 0, receipt.chargeReceipt['errmsg'])  # 断言/charge/receipt

    def testChargeChange(self):
        '''交易模块接口/charge/change'''
        change = charge_change.ChargeClass()
        #断言
        self.assertEqual(change.chargeChange['errcode'], 0, change.chargeChange['errmsg']) #断言/charge/change


if __name__=="__main__":
    '''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(InterfaceTest.testInterfaceCharge))
    '''
    unittest.main()