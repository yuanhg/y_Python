#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
'''
The Zen of Python, by Tim Peters
Python之禅 by Tim Peters

Beautiful is better than ugly.
优美胜于丑陋（Python 以编写优美的代码为目标）
Explicit is better than implicit.
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
Simple is better than complex.
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
Complex is better than complicated.
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
Sparse is better than dense.
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
Readability counts.
可读性很重要（优美的代码是可读的）
Special cases aren't special enough to break the rules.
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
Although practicality beats purity.
当存在多种可能，不要尝试去猜测
Errors should never pass silently.
不要包容所有错误
Unless explicitly silenced.
除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
Now is better than never.
做也许好过不做
Although never is often better than *right* now.
但不假思索就动手还不如不做（动手之前要细思量）
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
Namespaces are one honking great idea -- let's do more of those!
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
'''
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


name = input('Please enter your name: ')
print('Hello,',nname)

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



'''
# reduce用法
1、求listE = [1,2,3,4,5]所有元素之和
        print(reduce(lambda x,y:x + y, listE))
2、求listE = [1,2,3,4,5]所有元素中最大值或者最小值
        print(reduce(lambda x,y:x if x>y else y, listE))
3、求stringsE = ['abc','abcd','def']中'abc'出现的总次数
        print(reduce(lambda count, str:count + str.count('abc'), stringsE, 0))

'''


'''     
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

## 【数】
### 【质（素）数】 
> 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。

### 【完全数】
> 又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
### 【梅森素数】
> 所谓梅森数，是指形如2p－1的一类数，其中指数p是素数，常记为Mp 。如果梅森数是素数，就称为梅森素数。
> 用因式分解法可以证明，若2n－1是素数，则指数n也是素数；反之，当n是素数时，2n－1（即Mp）却未必是素数。前几个较小的梅森数大都是素数，然而梅森数越大，梅森素数也就越难出现。
> 目前仅发现50个梅森素数，最大的是 277232917－1（即2的77232917次方减1），有23249425位数。
### 【自幂数】
> 自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。（例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数）；
> 自幂数包括：独身数、水仙花数、四叶玫瑰数、五角星数、六合数、北斗七星数、八仙数、九九重阳数、十全十美数 
### 【对称（回）数】
> 一个整数，它的各位数字如果是左右对称的，则称这个数是对称数。也称之为回数，就是倒着读和正着读一样的数 


### 【亲和数】 
> 亲和数是一种古老的数。 [2] 
> 在遥远的古代，人们发现某些自然数之间有特殊的关系：如果两个数a和b，a的所有除本身以外的因数之和等于b，b的所有除本身以外的因数之和等于a，则称a,b是一对亲和数。古希腊毕达哥拉斯发现的220与284；费马发现了另一对相亲数：17296和18416；笛卡儿也发现了一对相亲数：9363584和9437056；欧拉也研究过相亲数这个课题。1750年，他一口气向公众抛出了60对相亲数：2620和2924，5020和5564，6232和6368，……，从而引起了轰动。1866年，年方16岁的意大利青年巴格尼尼发现1184与1210是仅仅比220与284稍为大一些的第二对相亲数。
目前，人们已找到了12,000,000多对相亲数。但相亲数是否有无穷多对，相亲数的两个数是否都是或同是奇数，或同是偶数，而没有一奇一偶等，这些问题还有待继续探索
### 【完全平方数】
> 若一个数能表示成某个整数的平方的形式，则称这个数为完全平方数。


### 【自守数】
> 如果某个数的平方的末尾极为数等于这个数，那么就称这个数为自守数。 
> 显然，5和6是一位自守数（5x5=25 6x6=36） 
> 25x25=625 76x76=5776，所以25和76是两位自守数。 
> 自守数有一个特性，以他为后几位的两个数相乘，乘积的后几位仍是这个自守数。因为5时自守数，所以以5为个位数的两个数相乘，乘积的个位仍然是5；76是自守数，所以以76为后两位数的两个数相乘，其结果的后两位仍是76，如176x576=101376。 
> 虽然0和1的平方的个位数仍然是0和1，但是他们太“平凡”了，研究他们没有意义，所以不算自守数。 
> 三位自守数是625和376，四位自守数是0625和9376，五位自守数是90625和09376...... 
> 我们可以看到，（n+1）位的自守数出自n位的自守数。由此得出，如果知道n位的自守数a，那么（n+1）位的自守数应当由a前面加上一个数构成。 
> 实际上，简化一下，还能发现如下规律： 
> 5+6=11 
> 25+76=101 
> 625+376=1001 
> ...... 
> 所以，两个n位自守数，他们的和等于10^n+1

### 【魔术数】
> 将自然数N接写在每一个自然数的右面,如果得到的新数都能被N整除,那么N称为魔术数
> 
### 【幸运数】
> 若一个自然数各位数字之和与各位数字之积的和恰好等于这个自然数，把这样的自然数叫做“幸运数”

#一个正整数有可能表示为n个连续正整数之和，如15=1+2+3+4+5，15=7+8等。
#那么给定一个正整数，找出所有连续正整数序列

'''    



