#!/usr/bin/env python
#coding=utf-8
import random
import os
'''
分组实现保存不同用户的数据
game.txt的内容如下
胡益辉 3 5 31
总游戏次数，最快猜出的轮数，猜过的总轮数
'''
Name = raw_input('请输入名字：')
if not os.path.exists('game.txt'):  #如果文件不存在则新建一个空文件
    open('game.txt','w')
game = open('game.txt')
Data = game.readlines()
game.close()
result = {}  #初始化一个字典
for line in Data:
    s = line.split()  #把每一行数据拆分成list
    result[s[0]] = s[1:]  #把第一项作为key，把剩下的作为value
if result.get(Name) is None:  #如果当前玩家数据没有，则初始化数据
    result[Name]=(0,0,0)
T1,T2,T3=int(result.get(Name)[0]),int(result.get(Name)[1]),int(result.get(Name)[2])  #获取之前玩家的数据
p = random.randint(1,20)  #取一个随机数
num = 0
while True:
    num += 1
    number = input('请输入一个数字猜大小：')
    if number < p:
        print('小了')
    elif number > p:
        print('大了')
    else:
        print('回答正确')
        break
if num < T2 or T2 == 0:
    T2 = num
T3 += num
T1 += 1
P = float(T3)/T1
print "%s: 总游戏次数:%d 最快猜出的轮数:%d 平均猜出答案的轮数:%.2f" % (Name,T1,T2,P)
result[Name] = str(T1),str(T2),str(T3)
#把字典的结果字符化并写入文件
results = ''
for n in result:
    reg = n + ' ' + ' '.join(result[n]) + '\n'
    results += reg
game = open('game.txt','w')
game.write(results)
game.close()

