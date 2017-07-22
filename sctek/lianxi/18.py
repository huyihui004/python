#!/usr/bin/env python
#coding=utf-8

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''

print "{}".format(1)*8  #此语法是重点
print '%s' % 1 * 8   #效果跟上面一样


a = int(raw_input("a:"))
n = int(raw_input("n:"))
list=[]
for i in range(1,n+1):
    list.append(int("{}".format(a)*i))
s = reduce(lambda x,y:x+y, list)
print list
print "计算和为：",s