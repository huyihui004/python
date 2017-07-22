#!/usr/bin/env python
#coding=utf-8
'''
题目：输出指定格式的日期。
'''
import time

print time.time()  #1498539133.655
print time.localtime()  #tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1, tm_yday=178, tm_isdst=0
print time.asctime()  #'Tue Jun 27 12:53:50 2017'
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #'2017-06-27 13:00:57'


import datetime

print datetime.date.today() #datetime.date(2017, 6, 27)
print datetime.date.today().strftime('%d/%m/%Y') #'27/06/2017'
print datetime.date(1941, 1, 5) #datetime.date(1941, 1, 5)