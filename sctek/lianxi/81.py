#!/usr/bin/env python
#coding=utf-8

#题目：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

a = 809
for i in range(10,100):
    b = i * a + 1
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print b,'/',i,' = 809 * ',i,' + ', b % i


'''
if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n
'''

def f8to10(num):
    print "8进制数：", num
    l = str(num)
    length = len(l)
    sum = 0
    for i in range(length):
        sum += 8 ** i * int(l[length-1-i])
    print "转成10进制数为：",sum

f8to10(122)