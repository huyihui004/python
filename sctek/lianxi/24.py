#!/usr/bin/env python
#coding=utf-8
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''
'''
def Num(n):
    x = 2
    y = 1
    s = 0
    for i in range(1,n+1):
        s += x / y
        t = x
        x += y
        y = t
    print s
Num(20)
'''
sum = 0
a, b = 1, 2
for i in range(1, 21):
    sum += b / a
    a, b = b, a + b
print(sum)