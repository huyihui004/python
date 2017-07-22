#!/usr/bin/env python
#coding=utf-8
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
'''
'''
n = int(raw_input('请输入分数：'))
if n >= 90:
    print('分数得分为A')
elif 60 <= n <= 89:
    print('分数得分为B')
else:
    print('分数得分为C')
'''

def k(x):
    if x in range(60):
        print('C')
    elif x in range(60,90):
        print('B')
    else:
        print('A')
score = int(raw_input('输入分数:\n'))
k(score)