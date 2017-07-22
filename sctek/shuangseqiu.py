#!/usr/bin/env python
#coding=utf-8

import random

#获取红球
hjc = random.sample(range(1,33), 6)
hjc.sort()
#获取蓝球
ljc = random.sample(range(1,16), 1)
#中奖号码
#print "开奖号码为:%s + %s" % (hjc,ljc)

#用户自选号码
hyh = []
lyh = []
hong = input("请输入六个红球号码: ")
hyh.append(hong)
yhhm = list(hyh[0])
lan = input("请输入一个篮球号码: ")
if lan < 1 or lan > 16:
    print("请输入1~16之间的数值，请重新输入")
    lan = input("请输入一个篮球号码: ")
lyh.append(lan)
print "您输入的号码为: %s + %s" % (yhhm,lyh)
#已中奖的红球号码
yh_hong = []
yh_lan = []
while len(yhhm) > 0 :
    nember = yhhm.pop()
    if nember in hjc:
        yh_hong.append(nember)
yh_hong.sort()
#已中奖的篮球号码
if lyh == ljc:
    yh_lan.append(lyh[0])
print "已中奖的号码: 红球%s + 蓝球%s" % (yh_hong,yh_lan)

#中奖信息
if str(len(yh_hong))+str(len(yh_lan)) == str(6)+str(1):
    print("恭喜中一等奖：1000万")
elif str(len(yh_hong))+str(len(yh_lan)) == str(6)+str(0):
    print("恭喜中二等奖：500万")
elif str(len(yh_hong))+str(len(yh_lan)) == str(5)+str(1):
    print("恭喜中三等奖：3000元")
elif str(len(yh_hong))+str(len(yh_lan)) == str(5)+str(0) or str(len(yh_hong))+str(len(yh_lan)) == str(4)+str(1):
    print("恭喜中四等奖：200元")
elif str(len(yh_hong))+str(len(yh_lan)) == str(4)+str(0) or str(len(yh_hong))+str(len(yh_lan)) == str(3)+str(1):
    print("恭喜中五等奖：10元")
elif str(len(yh_hong))+str(len(yh_lan)) == str(2)+str(1) or str(len(yh_hong))+str(len(yh_lan)) == str(1)+str(1) or str(len(yh_hong))+str(len(yh_lan)) == str(0)+str(1):
    print("恭喜中六等奖：5元")
else:
    print("很遗憾没有中奖！")

#开奖号码
print "开奖号码为:%s + %s" % (hjc,ljc)
