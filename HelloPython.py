#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#简单的输入输出
print('Hello,World!')
print('The quick brown fox','jumps over','the lazy dog')
name = input('Please enter your name: ')
print('hello,',name)

#编码
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#列表
L=[
	['apple','google','microsoft'],
	['java','phthon','php'],
	['adam','bart','lisa']
	]
print(L[2][2])
lisa
print(L[1][-2:])
['phthon', 'php']

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
