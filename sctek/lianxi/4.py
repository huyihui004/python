#!/usr/bin/env python
#coding=utf-8

def Date(y,m,d):
    #平年
    x1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    #闰年
    x2 = [31,29,31,30,31,30,31,31,30,31,30,31]
    n=0
    for i in range(1,m):
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            n += x1[i]
        else:
            n += x2[i]
    date = n + d
    print "这一天是第%s天" % date

y = int(raw_input('请输入年：'))
m = int(raw_input('请输入月：'))
d = int(raw_input('请输入日：'))

Date(y,m,d)
