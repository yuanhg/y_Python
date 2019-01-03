#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#简单的输入输出
print('Hello,World!')
print('The quick brown fox','jumps over','the lazy dog')

yName = input('Please enter your name: ')
print('Hello,',yNname)

#编码
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#字典
yDict = {'name': 'Zara', 'age': 47}
#字典转为字符串
str(yDict)
"{'name': 'Zara', 'age': 47}"
#字典可以转为元组
tuple(yDict)
('name', 'age')
#字典可以转为元组
tuple(yDict.values())
('Zara', 47)
#字典转为列表
list(yDict)
['name', 'age']
#字典转为列表
list(yDict.values())
['Zara', 47]

#元组
yTuple=(1, 2, 3, 4, 5,6,7,8)
#元组转为字符串
yTuple.__str__()
'(1, 2, 3, 4, 5, 6, 7, 8)'
#元组转为列表
list(yTuple)
[1, 2, 3, 4, 5, 6, 7, 8]
#元组不可以转为字典*

#列表
yList=[1, 3, 5, 7, 9, 11, 13]
#列表转为字符串
str(yList)
'[1, 3, 5, 7, 9, 11, 13]'
#列表转为元组
tuple(yList)
(1, 3, 5, 7, 9, 11, 13)
#列表不可以转为字典*

#字符串
yStr="(1,2,3)"
#字符串转为元组
tuple(eval(yStr))
(1, 2, 3)
#字符串转为列表
list(eval(yStr))
[1, 2, 3]
#字符串转为字典
yStr1="{'name':'yuan', 'age':46}"
eval(yStr1)
{'name': 'yuan', 'age': 46}

#复杂列表
L=[
	['apple','google','microsoft'],
	['java','phthon','php'],
	['adam','bart','lisa']
	]

print(L[2][2])
lisa
print(L[1][-2:])
['phthon', 'php']

#打印9*9乘法表
def mult99():
    for i in range(9):
        for j in range(i+1):
            print(j+1,"*",i+1,"=",(j+1)*(i+1)," ", end="")
            if (j+1)*(i+1)<10:
                print(" ",end="")
        print("")

#用*号输出圣诞树图案
def tree():
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

#求两个整数的最小公倍数、最小公因数
def Gcd_OU(n1,n2):
    """greatest common divisor function辗转相除法也叫欧几里德算法 """
    return Gcd_OU(n2, n1 % n2) if n2 > 0 else n1

    """
    while n1%n2!=0:
        n1,n2=n2,n1%n2
    return n2
    """

def Gcd_JZ(n1,n2,i=0):
    """greatest common divisor function更相减损法也叫也叫更相减损术，是出自《九章算术》 """
    while n1%2==0 and n2%2==0:
        n1=n1/2
        n2=n2/2
        i+=1
    while n2!=n1:
        n1,n2=n2,abs(n1-n2)
    return n1 if i==0 else n1*2*i
    

def lcm(n1,n2):
    """lowest common multiple function"""
    return n1 * n2 // gcd(n1, n2)

def lcm_gcd():
    '''硬算。公倍数用最小数的倍数逐个测试；'''
    '''公因数用两个数的因数分解，从最大开始往最小比较，找到第一个一样的'''
    n1=int(input("please type in the first number:"))
    n2=int(input("please type in the second number:"))
    if n2>n1:
        n1, n2=n2, n1
    for i in range(2, n1+1):
        if n2*i%n1==0:
            print("the lcm is:", n2*i)
            break
    l1=[]
    l2=[]
    for i in range(1,n1+1):
        if n1%i==0:
            l1.append(i)
    for i in range(1,n2+1):
        if n2%i==0:
            l2.append(i)
    if len(l2)>len(l1):
        l1, l2=l2, l1
    for i in range(len(l2)):
        for j in range(len(l1)):
            if l2[-1-i]==l1[-1-j]:
                print("the gcd is:", l2[-1-i])
                break
        if l2[-1-i]==l1[-1-j]:
            break
        
#用 1 到 9 组成一个九位数，使得这个数的第一位能被 1 整除，前两位组成的两位数能被 2 整除，以此类推，一直到整个九位数能被 9 整除。
def div9():
    '''使用字符串方式，逐个找出符合条件的N位数，直到9位数'''
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

