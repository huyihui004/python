#!/usr/bin/env python
#coding=utf-8

#题目：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数。
#程序分析：999999 / 13 = 76923。

'''
b=input('input a number:\n')

a=9
n=1
while (1):
    if a%b==0:
        break
    else:
        a=a*10+9
        n=n+1
print '%d 个 9 除于 %d 为整数' % (n,b)
'''


if __name__ == '__main__':
    zi = int(raw_input('输入一个数字:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print '%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum)
    r = sum / zi
    print '%d / %d = %d' % (sum,zi,r)