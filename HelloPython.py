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
#用*号输出字母C的图案
#要求输出国际象棋棋盘
#求两个整数的最小公倍数、最小公约数
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
#用 1 到 9 组成一个九位数，使得这个数的第一位能被 1 整除，前两位组成的两位数能被 2 整除，前三位组成的三位数能被 3 整除，以此类推，一直到整个九位数能被 9 整除。
#自然数内的前50个素数，每行显示10个
#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#十进制转16进制,十六进制转十进制
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
#输入某年某月某日，判断这一天是这一年的第几天，星期几？ 
#输入三个整数x,y,z，请把这三个数由小到大输出。 
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。 
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
企业发放的奖金根据利润提成。利润(I)
低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
#把列表L的单词第一个字母大写，并生成一个字典
#1.波那契数列。1，1，2，3，5。。每一项都是前二项的和；（兔子问题）
#2.卢卡斯数列：4，14，194，37634，。。。每一项都是前一项的平方减二；
#3.费马数列：3，5，17，257，65537，。。。，每一项都可表为 2^(2^n) + 1 ；

#自然数列求和，平方和，立方和，


#π＝3.14159265358979325

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

def Lei_Pi_Num(n=10000):
    Pi = 0
    LeiPi = Lei_Pi()
    while n>0:
        Pi = Pi + next(LeiPi)
        n = n -1
    return 4*Pi
#πNilakantha 级数:
#公式：  π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
def N_Pi_Num(n=10000):
    Pi=0
    i=2
    while n>0:
        Pi=Pi+1/(i*(i+1)*(i+2))-1/((i+2)*(i+3)*(i+4))
        i=i+4
        n=n-1
    return 3+4*Pi
#π韦达公式:根号2的表现形式
#公式：  π = 2 2/sqrt(2) 2/sqrt(2+sqrt(2)) ……
import math
def WD_Pi(n=10000):
    T2=math.sqrt(2)
    Pi=2*2/T2
    if n==1:
        return Pi
    while n>1:
        T2=math.sqrt(2+T2)
        Pi=Pi*2/T2
        n=n-1
    return Pi


#给出一个无限长的自然数构成的字符串S：12345678910111213……，它是由自然数
#从小到大依次排列出来的。那么给定数字串S1，求它第一次出现的位置

#一个正整数有可能表示为n个连续正整数之和，如15=1+2+3+4+5，15=7+8等。
#那么给定一个正整数，找出所有连续正整数序列
        
#函数的参数
#默认参数






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



        


        
