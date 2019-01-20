#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('D:/见与不见.txt','r')    as  pif:
    for line in pif:
        if "那里" in line:
            print(line)

with open('D:/Pi10000.txt','r')    as  pif:
    for line in pif:
        print(line)



def fninpi():
    ss=str(input("Pls input a Number :"))
    ts=''
    with open('D:/Pi - Dec - Chudnovsky.txt','r')    as  pif:
        for line in pif:
            '''构造第一个和输入数字字符串等长的字符串'''
            for i in range(len(ss)):
                ts=ts+line[i]
            '''如果字符串和目标字符串不匹配，字符串自动向后滑动1位，直至相等'''
            n=len(ss)
            num=1
            while True:
                if ss==ts:
                    print("在圆周率小数点第",n-len(ss)-1,"位第",num,"次出现了",line[(n-len(ss)):n])
                    ts=ts[1:]+line[n]
                    num+=1
                else:
                    ts=ts[1:]+line[n]
                n+=1
            
