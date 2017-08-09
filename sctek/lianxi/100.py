#!/usr/bin/env python
#coding=utf-8

#题目：列表转换为字典。

i = ['a', 'b']
l = [1, 2]
print dict([i,l])



l1=[1,2,3,6,87,3,5]
l2=['aa','bb','cc','dd','ee','ff','aa']
d={}
for index in range(len(l1)):
    d[l1[index]]=l2[index]    # 注意，key 若重复，则新值覆盖旧值
print d