#!/usr/bin/env python
#coding=utf-8

#题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
if __name__ == '__main__':
    fa = open('A.txt','w+')
    a = raw_input('请输入文件A的字符串：\n')
    fa.write(a)
    fa = open('A.txt','r')
    ra = fa.read()
    fa.close()

    fb = open('B.txt','w+')
    b = raw_input('请输入文件B的字符串：\n')
    fb.write(b)
    fb = open('B.txt','r')
    rb = fb.read()
    fb.close()

    fc = open('C.txt','w')
    c = list(ra + rb)
    c.sort()
    print c
    s = ''
    s = s.join(c)
    print s
    fc.write(s)
    fc.close()

'''
if __name__ == '__main__':
    import string
    fp = open('test1.txt')
    a = fp.read()
    fp.close()

    fp = open('test2.txt')
    b = fp.read()
    fp.close()

    fp = open('test3.txt','w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()
'''