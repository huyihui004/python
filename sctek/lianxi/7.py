#!/usr/bin/env python
#coding=utf-8
'''
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
'''

#PS1:
a = [1,2,3,4]
b = [5,6,7]
for i in range(len(b)):
    a.append(b[i])
print a

#PS2:
a = [1, 2, 3]
b = a[:]
print b