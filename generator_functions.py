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
'''
#自然数列求和，平方和，立方和，
'''
import math
def  n_sum(n=10):
    i, j, k = 0, 0, 0
    num = Natural_Number()
    for _ in range(n):
        t= next(num)
        i += t
        j += math.pow(t, 2)
        k += math.pow(t, 3)
    return i, j, k

'''
> 亲和数Amicable Pair是一种古老的数。 [2] 
> 在遥远的古代，人们发现某些自然数之间有特殊的关系：如果两个数a和b，a的所有除本身以外的因数approximate number之和等于b，b的所有除本身以外的因数之和等于a，则称a,b是一对亲和数。古希腊毕达哥拉斯发现的220与284；费马发现了另一对相亲数：17296和18416；笛卡儿也发现了一对相亲数：9363584和9437056；欧拉也研究过相亲数这个课题。1750年，他一口气向公众抛出了60对相亲数：2620和2924，5020和5564，6232和6368，……，从而引起了轰动。1866年，年方16岁的意大利青年巴格尼尼发现1184与1210是仅仅比220与284稍为大一些的第二对相亲数。
目前，人们已找到了12,000,000多对相亲数。但相亲数是否有无穷多对，相亲数的两个数是否都是或同是奇数，或同是偶数，而没有一奇一偶等，这些问题还有待继续探索
>如果a的约数和等于a，就称a为完美数pefect number
>第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
'''
def appro_num_sum(n):
    appro_list = []
    for i in range(1, n):
        if  n%i == 0: appro_list.append(i)
    return sum(appro_list)

def amica_pair():
    i = 10
    while True:
        j = appro_num_sum(i)
        if i < j and i == appro_num_sum(j):
            yield i, j
        i +=1

def pefect_number():
    i = 1
    while True:
        if  i == appro_num_sum(i):
            yield i
        i +=1
        
'''
>
'''
        
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


##素数函数生成器，求自然数中第xxx个素数
def iter2():
    n = 2
    while True:
        yield n
        n += 1

def _not_divisible(n):
    return lambda x: x % n >0

def primes():
    it = iter2()     #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)    #构造新的序列，筛除能被第一个数n整除的数

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

'''
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
#请利用filter()筛选出回数
'''
def o_iter():
    i=1
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

'''
#卢卡斯数列：4，14，194，37634，。。。每一项都是前一项的平方减二；
'''
def lucas_sequence():
    lu = 4
    while True:
        yield lu
        lu = lu*lu - 2

'''
#费马数列：3，5，17，257，65537，。。。，每一项都可表为 2^(2^n) + 1 ；
'''
import math
def fermat_number():
    i = 1
    while True:
        yield math.pow(2, math.pow(2, i)) + 1
        i += 1
                
'''   
# 【幸运数】
#若一个自然数各位数字之和与各位数字之积的和恰好等于这个自然数，把这样的自然数叫做“幸运数”
#19,29,~.99, 没有大于100的幸运数
'''
def luck_n():
    i = 10
    while True:
        str_l = list(str(i))
        num_l = list(map(lambda x: int(x), str_l ))
        a = reduce(lambda x,y:x+y, num_l )
        b = reduce(lambda x,y:x*y, num_l )
        if a+b == i:
            yield i
        i += 1


'''
#给出一个无限长的自然数从小到大依次排列构成的字符串S：12345678910111213……，
那么给定数字串S1，求它第一次出现的位置

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



