#!/usr/bin/env python
#coding=utf-8

print('请输入10个数')
L = []
for i in range(10):
    L.append(raw_input('输入一个数字：'))
L.sort()
print L