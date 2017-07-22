#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="huyihui004"    #用户名
mail_pass="123456"   #口令

sender = 'huyihui004@163.com'
receivers = ['704252929@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = '请问你收到邮件了吗'

msg = MIMEText('运维工程师', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'huyihui004<huyihui004@163.com>'
msg['To'] = '704252929@qq.com'

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"