def div10():
    '''使用字符串方式，逐个找出符合条件的N位数，直到n位数'''
    n=["0","1","2","3","4","5","6","7","8","9"]
    L=[["1","2","3","4","5","6","7","8","9"]]
    i=1
    while True:
        L.append([])
        flage =0
        for j in L[i-1]:
            for k in n:
                if k not in j and int(j+k)%(i+1)==0:                    
                    L[i].append(j+k)
                    flage = 1
        if flage == 0:
            break
        else:
            i += 1
    for i in range(len(L)):
        print(L[i])
      
from datetime import datetime
def divi9():
    '''硬除，直到找到9位数'''
    begin=datetime.now()
    for n in range(123456789,987654321):
        if   str(n).count("0")>0:
            continue
        elif str(n).count("1")>1:
            continue
        elif str(n).count("2")>1:
            continue
        elif str(n).count("3")>1:
            continue
        elif str(n).count("4")>1:
            continue
        elif str(n).count("5")>1:
            continue
        elif str(n).count("6")>1:
            continue
        elif str(n).count("7")>1:
            continue
        elif str(n).count("8")>1:
            continue
        elif str(n).count("9")>1:
            continue

        if n%9 != 0:
            continue
        elif n//10%8 !=0:
            continue
        elif n//100%7 !=0:
            continue
        elif  n//1000%6 !=0:
            continue
        elif n//10000%5 !=0:
            continue
        elif n//100000%4 != 0:
            continue
        elif n//1000000%3 != 0:
            continue
        elif n//10000000%2 != 0:
            continue
        else:
            print("time lasting:",datetime.now()-begin)
            print(n)

    print("the finish time last is :",datetime.now()-begin)

if __name__ == "__main__" :
    divi9()
    
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
#自然数内的前50个素数，每行显示10个
#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#十进制转16进制,十六进制转十进制
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
#输入某年某月某日，判断这一天是这一年的第几天，星期几？ 
#输入三个整数x,y,z，请把这三个数由小到大输出。 
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。 
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#个人所得税扣除
#把列表L的单词第一个字母大写，并生成一个字典
#1.波那契数列。1，1，2，3，5。。每一项都是前二项的和；（兔子问题）
#2.卢卡斯数列：4，14，194，37634，。。。每一项都是前一项的平方减二；
#3.费马数列：3，5，17，257，65537，。。。，每一项都可表为 2^(2^n) + 1 ；

#自然数列求和，平方和，立方和，


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
#π格雷戈里-莱布尼茨级数：
#公式：  π= (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
def  Lei_Pi():
    i = 1
    while True:
        yield 1/i-1/(i+2)
        i = i +4

def Lei_Pi_Num(n=47454000):  #  47454000时收敛到3.1415926 4457 6215 7，……5358  9793 2
    Pi = 0
    LeiPi = Lei_Pi()
    while n>0:
        Pi = Pi + next(LeiPi)
        n = n -1
    return 4*Pi

def Lei_Pi_NumS(n=47454000):  #不使用迭代
    Pi=0
    i=1
    while n>0:
        Pi=Pi+1/i-1/(i+2)
        i=i+4
        n=n-1
    return 4*Pi

def Lei_Pi_NumS_N():  #33558529不使用迭代
    Pi=0
    i=1
    k=0
    Pi_N=3    
    while Pi_N - Pi != 0:
        Pi_N=Pi
        Pi=Pi+1/i-1/(i+2)
        i=i+4
        k+=1
    return 4*Pi,k

#πNilakantha 级数: 
#公式：  π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
def N_Pi_Num(n=44531):   #44531时收敛到3.1415926 5358 9791 3，……9793 2
    Pi=0
    i=2
    while n>0:
        Pi=Pi+1/(i*(i+1)*(i+2))-1/((i+2)*(i+3)*(i+4))
        i=i+4
        n=n-1
        print("%.53f"%(3+4*Pi),end='\r')
    print()
    print("%.53f"%(3+4*Pi))

