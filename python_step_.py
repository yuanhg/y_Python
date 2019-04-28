#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

def mult99():
    '''#打印9*9乘法表'''
    for i in range(9):
        for j in range(i+1):
            print(j+1,"*",i+1,"=",(j+1)*(i+1)," ", end="")
            if (j+1)*(i+1)<10:
                print(" ",end="")
        print("")


def tree():
    '''#用*号输出圣诞树图案'''
    for i in range(10):
        for j in range(20):
            print(" ",end="")
        for j in range(9-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print("")
    for i in range(5):
        for j in range(28):
            print(" ",end="")
        print("*")


def gcd(n1,n2):
    '''greatest common divisor function最大公因数辗转相除法也叫欧几里德算法 '''
    '''利用递归函数完成运算'''
    return gcd(n2, n1 % n2) if n2 > 0 else n1

    '''
    #利用数学算式完成运算
    while n1%n2!=0:
        n1,n2=n2,n1%n2
    return n2
    '''


def lcm(n1,n2):
    """lowest common multiple function最小公倍数"""
    return n1 * n2 // gcd(n1, n2)


def div9():
    '''用 1 到 9 组成一个九位数，使得这个数的第一位能被 1 整除，前两位组成的两位数能被 2 整除，以此类推，一直到整个九位数能被 9 整除。'''
    '''算法一：使用字符串方式，逐个找出符合条件的N位数，直到9位数'''
    n=[["1","2","3","4","5","6","7","8","9"]]
    for i in range(1,9):
        n.append([])
    for i in range(1,9):
        for j in n[i-1]:
            for k in n[0]:
                if k not in j and int(j+k)%(i+1)==0:                    
                    n[i].append(j+k)
    for i in range(9):
        print(n[i])


def factorial_recursive(n):
    '''#用递归函数实现f(x)=1*2*3*……'''
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)


def HanoiMove(n,A='A',B='B',C='C'):
    '''
    汉诺塔的移动可以用递归函数非常简单地实现,move(n, A,B,C)函数，它接收参数n，表示n个盘子;
    参数A、C，表示3个柱子,B是中间柱；然后打印出把所有盘子从A借助B移动到C的方法;
    '''
    if n==1:
        print(A,'-->',C)
    else:
        HanoiMove(n-1,A,C,B)
        HanoiMove(1,A,B,C)
        HanoiMove(n-1,B,A,C)
        
