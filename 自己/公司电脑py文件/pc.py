#!/usr/bin/env python
#coding=utf-8
#jianghu
#20160929

import  requests
import re
import time
from email.mime.text import MIMEText
import smtplib
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
class Listen_Web():
    def __init__(self):
        self.SMTPserver = 'smtp.139.com'
        self.MailUser = '13794521695@163.com'
        self.MailPassword = '14683245132'
        self.Mailcli = ['704213848@qq.com','121874900@qq.com']
        self.Total_List = ["CCTV-2财经", "CCTV-9纪录", "CCTV-10科教", "CCTV-11戏曲", "CCTV-14少儿", "CCTV-15音乐", "北京卫视高清", "深圳卫视高清", "广东卫视高清", "东方卫视", "天津卫视", "湖北卫视", "旅游卫视", "安徽卫视", "四川卫视", "重庆卫视", "福建东南卫视", "汕头1", "汕头2", "汕头3", "山东卫视", "辽宁卫视", "山西卫视", "贵州卫视", "云南卫视", "江西卫视", "吉林卫视", "河北卫视", "内蒙古卫视", "甘肃卫视", "青海卫视", "宁夏卫视", "广西卫视", "河南卫视", "西藏卫视", "陕西卫视", "新疆卫视", "中国教育电视台-1", "北京青年", "山东教育", "CCTV-4中文国际", "CCTV-13 News", "CCTV-9 Documentary", "CCTV娱乐 ", "CCTV电影", "湖南国际", "浙江国际", "江苏国际", "北京国际", "天津国际", "上海国际", "重庆国际", "深圳国际", "安徽国际", "泰山电视台", "河南国际", "中国黄河", "广东南方卫视", "海峡卫视", "CCTV戏曲", "CCTV西班牙语", "CCTV法语", "CCTV阿拉伯语", "CCTV俄语", "CCTV-1综合", "CCTV-3综艺", "CCTV-7军事农业", "CCTV-12社会与法", "CCTV-13新闻", "湖南卫视高清", "浙江卫视高清", "江苏卫视高清", "凤凰卫视中文台", "凤凰资讯台", "凤凰香港高清", "卡酷动画", "功夫卫视", "阳光卫视", "莲花卫视", "广东珠江台", "深圳电视剧高清", "深圳都市高清", "高尔夫", "美国中文电视", "人间卫视", "CCTV-1综合超清", "湖南卫视超清", "浙江卫视超清", "江苏卫视超清", "东方卫视超清", "北京卫视超清", "CCTV-9纪录超清", "CCTV-10科教超清", "ChinaTV频道", "CIBN热播剧场", "CIBN骄阳剧场", "CIBN综艺频道", "CIBN古装剧场", "CIBN禅文化频道", "CIBNTEA电竞"]
        self.Error_Dict = {}


    #发送邮件
    def SendMail(self,Local_Time,App_Name,Error_Time):
        me = self.MailUser
        Title = "电视台故障监控报警"
        MailText = '''
        <table border="1">
        <tr>
        <td><h2>故障产生时间{%s}</h2></td>
        </tr>
        </tr>
        <td><h2>故障电视台名称{%s}</h2></td>
        </tr>
        <td><h2>故障总时时长{%s分钟}</h2></td>
        </tr>
        </table>
        ''' %(Local_Time,App_Name,str(Error_Time))
        msg = MIMEText(MailText,_subtype='html',_charset='utf-8')
        msg['Subject'] = Title
        msg['From'] = me
        msg['To'] = ";".join(self.Mailcli)

        Mail = smtplib.SMTP(self.SMTPserver)
        Mail.set_debuglevel(1)
        Mail.login(self.MailUser,self.MailPassword)
        Mail.sendmail(me,self.Mailcli,msg.as_string())
        Mail.close()

    #抓取web数据,并记录
    def Request_Web(self):
        r = requests.get("http://198.255.98.154:8001/support/live/nostreams/channels")
        r.encoding='utf-8'
        Web_Values = r.text
        r.close()
        Web_Values = re.findall('<div>(.*)</div>',Web_Values,re.S)[0].split("\n")
        print Web_Values
        Web_List = []
        for web in range(len(Web_Values)):
            Re_Temp = r'^(.*)\(.*$'
            Values_List = re.findall(Re_Temp,Web_Values[web])

            #将新的错误电视台存储到错误字典中
            if Values_List != [] and Values_List[0] in self.Total_List:
                Web_List.append(Values_List[0])
                if Values_List[0] not in self.Error_Dict.keys():
                    self.Error_Dict['%s' %(Values_List[0])] = time.strftime("%Y-%m-%d %H:%M:%S")

        #对已经正常的错误进行删除
        Temp_List = self.Error_Dict.keys()
        for name in range(len(Temp_List)):
            if Temp_List[name] not in Web_List:
                self.Error_Dict.pop(Temp_List[name])

    #发送报警邮件
    def Check_baoj(self):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        for key in self.Error_Dict.keys():
            Local_Time = time.mktime(time.strptime(self.Error_Dict[key],'%Y-%m-%d %H:%M:%S'))
            System_Time = time.mktime(time.strptime(time.strftime("%Y-%m-%d %H:%M:%S"),'%Y-%m-%d %H:%M:%S'))
            Error_Time = int(System_Time) - int(Local_Time)
            if Error_Time >= 900:
                self.SendMail(self.Error_Dict[key],key,Error_Time / 60)

if __name__ == '__main__':
    main=Listen_Web()
    main.Request_Web()

    '''
    ServerIP = "0.0.0.0"
    ServerPort = int(2600)
    main = Listen_Web()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ServerIP,ServerPort))
    s.listen(1)
    while True:
        try:
            main.Request_Web()
            main.Check_baoj()
            time.sleep(300)
        except:
            continue
    '''