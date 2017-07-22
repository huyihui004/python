#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import re



def getHtml(pageNum):
    url = 'http://www.mm131.com/mingxing/520_'+str(pageNum)+'.html'
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    reg = re.compile(r'<a href=\'.*?.html\'><img alt=".*?" src="(.*?)" /></a>',re.S)
    imglist = re.findall(reg,html)[0]
    print imglist
    urllib.urlretrieve(imglist,'D:\Img\%s.jpg' %(pageNum))

try:
    for i in range(3,50):
        getHtml(i)
except Exception,e:
    print e