#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fninpi():
    ss=str(input("Pls input a Number :"))
    ts=''
    with open('D:/Pi1000.txt','r')    as  pif:
        for line in pif:
            '''构造第一个和输入数字字符串等长的字符串'''
            for i in range(len(ss)):
                ts=ts+line[i]
            '''如果字符串和目标字符串不匹配，字符串自动向后滑动1位，直至相等'''
            n=len(ss)
            num=1
            while True:
                if ss==ts:
                    print("在圆周率中（含小数点）第",n-len(ss)+1,"位第",num,"次出现了",line[(n-len(ss)):n])
                    num+=1
                if n==len(line):
                    break
                ts=ts[1:]+line[n]
                n+=1
            print("搜索完毕")

def pipi():
    with open('D:/Pi - Dec - Chudnovsky.txt','r') as pi1, open('D:/Pi1000.txt','r') as pi2:
        for line1 ,line2 in zip(pi1,pi2):
            print(len(line1),len(line2))
            for i in range(len(line2)):
                if line1[i]!=line2[i]:
                    print("第",i+1,"位不同，正确的数字是",line1[i],"不是",line2[i])
                
                       
