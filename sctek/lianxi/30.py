#!/usr/bin/env python
#coding=utf-8
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
'''
a = raw_input('输入一个五位数：')
p = list(a)
if p[0] == p[-1] and p[1] == p[-2]:
    print "%s此数是回文数" % a
else:
    print "%s此数不是回文数" % a
'''

#最简单
a = raw_input("输入一串数字: ")
b = a[::-1]
if a == b:
    print("%s 是回文"% a)
else:
    print("%s 不是回文"% a)
