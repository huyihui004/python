#!/usr/bin/python
#coding:utf-8
#题目：打印出杨辉三角形（要求打印出10行如下图）。

n =10
def lst(i,j):
    if i==j or j==1:
        return 1
    else:
        return lst(i-1,j-1) + lst(i-1,j)
for i in range(1,n+1):
    for j in range(1,i+1):
        print lst(i,j),
    print