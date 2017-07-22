#!/usr/bin/env python
#coding=utf-8
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
'''
p = raw_input('请输入五个字符：')
L = list(p)
L.reverse()
for i in range(len(L)):
    print(L[i])
'''

def output(s,l):
    if l==0:
       return
    print (s[l-1])
    output(s,l-1)

s = raw_input('Input a string:')
l = len(s)
output(s,l)