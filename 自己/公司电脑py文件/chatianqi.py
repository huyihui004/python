#!/usr/bin/env python
#coding=utf-8

import urllib2
import re
import city

City=raw_input(u'请输入城市：')
cityid=city.city[City]
URL="http://www.weather.com.cn/data/cityinfo/%s.html" %(cityid)
urlopen=urllib2.urlopen(URL)
urlhtml=urlopen.read()
reg=re.compile('"cityid":".*?","temp1":"(.*?)","temp2":"(.*?)","weather":"(.*?)"',re.S)
Weather=re.findall(reg,urlhtml)
w=list(Weather[0])
print '%s城市天气预报：%s~%s,%s' %(City,w[0],w[1],w[2])