#!/usr/bin/env python
#coding=utf-8
'''
#题目：学习使用auto定义变量的用法。
#43
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()
#45
a=0
for i in range(1,101):
    a += i
print a
#46
print "如果输入的数字小于 50，程序将停止运行"
while 1:
    n = int(raw_input("输入一个数："))
    print "次数的平方数是%s" % n**2
    if (n**2) < 50:
        quit()
'''
#47
def exchange(a, b):
    print('第一个变量 = {}, 第二个变量 = {}'.format(a, b))
    a, b = b, a
    print('第一个变量 = {}, 第二个变量 = {}'.format(a, b))
if __name__ == '__main__':
    x = 1
    y = 8
    exchange(x, y)
