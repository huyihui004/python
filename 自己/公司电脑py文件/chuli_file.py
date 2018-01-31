#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
统计每个学生的平时作业总得分。
看一下我们的文档里的数据：
#-- scores.txt
刘备 23 35 44 47 51
关羽 60 77 68
张飞 97 99 89 91
诸葛亮 100
'''
f=open('scores.txt','r+')
lines=f.readlines()
#print lines
f.close()


results = []
for line in lines:
    data = line.split()
    sum = 0
    for core in data[1:]:
        sum += int(core)
    result="%s \t: %s\n" % (data[0],str(sum))
    results.append(result)
output = file('result.txt','w')
output.writelines(results)
output.close()

'''
jieguos={}
for line in lines:
    data = line.split()
    jieguo=0
    for j in data[1:]:
        jieguo += int(j)
    jieguos[data[0]] = jieguo
p=open('jieguos.txt','w+')
for key in jieguos:
    p.write(key)
    p.write('\t')
    p.write(str(jieguos[key]))
    p.write('\n')
p.close()
'''
