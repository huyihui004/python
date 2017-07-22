#!/usr/bin/env python
#coding=utf-8
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''
'''
f1 = 1
f2 = 1
for i in range(1,36):
    print '%12ld %12ld' % (f1,f2),
    if (i % 3) == 0:
        print ''
    f1 = f1 + f2
    f2 = f1 + f2
'''
'''
#递归做，非常慢。计算n=36就要大概七八秒吧
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print fib(36)
'''
#运算很快
def rabbit(num):
    f1 = 1
    # 第一个月为1
    f2 = 1
    # 第二个月为1
    if num == 1 or num == 2:
        return 1
    else:
        for i in xrange(num-1):
            f1,f2 = f2,f1+f2
    return f1

# 第三十六月兔子数量
print rabbit(36)