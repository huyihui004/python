#!/usr/bin/env python
#__*__coding:utf-8__*__
#Author:Jason Zhang

import re
import requests
from lxml import etree

class Luoo():
    def __init__(self):
        self.base_url = "http://www.luoo.net/tag/?p="
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        #self.page = 1


    def send_request(self,url):
        html = requests.get(url,headers=self.headers).content
        #print("[INFO] : 正在抓取%d 页.." % self.page)
        #self.page += 1
        return html

    def load_song(self,html):
        html_obj = self.send_request(html)
        url = "http://mp3-cdn2.luoo.net/low/luoo/radio"
        html_obj1 = etree.HTML(html_obj)
        qi = html_obj1.xpath('//span[@class="vol-number rounded"]')[0].text
        #//a[@class="trackname btn-play"]
        print(qi)
        name_list = html_obj1.xpath('//a[@class="trackname btn-play"]')
        #print(name_list)
        l = len(name_list)
        for i in range(1,l):
            full_url = url + str(qi) + "/" + str(i) + ".mp3"
            if i <10:
                full_url = url+str(qi)+"/"+"0"+str(i)+".mp3"
            #//a[@class="trackname btn-play"]
            file_name = html_obj1.xpath('//a[@class="trackname btn-play"]')[i-1].text+".mp3"
            #file_name = full_url[-10:]
            pattern = re.compile(r'(.*?\s)?')
            geming = pattern.sub('',file_name,1)
            # print(geming)
            response = self.send_request(full_url)
            #print(type(response))
            #print(file_name)
            self.writer_data(response,geming)

    def writer_data(self,response,name):
        #print(response)
        #print(name)
        print("[INFO]: 正在保存 %s " % name)
        with open("music/%s"%name,'wb') as f:
            f.write(response)

    def load_page(self,html):
        html_obj = etree.HTML(html)
        link_list = html_obj.xpath('//div[@class="meta rounded clearfix"]/a/@href')
        # print(link_list)
        for i in link_list:
            print(i)
            self.load_song(i)
        if html_obj.xpath('//a[@class="next disabled"]/@href'):
            return False
        next_link = html_obj.xpath('//a[@class="next"]/@href')[0]
        return str(next_link)

    def start_work(self):
        html = self.send_request(self.base_url)
        a=0
        while a<15:
            next_link = self.load_page(html)
            if not next_link:
                break
            html_obj = self.send_request(next_link)
            #print(html_obj)
            a+=1
        print("[INFO] 谢谢使用，再见！")
        #num = input("请输入你要下载的期刊号")


if __name__ == '__main__':
    luoo = Luoo()
    luoo.start_work()


