#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''#π＝3.1415926 5358 9793    23846 '''

import random
def Pai(num):
    '''#π蒙特卡罗模拟求pi:假设一个矩形的面积是4，矩形内切圆的半径是1，算出圆的面积是π'''
    numHit=0
    for i in range(num):
        x=random.random()*2-1
        y=random.random()*2-1
        if x*x+y*y<=1:
            numHit+=1
    return 4*numHit/num



import math
def wd(n=27):
    '''
    #π韦达公式:根号2的表现形式
    #公式：  π = 2 2/sqrt(2) 2/sqrt(2+sqrt(2)) ……
    #27时收敛到3.1415926 5358 9794 4
    '''
    T2=math.sqrt(2)
    Pi=2*2/T2
    if n==1:
        return Pi
    while n>1:
        T2=math.sqrt(2+T2)
        Pi=Pi*2/T2
        n=n-1
    return Pi


def wls():
    '''
    #π沃利斯公式 π/2=2*2/1*3 4*4/3*5 6*6/5*7 ……
    #27362787时收敛到3.1415926 2456 4901 3
    '''
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


def  gllb(n=10):
    '''
    #π格雷戈里-莱布尼茨级数：
    #公式：  π= (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
    '''
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


def nila(n=10):
    '''#πNilakantha 级数:
    #公式：  π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...'''
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


def maqing(n=100):
    '''#马青公式，可计算任意位数.'''
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
    return p // 10**10


def new_pi(numbers=1000000, lines=True,  line_num=100):
    """
    本函数从拥有10亿位的pi(楚德诺夫斯基公式)中生成一个拥有指定pi位数的文件，
    默认1000000位，每行100位数字，且3. 单独一行
    """
    file_path = 'D:\data_files\Pi - Dec - Chudnovsky.txt'
    '''生成文件名'''
    save_path = 'D:\data_files\Pi - Dec - ' + str(numbers)
    if lines == True:
        save_path += 'n.txt'    #换行加“n”作为标识
    else:
        save_path += '.txt'
    '''读取文件'''
    try:
        with open(file_path,'r',encoding='UTF-8') as fr:
            data = fr.read(numbers+2)   #考虑到“3.”，多读2位
    except FileNotFoundError:
        print('Sorry, the file  ', file_path, ' does not exists.')
    else:
        '''开始写文件'''
        with open(save_path,'w',encoding='UTF-8') as fs:
            if lines == False:
                fs.write(data)
            else:
                i = 2
                fs.write(data[:2])
                fs.write('\n')
                while i < len(data):
                    fs.write(data[i:i+line_num])
                    fs.write('\n')
                    i += line_num
        print('All is done')
        

def num_pi():
    '''此函数在10亿位π中寻找出现的次数，并打印出现的位置。'''
    '''利用字符串切分为list，统计list个数的方法'''
    word = input("Pls input a Number :")        #   获得数字字符串
    file_path = 'D:\data_files\Pi - Dec - Chudnovsky.txt'
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:   
            contents = f.read()     #contents is STRING
    except FileNotFoundError:
        print('Sorry, the file  ', file_path, ' does not exists.')
    else:
        words = contents.split(word)            #words is LIST,把字符串用要找的单词切分，
        i = len(words) - 1
        print('"' + word + '"' + "在π中出现了 " + str(i) + "次。")
        for i in range(len(words)-1):
            print("第" + str(i+1) + "次出现在数字" + words[i][-5:] + " " + word + " " + words[i+1][:3] + ";")


def num_pi2():
    '''此函数在10亿位π中寻找出现的次数，并打印出现的位置。'''
    '''逐个字节比较的方法'''
    word = input("Pls input a Number :")        #   获得数字字符串
    file_path = 'D:\data_files\Pi - Dec - Chudnovsky.txt'
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:   
            contents = f.read()     #contents is STRING
    except FileNotFoundError:
        print('Sorry, the file  ', file_path, ' does not exists.')
    else:
        num = 0
        for i in range(len(word)-1,len(contents)):
            if word == contents[i+1-len(word):i+1]:
                num += 1
                print("第" + str(num) + "次出现在数字" + contents[i+1-len(word)-5:i+1-len(word)] + " "
                      + word + " " + contents[i+1:i+3] + ";")
        print('"' + word + '"' + "在π中出现了 " + str(num) + "次。")


