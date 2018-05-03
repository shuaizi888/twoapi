#_*_coding:utf-8_*_

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import time
from interface_project.library import scripts
from interface_project.globalVar import gl

import yaml,os,base64


class EmailClass(object):
    def __init__(self):
        self.curDateTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #当前日期时间
        self.config = scripts.getYamlfield(os.path.join(gl.configPath,'config.yaml')) #配置文件路径
        self.sender = self.config['EMAIL']['Smtp_Sender'] # 从配置文件获取，发件人
        self.receivers = self.config['EMAIL']['Receivers']  # 从配置文件获取，接收人
        self.msg_title = self.config['EMAIL']['Msg_Title'] #从配置文件获取，邮件标题
        self.sender_server = self.config['EMAIL']['Smtp_Server'] #从配置文件获取，发送服务器
        self.From = '自动化测试系统'
        self.To = '微生活测试组'

    '''
    配置邮件内容
    '''
    @property
    def setMailContent(self):
        print self.receivers
        msg = MIMEMultipart()
        msg['From'] = Header(self.From,'utf-8')
        msg['To'] = self.To
        msg['Subject'] = Header('%s%s'%(self.msg_title,self.curDateTime),'utf-8')

        reportfile = os.path.join(gl.reportPath, 'Report.html')
        fp = open(reportfile, 'rb')
        reportHtmlText = fp.read()
        msg.attach(MIMEText(reportHtmlText,'html','utf-8'))

        ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)

        # 附件-文件
        file = MIMEBase(maintype, subtype)
        file.set_payload(reportHtmlText)
        file.add_header('Content-Disposition', 'attachment', filename='Report%s.html'%self.curDateTime)
        encoders.encode_base64(file)
        msg.attach(file)
        fp.close()
        return msg


    '''
    发送电子邮件
    '''
    def sendEmail(self,message):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.sender_server,25)
            smtpObj.login(self.sender,self.config['EMAIL']['Password'])
            smtpObj.sendmail(self.sender,self.receivers , message.as_string())
            smtpObj.quit()
            print "邮件发送成功"
        except smtplib.SMTPException as ex:
            print "Error: 无法发送邮件.%s"%ex


if __name__=="__main__":
    email_class = EmailClass()
    email_class.sendEmail(email_class.setMailContent)

