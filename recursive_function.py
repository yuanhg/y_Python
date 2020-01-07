#!/usr/bin/env python3
#-*- coding: utf-8 -*-


def gcd(n1,n2):
    '''greatest common divisor function最大公因数 '''
    '''利用递归函数完成运算,辗转相除法也叫欧几里德算法'''
    
    return gcd(n2, n1 % n2) if n2 > 0 else n1


def lcm(n1,n2):
    """lowest common multiple function最小公倍数"""
    
    return n1 * n2 // gcd(n1, n2)


def factorial_recursive(n):
    '''#用递归函数实现f(x)=1*2*3*……'''
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)


def HanoiMove(n=3, A='A', B='B', C='C'):
    '''汉诺塔的移动可以用递归函数非常简单地实现,
    move(n, A,B,C)函数，它接收参数n，表示n个盘子;参数A、C，表示3个柱子,B是中间柱；
    然后打印出把所有盘子从A借助B移动到C的方法;
    '''
    if n==1:
        print("No. ", n, "from ", A, '-->', C, ".")
    else:
        HanoiMove(n-1,A,C,B)
        print("No. ", n, "from ", A, '-->', C, ".")
        HanoiMove(n-1,B,A,C)
        
