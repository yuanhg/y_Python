#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#π＝3.1415926 5358 9793    23846 
#π蒙特卡罗模拟求pi:假设一个矩形的面积是4，矩形内切圆的半径是1，算出圆的面积是π
import random
def Pai(num):
    numHit=0
    for i in range(num):
        x=random.random()*2-1
        y=random.random()*2-1
        if x*x+y*y<=1:
            numHit+=1
    return 4*numHit/num

#π韦达公式:根号2的表现形式
#公式：  π = 2 2/sqrt(2) 2/sqrt(2+sqrt(2)) ……
import math
def wd(n=27):  #27时收敛到3.1415926 5358 9794 4，……9793 2
    T2=math.sqrt(2)
    Pi=2*2/T2
    if n==1:
        return Pi
    while n>1:
        T2=math.sqrt(2+T2)
        Pi=Pi*2/T2
        n=n-1
    return Pi

#π沃利斯公式 π/2=2*2/1*3 4*4/3*5 6*6/5*7
def wls():  #27362787时收敛到3.1415926 2456 4901 3
    Pi_N=1
    Pi =2*10**15
    n=2
    i=0
    while Pi != Pi_N:
        Pi_N=Pi
        Pi = Pi*n*n/(n-1)/(n+1)
        n=n+2
        i += 1
    return Pi,i

#π格雷戈里-莱布尼茨级数：
#公式：  π= (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
def  gllb(n=10):
    pi=0
    p=10**(n+10)
    i=1
    f=1
    while f :
        f=p//i-p//(i+2)
        pi=pi+f
        i +=4
        print(4*pi,end='\r')
    print()
    print(4*pi)
    return 4*pi//10**10


#πNilakantha 级数: 
#公式：  π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
def nila(n=10):   
    Pi=0
    p=10**(n+10)
    i=2
    f=1
    while f:
        f=p//(i*(i+1)*(i+2))-p//((i+2)*(i+3)*(i+4))
        Pi=Pi+f
        i=i+4
        print(4*Pi,end='\r')
    print()
    print(4*Pi)
    return 4*Pi//10**10+3*10**n



#马青公式，可计算任意位数
def maqing(n=10):
    p = 10 ** (n + 10)  # 准备初始整数，先多乘10个0，以增加精度，最后再去掉
    a = p * 16 // 5     # 第一项的前半部分
    b = p * 4 // -239   # 第一项的后半部分
    f = a + b           # 第一项的值
    p = f               # π
    j = 3              
    while abs(f):       # 当|f|=0后计算π的值就不会再改变了
        a //= -25       # 第n项的前半部分
        b //= -57121    # 第n项的后半部分
        f = (a + b) // j
        p += f
        j += 2
        print(p,end='\r')
    print()
    print(p)
    return p // 10**10


'''
寻找一串数字在π中的位置
'''
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
            
