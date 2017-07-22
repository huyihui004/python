#!/usr/bin/env python
#coding=utf-8

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''

def Number( m ):
    if ( m <= 10 ):
        p = m * 0.1
        print "奖金是: ", p,"万元"
    elif ( 10 < m <= 20 ):
        p1 = ( m - 10 ) * 0.075
        p = 10 * 0.1 + p1
        print "奖金是：", p,"万元"
    elif ( 20 < m <= 40 ):
        p1 = ( m - 20 ) * 0.05
        p = 10 * 0.1 + 10 *0.075 + p1
        print "奖金是：", p,"万元"

n = int(raw_input("请输入利润值："))
Number(n)
