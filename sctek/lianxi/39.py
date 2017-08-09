#!/usr/bin/env python
#coding=utf-8

#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
list = [1,2,3,4,5,6,8,9,10,11,12,13]
print list
#我将通过插入数字7来加入按照从小到大排列的列表中
n = int(raw_input("插入一个数字："))
#通过for循环来讲数字在列表中定位，然后将数字添加进去就可以了。
for i in range(0,13):
    if n > list[i] and n <= list[i+1]:
        list.insert(i+1,n)
print u"插入数字后的列表为：\n",list