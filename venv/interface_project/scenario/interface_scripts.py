#_*_coding:utf-8_*_
import unittest
from interface_project.interface import charge,credit,Deal,grade,manage,user
from interface_project.interface.charge import charge_today,charge_receipt,charge_change,charge_rule,charge_view,pos_chargedetail

class InterfaceTest(unittest.TestCase):
    '''点评微生活－API单接口'''
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testChargetoday(self):
        '''交易模块/charge/today'''
        today = charge_today.ChargeClass()
        #断言
        self.assertEqual(today.chargeToday['errcode'],0,today.chargeToday['errmsg']) #断言 /charge/today

    def testChargeReceipt(self):
        '''交易模块/charge/receipt'''
        receipt = charge_receipt.ChargeClass()
        #断言
        self.assertEqual(receipt.chargeReceipt['errcode'], 0, receipt.chargeReceipt['errmsg'])  # 断言/charge/receipt

    def testChargeChange(self):
        '''交易模块/charge/change'''
        change = charge_change.ChargeClass()
        #断言
        self.assertEqual(change.chargeChange['errcode'], 0, change.chargeChange['errmsg']) #断言/charge/change


    def testChargeRule(self):
        '''交易模块/charge/rule'''
        rule = charge_rule.ChargeClass()
        #断言
        self.assertEqual(rule.chargeRule['errcode'],0,rule.chargeRule['errmsg']) #断言/charge/rule


    def testChargeView(self):
        '''交易模块/charge/view'''
        view = charge_view.ChargeClass()
        #断言
        self.assertEqual(view.chargeView['errcode'],0,view.chargeView['errmsg']) #断言/charge/view

    def testPosChargedetail(self):
        '''交易模块pos/chargedetail'''
        pos = pos_chargedetail.ChargeClass()
        #断言
        self.assertEqual(pos.posChargeDetail['errcode'],0,pos.posChargeDetail['errmsg']) #断言pos/chargedetail



if __name__=="__main__":
    '''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(InterfaceTest.testInterfaceCharge))
    '''
    unittest.main()