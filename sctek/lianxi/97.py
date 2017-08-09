#!/usr/bin/env python
#coding=utf-8

'''
filename = input('输入文件名:\n')
fp = open(filename , "w+")
ch = ''
while '#' not in ch:
    fp.write(ch)
    ch = input('输入字符串:\n')
fp.close()
'''

if __name__ == '__main__':
    from sys import stdout
    filename = raw_input('输入文件名:\n')
    fp = open(filename,"w")
    ch = raw_input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = raw_input('')
    fp.close()