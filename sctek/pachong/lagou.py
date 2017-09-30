#!/usr/bin/env python
# __*__coding:utf-8__*__
# Author:Jason Zhang

import requests
import json
import jsonpath
import time
import random


class LagouSpider(object):
    def __init__(self):
        self.headers = {
            "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json?"
        self.position_name = input("请输入职位名:")
        self.city_name = input("请输入城市名:")
        self.page_num = int(input("请输入爬取的页数:"))
        self.item_list = []
        self.page = 1
        self.proxy_list = [
            {"http": "117.90.1.183:9000"},
            {"http": "114.102.45.112:8118"},
            {"http": "139.129.166.68:3128"},
            {"http": "116.199.2.196:80"},
            {"http": "106.39.160.135:8888"},
            {"http": "11.167.248.228:8080"},
            {"http": "61.172.249.96:80"},
        ]

    def load_page(self):
        params = {
            "px": "default",
            "city":self.city_name,
            "needAddtionalResult":"false",
            "isSchoolJob":"0"
        }
        formdata = {
            "first": "false",
            "pn": self.page,
            "kd": self.position_name,
        }
        proxy = random.choice(self.proxy_list)

        try:
            print ("[INFO] : 正在爬取 %d 页.." % self.page)
            response = requests.post(self.base_url, params=params, data=formdata, headers=self.headers, proxies=proxy)
        except:
            print("[ERROR]: 请求发送失败..")

        json_obj = response.json()
        try:
            result_list = jsonpath.jsonpath(json_obj, "$..result")[0]
            for result in result_list:
                item = {}
                item["companyFullName"] = result["companyFullName"]
                item["positionName"] = result["positionName"]
                item["salary"] = result["salary"]
                item["city"] = result["city"]
                item["district"] = result["district"]
                item["createTime"] = result["createTime"]
                self.item_list.append(item)
        except:
            print("[ERROR]: 数据提取失败..")
            print(proxy)

    def write_page(self):
        json_str = json.dumps(self.item_list)
        with open("lagou_info.json","w") as f:
            f.write(json_str)

    def start_work(self):
        while self.page <= self.page_num:
            self.load_page()
            time.sleep(2)
            self.page += 1
        self.write_page()

if __name__ == '__main__':
    spider = LagouSpider()
    spider.start_work()
