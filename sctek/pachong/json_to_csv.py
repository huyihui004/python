#!/usr/bin/env python
#__*__coding:utf-8__*__
#Author:Jason Zhang
import csv
import json
import sys

json_file = open("lagou_info.json","r")
content_list= json.load(json_file)

csv_file = open("lagou_csv.csv","w",newline='')
#创建csv文件读写对象，之后的读写操作就是对csv文件对象操作
csv_writer = csv.writer(csv_file)

head_list = content_list[0].keys()
data_list = [content.values() for content in content_list]

csv_writer.writerow(head_list)
csv_writer.writerows(data_list)

csv_file.close()
json_file.close()