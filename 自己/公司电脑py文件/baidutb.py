#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import urllib2
import re

class BDTB:
    baseUrl = 'http://tieba.baidu.com/p/3738774251?see_lz=1&pn='
    #源代码
    def getPage(self,pageNum):
        try:
            url = self.baseUrl+str(pageNum)
            request = urllib2.Request(url) #构造对象
            response = urllib2.urlopen(request).read()
            #print response
            return response
        except Exception,e:
            print e

    #匹配总页数
    def Total(self,pageNum):
        html = self.getPage(pageNum)
        reg = re.compile(r'"total_page":(.*?)}',re.S)
        items = re.findall(reg,html)
        return items[0]

    #匹配标题
    def Title(self,pageNum):
        html = self.getPage(pageNum)#调用获取源码
        reg = re.compile(r'title="【原创】(.*?)"')#提高效率
        items = re.findall(reg,html)
        print items[0].decode('UTF-8').encode('GBK')
        for item in items:
            f = open('text1.txt','w')
            f.write('标题'+'\t'+item)
            f.close()
        return items
        print items[0].decode('UTF-8').encode('GBK')

    #匹配正文
    def Text(self,pageNum):
        html = self.getPage(pageNum)
        reg = re.compile(r'class="d_post_content j_d_post_content ">            (.*?)</div><br>',re.S)
        req = re.findall(reg,html)
        #print req[0]
        for i in req:
            removeAddr = re.compile('<a.*?>|</a>')
            removeaddr = re.compile('<img.*?>')
            removeadd = re.compile('http.*?.html')
            i = re.sub(removeAddr,"",i)#替换
            i = re.sub(removeaddr,"",i)#替换
            i = re.sub(removeadd,"",i)#替换
            i = i.replace('<br>','')
            f = open('text1.txt','a') #追加模式
            f.write('\n\n'+i)
            f.close()
        #print i.decode('UTF-8').encode('GBK')


try:
    bdtb = BDTB()
    bdtb.Total(1)
    for i in range(1,int(bdtb.Total(1))+1):
        bdtb.getPage(i)
        bdtb.Title(i)
        bdtb.Text(i)
except Exception,e:
    print e