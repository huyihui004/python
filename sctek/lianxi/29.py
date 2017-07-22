#!/usr/bin/env python
#coding=utf-8
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。
'''
p = raw_input("请输入不多于5位的正整数：")

print "它是%s位数" % len(p)
L = list(p)
a = []
L.reverse()
for i in L:
    a.append(i)
print a
