#!/usr/bin/env python
#coding=utf-8

import urllib2
import city
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

City=raw_input(u"请输入城市:")
cityid=city.city.get(City)
if cityid:
    try:
        URL="http://www.weather.com.cn/data/cityinfo/%s.html" %(cityid)
        urlopen=urllib2.urlopen(URL)
        urlhtml=urlopen.read()
        jsonhtml=json.loads(urlhtml).get('weatherinfo')
        Temp1=jsonhtml.get('temp1')
        Temp2=jsonhtml.get('temp2')
        Weath=jsonhtml.get('weather')
        print '天气预报：%s~%s,%s' %(Temp1,Temp2,Weath)
        '''
        #以下是使用re模块实现
        reg=re.compile('"cityid":".*?","temp1":"(.*?)","temp2":"(.*?)","weather":"(.*?)"',re.S)
        Weather=re.findall(reg,urlhtml)
        w=list(Weather[0])
        print '天气预报：%s~%s,%s' %(w[0],w[1],w[2])
        '''
    except:
        print("查询失败")
else:
    print("城市名不存在")