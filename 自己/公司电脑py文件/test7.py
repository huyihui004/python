#!/usr/bin/env python
#coding=utf-8

#coding=utf-8
import time
import os
class Graphical():
    def __init__(self):
        pass

    def Aircraft(self,line):
        Top1 = u'%s◥█▄▃▁' %(' ' * line)
        Top2 = u'%s.......◥█☆█▅▄▃▁▁▁▁▁▃▄▅▅ ▅▅▅▄▁' %(' ' * line)
        Top3 = u'%s〓▇████████群主专人飞机██████████████▅▄▃▁▁' %(' ' * line)
        Top4 = u'%s〓〓〓███撸撸2号██████████◤' %(' ' * line)
        print Top1
        print Top2
        print Top3
        print Top4


if __name__ == '__main__':
    test = Graphical()
    count = 0
    while count <= 9:
        os.system('cls')
        test.Aircraft(count)
        count += 1
        time.sleep(0.2)
    time.sleep(100)