#!/usr/bin/env python
#coding=utf-8

while True:
    data = raw_input('请输入要保存的内容：')
    if data == 'no':
        break
    f = open('data.txt','a')
    f.writelines('%s\n' % data)
    f.close()

