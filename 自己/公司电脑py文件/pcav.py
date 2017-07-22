#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
#根据番号获取磁力链接
def getInfo(pageNum):
    #根据提供的网站取出片名番号更新时间信息
    url = 'https://avmo.pw/cn/star/2jv/page/'+str(pageNum)
    urlopen = urllib2.urlopen(url)
    html = urlopen.read()
    reg = re.compile('<span>(.*?) .*?<br><date>(.*?)</date> / <date>(.*?)</date></span>',re.S)
    Info = re.findall(reg,html)
    #创建文件
    file = open('D:/av.txt','a+')
    file.write('最新番号：\n\n')
    for  j in Info:
        url = 'http://www.cililian.com/main-search.html?kw='+j[1]
        urlopen = urllib2.urlopen(url)
        html = urlopen.read()
        #根据提供的番号过滤出视频大小和对应的URL
        reg = re.compile('<h5 class="item-title"><a href="(.*?)" target="_blank">.*?<td width="100px"><span class="label label-info"><b>(.*?)GB</b></span></td>',re.S)
        info = re.findall(reg,html)
        #取出小于5G中最大的视频所对应的URL
        if info != []:
            number = 0.0
            index = 0
            for i in range(len(info)):
                if (float(info[i][-1]) <= float(5)) and (float(info[i][-1]) > float(number)):
                    number = float(info[i][-1])
                    index = i
            url = 'http://www.cililian.com' + info[index][0]
            urlopen = urllib2.urlopen(url)
            html = urlopen.read()
            #取出磁力链接
            reg = re.compile('.*readonly>(.*?)</textarea>.*',re.S)
            info = re.findall(reg,html)
            size = str(number) + 'GB'
            print size
            cili = info[0]
            #把所有信息写入文本文档
            file.write('%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n\n' %('片名', j[0], '番号', j[1],'更新时间',j[2],'大小',size,'磁力链接',cili))
            print cili.decode('UTF-8').encode('GBK')
    file.close()
for i in range(4,10):
    getInfo(i)


