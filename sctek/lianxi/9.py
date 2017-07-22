#!/usr/bin/env python
#coding=utf-8

import time

l=[1,2,3,4]
for i in range(len(l)):
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print l[i]
    time.sleep(1)  # 暂停一秒输出

