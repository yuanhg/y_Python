#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

##################################
#简单的输入输出
print('Hello,World!')
print('The quick brown fox',' jumps over','the lazy dog')
message = 'python是一门神奇的语言'
print(message)
message = 'hello, pyThon world.'
print(message)

print(message.title())  #Hello, Python World.
print(message.lower())  #hello, python world.
print(message.upper())  #HELLO, PYTHON WORLD.

message[12:27]  #'n world.'  字符串也可以用切片操作

cars = ['bmw','Audi','toyota','suBrU']
print(cars)

a = {'a':1,'b':2,'c':3}
b = {'aa':11,'bb':22,'cc':33}
dict(a,**b)

c={}
c.update(a)
c.update(b)

name = input('Please enter your name: ')
print('Hello,',name)

#时间戳（timestamp），特定的时刻。
#固定时期（period），如2007年1月或2010年全年。
#时间间隔（interval），由起始和结束时间戳表示。时期（period）可以被看做间隔（interval）的特例。

def mult99():
    '''#打印9*9乘法表'''
    for i in range(9):
        for j in range(i+1):
            print(j+1,"*",i+1,"=",(j+1)*(i+1)," ", end="")
            if (j+1)*(i+1)<10:
                print(" ",end="")
        print("")

print("\n".join("\t".join(["%s*%s=%s"%(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))

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
    #for i in range(9):
    #    print(n[i])
    print(n[8])


#4位数经过7步之内的减法，得到6174这个神奇的数字
def m6174():
    num4 = []
    for i in range(1234, 9877):
        k = len(set(str(i)))
        if k == 4:
            num4.append(i)
    print("没有重复数字的4位数总共有： ", len(num4))
    num6174 = []
    for number in num4:
       num_list = list(number)
       num_list.sort()
       num_low = int(''.join(num_list))
       num_list.sort(reverse=True)
       num_high = int(''.join(num_list))
       if num_high - num_low == 6174:
           num6174.append(num_high - num_low)
    print("一次减法得到6174的4位数有： ", len(num6174))
    print(num6174)
    
    
    
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

#遍历L
def lis(z):
    for i in z:
        if isinstance(i,list):
            lis(i)
        else:
            print(i)

list(L)
apple
google
microsoft
java
phthon
php
adam
bart
lisa
#把列表L的单词第一个字母大写，并生成一个字典
[v.capitalize() for vec in L for v in vec]
['Apple', 'Google', 'Microsoft', 'Java', 'Phthon', 'Php', 'Adam', 'Bart', 'Lisa']

#######################################
# reduce用法
#1、求listE = [1,2,3,4,5]所有元素之和
print(reduce(lambda x,y:x + y, listE))
15

#2、求listE = [1,2,3,4,5]所有元素中最大值或者最小值
print(reduce(lambda x,y:x if x>y else y, listE))
5
print(reduce(lambda x,y:x if x<y else y, listE))
1

#3、求stringsE = ['abc','abcd','def']中'abc'出现的总次数
print(reduce(lambda count, str:count + str.count('abc'), stringsE, 0))
2


'''     
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
#输入某年某月某日，判断这一天是这一年的第几天，星期几？ 
#输入三个整数x,y,z，请把这三个数由小到大输出。 
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。 
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#个人所得税扣除

''' 

 
def n_s(n=15):
    '''#一个正整数有可能表示为n个连续正整数之和，如15=1+2+3+4+5，15=7+8等。
    #那么给定一个正整数，找出所有连续正整数序列
    '''
    n_list = []
    for i in range(1, n//2+1):
        t_list = [i]       
        t = i
        j = i + 1
        while True:
            t += j
            if t < n:
                t_list .append(j)
                j +=1
            if t > n: break
            if t == n:
                t_list.append(j)
                n_list.append(t_list)
                break
    return n_list
 

'''
用一行代码就把 109 张图片读到了一个 109x256x256x4 的 numpy 数组中，耗时 172 毫秒
data = np.stack([np.array(Image.open('head%d.png'%i)) for i in range(109)], axis=0)

data = list
for i in range(109):
img = Image.open('head%d.png'%i)
img = np.array(img)
data.append(img)
data = np.stack(data, axis=0)

一行代码打印乘法口诀
print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

一行代码打印迷宫
print(''.join(__import__('random').choice('\\u2571\\u2572') for i in range(50*24)))

一行代码表白爱情
print('\n'.join([''.join([('Love'[(x-y) % len('Love')]
    if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ')
    for x in range(-30, 30)]) for y in range(30, -30, -1)]))

一行代码打印小龟龟
print('\n'.join([''.join(['*' if abs((lambda a:lambda z,c,n:a(a,z,c,n))
    (lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else ' '
    for x in range(-80,20)]) for y in range(-20,20)]))
'''


# Gather our code in a main() function
import argparse
def main():
    # create parser
    descStr = """
    This program analyzes args .
    """
    parser = argparse.ArgumentParser(description=descStr)
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()

    # add expected arguments
    group .add_argument('--common', nargs = '*', dest='plFiles', required=False)
    group .add_argument('--stats', dest='plFile', required=False)
    group .add_argument('--dup', dest='plFileD', required=False)

    # parse args
    args = parser.parse_args()

    if args.plFiles:
        # find common tracks
        findCommonTracks(args.plFiles)
    elif args.plFile:
        # plot stats
        plotStats(args.plFile)
    elif args.plFileD:
        # find duplicate tracks
        findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")

# main method
if __name__ == '__main__':
    main()