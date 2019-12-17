#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:14:08 2019

@author: yuanhonggang
"""

def num_sub(number):
    num_list = list(str(number))
    num_list.sort()
    num_low = int(''.join(num_list))
    num_list.sort(reverse=True)
    num_high = int(''.join(num_list))
    return( num_high - num_low )


def m6174():
    num4 = []
    for i in range(1234, 9877):
        k = len(set(str(i)))
        if k == 4:
            num4.append(i)
    print("没有重复数字的4位数总共有： ", len(num4))
    num6174 = []
    for number in num4:
       if num_sub(number) == 6174:
           num6174.append(number)
    print("1次减法得到6174的4位数有： ", len(num6174))
    print(num6174)
    
    #num4 = num4 - num6174
    num4 = list(set(num4).difference(set(num6174)))
    num6174_2 = []
    for number in num4:
       if num_sub(num_sub(number)) == 6174:
           num6174_2.append(number)
    print("2次减法得到6174的4位数有： ", len(num6174_2))
    print(num6174_2)
    
    #num4 = num4 - num6174_2
    num4 = list(set(num4).difference(set(num6174_2)))
    num6174_3 = []
    for number in num4:
       if num_sub(num_sub(num_sub(number))) == 6174:
           num6174_3.append(number)
    print("3次减法得到6174的4位数有： ", len(num6174_3))
    print(num6174_3)
    
    #num4 = num4 - num6174_3
    num4 = list(set(num4).difference(set(num6174_3)))
    num6174_4 = []
    for number in num4:
       if num_sub(num_sub(num_sub(num_sub(number)))) == 6174:
           num6174_4.append(number)
    print("4次减法得到6174的4位数有： ", len(num6174_4))
    print(num6174_4)
    
    #num4 = num4 - num6174_4
    num4 = list(set(num4).difference(set(num6174_4)))
    num6174_5 = []
    for number in num4:
       if num_sub(num_sub(num_sub(num_sub(num_sub(number))))) == 6174:
           num6174_5.append(number)
    print("5次减法得到6174的4位数有： ", len(num6174_5))
    print(num6174_5)
    
    #num4 = num4 - num6174_5
    num4 = list(set(num4).difference(set(num6174_5)))
    num6174_6 = []
    for number in num4:
       if num_sub(num_sub(num_sub(num_sub(num_sub(num_sub(number)))))) == 6174:
           num6174_6.append(number)
    print("6次减法得到6174的4位数有： ", len(num6174_6))
    print(num6174_6)
    
    #num4 = num4 - num6174_6
    num4 = list(set(num4).difference(set(num6174_6)))
    num6174_7 = []
    for number in num4:
       if num_sub(num_sub(num_sub(num_sub(num_sub(num_sub(num_sub(number))))))) == 6174:
           num6174_7.append(number)
    print("7次减法得到6174的4位数有： ", len(num6174_7))
    print(num6174_7)
    
    num4 = list(set(num4).difference(set(num6174_6)))
    print("dddd", num4)
    

    
    
    
def num5(num = 123):
    while True:
        if num == num_sub(num):break
        num =num_sub(num)
        print(num)
    print(num)
    
    
def numnum(n = 12345):
    i = 1;
    first = num_sub(n)
    num = num_sub(n)
    while True:
        i += 1
        if first == num_sub(num):break
        num = num_sub(num)
    print("the no. i : ", first)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    