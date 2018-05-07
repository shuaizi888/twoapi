#_*_coding:utf-8_*_
import unittest
from interface_project.interface import charge,credit,Deal,grade,manage,user
from interface_project.interface.charge import charge_today,charge_receipt,charge_change,charge_rule,charge_view,pos_chargedetail
from interface_project.interface.Deal import consumeToday,deal_getpaytype,deal_rollback,deal_sendnotification
from interface_project.interface.grade import grade_rule
from interface_project.interface.credit import credit_change,credit_exchange,credit_rule
from interface_project.interface.manage import cashier_list
from interface_project.interface.user import user_account,user_grade,user_getinfo,user_uopencard
from interface_project.interface.user import user_checkcard,user_cardinfo,user_edit,user_ugetinfo
from interface_project.interface.product import product_list,product_listbyuser
from interface_project.interface.tag import tag_touser,tag_listusertags
from interface_project.interface.activity import activity_getuserthumbuplog,activity_list
from interface_project.interface.coupon import coupon_adjust,coupon_detail,coupon_gift,coupon_list,coupon_send,coupon_verification

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
        '''储值模块:当日储值统计/charge/today'''
        today = charge_today.ChargeClass()
        #断言
        self.assertEqual(today.chargeToday['errcode'],0,today.chargeToday['errmsg']) #断言 /charge/today

    def testChargeReceipt(self):
        '''储值模块:储值是否开发票/charge/receipt'''
        receipt = charge_receipt.ChargeClass()
        #断言
        self.assertEqual(receipt.chargeReceipt['errcode'], 0, receipt.chargeReceipt['errmsg'])  # 断言/charge/receipt

    def testChargeChange(self):
        '''储值模块:储值调整/charge/change'''
        change = charge_change.ChargeClass()
        #断言
        self.assertEqual(change.chargeChange['errcode'], 0, change.chargeChange['errmsg']) #断言/charge/change


    def testChargeRule(self):
        '''储值模块:查看门店储值规则设置/charge/rule'''
        rule = charge_rule.ChargeClass()
        #断言
        self.assertEqual(rule.chargeRule['errcode'],0,rule.chargeRule['errmsg']) #断言/charge/rule


    def testChargeView(self):
        '''储值模块:储值记录详情/charge/view'''
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
        '''交易模块:获取交易/储值支付方式/deal/getpaytype'''
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
        '''等级接口:查看等级设置/grade/rule'''
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


    def testUsergrade(self):
        '''用户接口:/user/grade'''
        grade = user_grade.DealClass()

        #断言
        self.assertEqual(grade.userGrade['errcode'],0,grade.userGrade['errmsg']) #断言


    def testUsergetinfo(self):
        '''用户接口:获取微信用户账户信息/user/getinfo'''
        info = user_getinfo.DealClass()

        #断言
        self.assertEqual(info.userGetinfo['errcode'],0,info.userGetinfo['errmsg']) #断言


    def testUsercheckcard(self):
        '''用户接口:验证实体卡信息/user/checkcard'''
        check = user_checkcard.DealClass()

        #断言
        self.assertEqual(check.userCheckcard['errcode'],0,check.userCheckcard['errmsg']) #断言

    def testUsercardinfo(self):
        '''用户接口:/user/cardinfo'''
        cardinfo = user_cardinfo.DealClass()

        #断言
        self.assertEqual(cardinfo.userCardinfo['errcode'],0,cardinfo.userCardinfo['errmsg']) #断言

    def testUseredit(self):
        '''用户接口:修改会员信息/user/edit'''
        userinfo = user_edit.DealClass()

        #断言
        self.assertEqual(userinfo.userEdit['errcode'],0,userinfo.userEdit['errmsg']) #断言


    def testUserugetinfo(self):
        '''用户接口:unionid查询用户/user/ugetinfo'''
        getinfo = user_ugetinfo.DealClass()

        #断言
        self.assertEqual(getinfo.userUgetinfo['errcode'],0,getinfo.userUgetinfo['errmsg']) #断言

    def testUseruopencard(self):
        '''用户接口:unionid开卡/user/uopencard'''
        opencard = user_uopencard.DealClass()
        unionidrnd = scripts.rndTimeStr()

        opencard.payload = scripts.replacePayload(opencard.payload,'unionid',unionidrnd)

        #断言
        self.assertEqual(opencard.userUopencard['errcode'],0,opencard.userUopencard['errmsg']) #断言


    #----------------------------------------Product START------------------------------------#
    def testProductlist(self):
        '''菜品接口:商家点菜记录列表/product/list'''
        product = product_list.DealClass()

        #断言
        self.assertEqual(product.productList['errcode'],0,product.productList['errmsg']) #断言


    def testProductlistbyuser(self):
        '''菜品接口:查询会员点菜记录/product/listbyuser'''
        productuser = product_listbyuser.DealClass()

        #断言
        self.assertEqual(productuser.productListbyuser['errcode'],0,productuser.productListbyuser['errmsg'])#断言

    #-------------------------------------------------Tag START---------------------------------#

    def testTaglistusertags(self):
        '''用户接口:用户标签列表/tag/listusertags'''
        taglist = tag_listusertags.DealClass()

        #断言
        self.assertEqual(taglist.tagListusertags['errcode'],0,taglist.tagListusertags['errmsg']) #断言

    def testTagtouser(self):
        '''用户接口:用户增加标签/tag/touser'''
        touser = tag_touser.DealClass()

        #断言
        self.assertEqual(touser.tagTouser['errcode'],0,touser.tagTouser['errmsg']) #断言tag/touser


    #---------------------------------------Activity START-------------------------------------------#
    def testActivityGetuserthumbuplog(self):
        '''活动接口:查询用户参与的集赞活动/activity/getuserthumbuplog'''
        thumbuplog = activity_getuserthumbuplog.ChargeClass()

        #断言
        self.assertEqual(thumbuplog.activityGetuserthumbuplog['errcode'],0,thumbuplog.activityGetuserthumbuplog['errmsg'])#断言


    def testActivitylist(self):
        '''活动接口:获取活动列表/activity/list'''
        activity = activity_list.ChargeClass()

        #断言
        self.assertEqual(activity.activityList['errcode'],0,activity.activityList['errmsg']) #断言


        #-------------------------------------Coupon START---------------------------------------#
    def testCouponsend(self):
        '''券接口:发券/coupon/send'''
        send = coupon_send.ChargeClass()
        biz_id = scripts.rndTimeStr()

        send.payload = scripts.replacePayload(send.payload,'biz_id',biz_id)

        #断言
        self.assertEqual(send.couponSend['errcode'],0,send.couponSend['errmsg']) #断言

    def testCoupondetail(self):
        '''券接口:券模板详情/coupon/detail'''
        detail = coupon_detail.ChargeClass()

        #断言
        self.assertEqual(detail.couponDetail['errcode'],0,detail.couponDetail['errmsg']) #断言



if __name__=="__main__":
    '''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(InterfaceTest.testInterfaceCharge))
    '''
    unittest.main()