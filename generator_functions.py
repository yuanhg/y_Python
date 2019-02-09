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

#给出一个无限长的自然数从小到大依次排列构成的字符串S：12345678910111213……，那么给定数字串S1，求它第一次出现的位置
'''
定义字符串生成器函数,字符串S：12345678910111213……每次返回一个数字字符s，以
及这个数字字符是第几个自然数中的字符，n表示。也就是说，字符串生成函数返回一个list，
第一个元素是数字字符s，第二个元素代表s是第n个自然数中数字
'''
def NN_String():
        n=1
    while True:
        ns=str(n)  #数字转换为字符串
        for s in ns:
            yield (s,n)  #返回一个字符,以及这个字符在第n个自然数中
        n += 1
            
#寻找匹配的数字字符串，默认是第一次匹配处
def FN(num=1):
    '''num表示找到几个匹配的地方'''
    ts=input("Pls input a Number :")
    ns=NN_String()
    ss=''
    '''构造第一个和输入数字字符串等长的字符串'''
    for tts in ts:
        sslist = next(ns)
        ss = ss + sslist[0]
    '''连续输出输出字符串'''
    print(ss, end="")
    while num >0:
        '''如果字符串和目标字符串不匹配，字符串自动向后滑动1位，直至相等'''
        while ss != ts:
            sslist = next(ns)
            nss = sslist[0]
            nn = sslist[1]
            print(nss,end="")
            ss = ss[1:]+nss
        print("")
        print("(",ss," ) in the NUMBER:",nn)
        num = num -1
        '''如果num大于0，则字符串向后滑动一位，再开始下一轮比较'''
        if num > 0:
            nss=next(ns)
            print(nss[0], end="")
            ss = ss[1:]+nss[0]



