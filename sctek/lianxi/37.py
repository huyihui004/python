#!/usr/bin/env python
#coding=utf-8
'''
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
'''
'''
print('请输入10个数')
L = []
for i in range(10):
    L.append(raw_input('输入一个数字：'))
L.sort()
print L
'''

n = 0
S = []
T = []
for num in range(1,11):
    a = int(input("输入: "))
    S.append(a)
for n in range(1,11):
    b = min(S)
    T.append(b)
    S.remove(b)
print T