def N_Pi_Num_N():   #7658时收敛到3.1415926 5358 9722 5，……9793 2
    Pi=0
    i=2
    k=0
    Pi_N=3
    while (Pi_N  - Pi )!= 0:
        Pi_N=Pi
        Pi=Pi+4/(i*(i+1)*(i+2))-4/((i+2)*(i+3)*(i+4))
        i=i+4
        k+=1
    return 3+Pi,k

def N_Pi_Num_N():   #7657时收敛到3.1415926 5358 9722 5，……9793 2
    Pi=0
    Pi_N=4/2/3/4-4/4/5/6
    i=2
    k=0
    while Pi_N > Pi :
        Pi=Pi+4/(i*(i+1)*(i+2))-4/((i+2)*(i+3)*(i+4))
        Pi_N=Pi_N+4/((i+4)*(i+5)*(i+6))-4/((i+6)*(i+7)*(i+8))
        i=i+4
        k+=1
    return 3+Pi,k

#π韦达公式:根号2的表现形式
#公式：  π = 2 2/sqrt(2) 2/sqrt(2+sqrt(2)) ……
import math
def WD_Pi(n=27):  #27时收敛到3.1415926 5358 9794 4，……9793 2
    T2=math.sqrt(2)
    Pi=2*2/T2
    if n==1:
        return Pi
    while n>1:
        T2=math.sqrt(2+T2)
        Pi=Pi*2/T2
        n=n-1
    return Pi

import math
def WD_Pi_N():  #计算收敛时的Pi值和迭代次数
    T2=math.sqrt(2)
    Pi=2*2/T2
    Pi_N=3
    i=0
    while Pi != Pi_N:
        Pi_N=Pi
        T2=math.sqrt(2+T2)
        Pi=Pi*2/T2
        i +=1
    return Pi,i


#给出一个无限长的自然数从小到大依次排列构成的字符串S：12345678910111213……，那么给定数字串S1，求它第一次出现的位置

#定义字符串生成器函数,字符串S：12345678910111213……
def NN_String():
    '''每次返回一个数字字符s，以及这个数字字符是第几个自然数中的字符，n表示'''
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

   
    


#一个正整数有可能表示为n个连续正整数之和，如15=1+2+3+4+5，15=7+8等。
#那么给定一个正整数，找出所有连续正整数序列
        
#函数的参数
#默认参数

'''# reduce用法
1、求listE = [1,2,3,4,5]所有元素之和
        print(reduce(lambda x,y:x + y, listE))
2、求listE = [1,2,3,4,5]所有元素中最大值或者最小值
        print(reduce(lambda x,y:x if x>y else y, listE))
3、求stringsE = ['abc','abcd','def']中'abc'出现的总次数
        print(reduce(lambda count, str:count + str.count('abc'), stringsE, 0))

'''



classEnroll = []

def addEnroll(name,gender,age=15,city='Beijing'):
    enroll=[name,gender,age,city]
    classEnroll.append(enroll)
    



import math

def quadratic(a,b,c):
    



#计算几个数据的乘积，空返回空，数据个数任意

def product(*numbers):
    if numbers:
        num = 1
        for n in numbers:
            num = num * n
        return num
    else:
        return None

#用递归函数实现f(x)=1*2*3*……

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)



#汉诺塔的移动可以用递归函数非常简单地实现
#请编写move(n, A,B,C)函数，它接收参数n，表示n个盘子;
#参数A、C，表示3个柱子,B是中间柱；
#然后打印出把所有盘子从A借助B移动到C的方法;

def HanoiMove(n,A='A',B='B',C='C'):
    if n==1:
        print(A,'-->',C)
    else:
        HanoiMove(n-1,A,C,B)
        HanoiMove(1,A,B,C)
        HanoiMove(n-1,B,A,C)
        
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
#注意不要调用str的strip()方法

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


#等差数列、等比数列、回数数列

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

def YHtriangles(layer):
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
#        t=[0]+triangles+[0]
#       triangles=[t[i]+t[i+1] for i in range(len(t)-1)]
#﻿﻿zip()函数接受一系列可迭代对象作为参数，将不同对象中相对应的元素打包成一个元组（tuple），
#返回由这些元组组成的list列表，如果传入的参数的长度不等，则返回的list列表的长度和传入参数中最短对象的长度相同。
        triangles=[sum(i) for i in zip([0]+triangles,triangles+[0])]


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



        


        
