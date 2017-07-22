#!/usr/bin/env python
#coding=utf-8

array = [1, 6, 10, 8, 4, 4, 8, 8, 8, 8, 9, 0]
def Delete(srcList): # None
    if not srcList: # False
        return -1
    index = 0
    while index < len(srcList):
        if srcList[index] > 5:
            del srcList[index]
            index -= 1
        if srcList.count(srcList[index]) > 1:
            del srcList[index]
            index -= 1
        index += 1
    return 0
Delete(array)
print(array)