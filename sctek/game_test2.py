#!/usr/bin/env python
#coding=utf-8

import random

s = int(random.uniform(1,10))
print(s)
m = int(input('输入整数:'))
while True:
    if m > s:
        print('大了')
        m = int(input('输入整数:'))
    if m < s:
        print('小了')
        m = int(input('输入整数:'))
    if m == s:
        print('OK')
        break;