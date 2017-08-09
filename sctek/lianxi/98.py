#!/usr/bin/env python
#coding=utf-8

if __name__ == '__main__':
    fp = open('huyihui.txt','w+')
    p = raw_input('请输入字符串：\n')
    string = p.upper()
    fp.write(string)
    fp = open('huyihui.txt','r')
    print fp.read()
    fp.close()
