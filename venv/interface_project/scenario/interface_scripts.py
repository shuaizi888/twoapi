#_*_coding:utf-8_*_
import unittest
from interface_project.interface import charge,credit,Deal,grade,manage,user
from interface_project.interface.charge import charge_today,charge_receipt,charge_change,charge_rule,charge_view,pos_chargedetail
from interface_project.interface.Deal import consumeToday,deal_getpaytype,deal_rollback,deal_sendnotification
from interface_project.interface.grade import grade_rule
from interface_project.interface.credit import credit_change,credit_exchange,credit_rule
from interface_project.interface.manage import cashier_list
from interface_project.interface.user import user_account
from interface_project.library import scripts

'''
'''
class InterfaceTest(unittest.TestCase):
    '''点评微生活－API单接口'''
    def setUp(self):
        pass
    def tearDown(self):
        pass

    #---------------------------------------charge START------------------------------------#
    def testChargetoday(self):
        '''储值模块/charge/today'''
        today = charge_today.ChargeClass()
        #断言
        self.assertEqual(today.chargeToday['errcode'],0,today.chargeToday['errmsg']) #断言 /charge/today

    def testChargeReceipt(self):
        '''储值模块/charge/receipt'''
        receipt = charge_receipt.ChargeClass()
        #断言
        self.assertEqual(receipt.chargeReceipt['errcode'], 0, receipt.chargeReceipt['errmsg'])  # 断言/charge/receipt

    def testChargeChange(self):
        '''储值模块/charge/change'''
        change = charge_change.ChargeClass()
        #断言
        self.assertEqual(change.chargeChange['errcode'], 0, change.chargeChange['errmsg']) #断言/charge/change


    def testChargeRule(self):
        '''储值模块/charge/rule'''
        rule = charge_rule.ChargeClass()
        #断言
        self.assertEqual(rule.chargeRule['errcode'],0,rule.chargeRule['errmsg']) #断言/charge/rule


    def testChargeView(self):
        '''储值模块/charge/view'''
        view = charge_view.ChargeClass()
        #断言
        self.assertEqual(view.chargeView['errcode'],0,view.chargeView['errmsg']) #断言/charge/view

    def testPosChargedetail(self):
        '''储值模块/pos/chargedetail'''
        pos = pos_chargedetail.ChargeClass()
        #断言
        self.assertEqual(pos.posChargeDetail['errcode'],0,pos.posChargeDetail['errmsg']) #断言pos/chargedetail

    #--------------------------------------Deal START---------------------------------------#
    def testDealconsumetoday(self):
        '''交易模块/consume/today'''
        today = consumeToday.DealClass()
        #断言
        self.assertEqual(today.consumeToday['errcode'],0,today.consumeToday['errmsg']) #断言consume/today

    def testDealgetpaytype(self):
        '''交易模块/deal/getpaytype'''
        paytype = deal_getpaytype.DealClass()
        #断言
        self.assertEqual(paytype.dealGetpaytype['errcode'],0,paytype.dealGetpaytype['errmsg']) #断言deal/getpaytype

    def testDealsendnotification(self):
        '''交易模块/deal/sendnotification'''
        sendnot = deal_sendnotification.DealClass()
        #断言
        self.assertEqual(sendnot.dealSendnotification['errcode'],0,sendnot.dealSendnotification['errmsg']) #断言/deal/sendnotification

    #----------------------------------------Grade START---------------------------------------#
    #等级接口
    def testGraderule(self):
        '''等级接口/grade/rule'''
        rule = grade_rule.DealClass()
        #断言
        self.assertEqual(rule.gradeRule['errcode'],0,rule.gradeRule['errmsg']) #断言/grade/rule

    #-----------------------------------------Credit START--------------------------------------#
    def testCreditchange(self):
        '''积分接口:手工调整积分/credit/change'''
        change = credit_change.DealClass()
        biz_id = scripts.rndTimeStr()
        change.payload = scripts.replacePayload(change.payload,'biz_id',biz_id)

        #断言
        self.assertEqual(change.creditChange['errcode'],0,change.creditChange['errmsg']) #断言/credit/change


    def testCreditrule(self):
        '''积分接口:看积分设置/credit/rule 查'''
        rule = credit_rule.DealClass()

        #断言
        self.assertEqual(rule.creditRule['errcode'],0,rule.creditRule['errmsg']) #断言/credit/rule

    def testCreditexchange(self):
        '''积分接口:积分换礼/credit/exchange'''
        exchange = credit_exchange.DealClass()
        biz_id = scripts.rndTimeStr()
        exchange.payload = scripts.replacePayload(exchange.payload,'biz_id',biz_id)

        #断言
        self.assertEqual(exchange.creditExchange['errcode'],0,exchange.creditExchange['errmsg']) #断言/credit/exchange

    #------------------------------------------Manage START----------------------------------#
    def testCashierlist(self):
        '''商家接口:获取收银员列表/cashier/list'''
        cashier = cashier_list.DealClass()

        #断言
        self.assertEqual(cashier.cashierList['errcode'],0,cashier.cashierList['errmsg']) #断言cashier/list

    #-----------------------------------------------------------------------------------------#
    def testUseraccount(self):
        '''用户接口:获取用户账户信息/user/account'''
        account = user_account.DealClass()

        #断言
        self.assertEqual(account.userAccount['errcode'],0,account.userAccount['errmsg']) #断言/user/account









if __name__=="__main__":
    '''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(InterfaceTest.testInterfaceCharge))
    '''
    unittest.main()