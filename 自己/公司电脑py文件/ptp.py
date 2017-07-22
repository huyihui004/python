#!/usr/bin/env python
#coding=utf-8
import urllib
import  re
#import request
def getHtml(url):
      f1=urllib.urlopen(url)
      f2=f1.read()
      return f2


def getimg(html):
      reg=r'src="(.*\.jpg)"'
      imgre=re.compile(reg)
      imglist=re.findall(imgre,html)
      print imglist
      x=0
      for imgurl in imglist:
            a=imgurl.split(':')
            b=a[0]
            if b == "http":
                  urllib.urlretrieve(imgurl,'%s.jpg' % x)
                  x+=1
#print getHtml("http://tieba.baidu.com/p/4705406787")
html=getHtml("http://wwww.ivsky.com/")
getimg(html)