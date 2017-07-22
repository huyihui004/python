#!/usr/bin/env python
#coding=utf-8

'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''

def Number(n):
    if n==1 or n==2:
        return 1
    return Number(n-1)+Number(n-2)

m = int(raw_input('输出了第几个斐波那契数列：'))
print Number(m)