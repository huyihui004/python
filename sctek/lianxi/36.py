#!/usr/bin/python
#coding:utf-8
'''
题目：求100之内的素数。
'''
import math

for i in range(1,100):
    if i > 1:
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            print i