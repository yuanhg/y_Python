#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#学习函数生成器

#自然数函数生成器
def Natural_Number():
    i = 1
    while True:
        yield i
        i += 1
    
#奇、偶数函数生成器
def Odd_Number():
    i = 1
    while True:
        yield i
        i += 2
        
def Even_Number():
    i = 2
    while True:
        yield i
        i += 2

#素数函数生成器
def _not_divisible(n):
    return lambda x: x % n >0

def Primes_Number():
    it = Odd_Number()   #初始序列,1开始的奇数列
    while True:
        n = next(it)
        if n==1:
            n = next(it)  # 去掉1
        it = filter(_not_divisible(n),it) #构造新的序列,筛除能被第一个数n整除的数
#        it = filter(lambda x: x%n>0,it)   #此语句lambda不能使用估计是变量n的原因
        yield n
      

#杨辉三角
def YHtriangles(layer=13):
    triangles=[1]
    while layer:
        print(triangles)
        t=[0]+triangles+[0]
        triangles=[t[i]+t[i+1] for i in range(len(t)-1)]
        layer-=1
    return "done"

#杨辉三角generator
def YHtriangles():
    triangles=[1]
    while True:
        yield triangles
        '''zip()函数接受一系列可迭代对象作为参数，将不同对象中相对应的元素打包成一个元组（tuple）'''
        triangles=[ sum(i) for i in zip( [0]+triangles, triangles+[0] ) ]


#求自然数中第xxx个素数
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x % n >0

def primes():
    yield 2
    it = _odd_iter()   #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) #构造新的序列

def primesNo(x):  #打印出第x个素数
    i=0
    pp=primes()
    while i<x:
        n=next(pp)
        i+=1
    print(n)

def primesNo2(x):  #打印出第x个素数
    i=1
    for n in primes():
        i+=1
        if i>x:
            break
    print(n)

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
#请利用filter()筛选出回数

def o_iter():
    i=0
    while True:
        i+=1
        yield i

def oio(n):
    if n==int(str(n)[::-1]):
        return True
    return False
    
def oxxo():
    p = o_iter()
    pp = filter(oio,p)
    return pp

