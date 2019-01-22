#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

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


#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，#注意不要调用str的strip()方法
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


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
"""greatest common divisor function最大公因数辗转相除法也叫欧几里德算法 """
def Gcd_OU(n1,n2):
    '''利用递归函数完成运算'''
    return Gcd_OU(n2, n1 % n2) if n2 > 0 else n1

    """'''利用数学算式完成运算'''
    while n1%n2!=0:
        n1,n2=n2,n1%n2
    return n2
    """
"""greatest common divisor function更相减损法也叫也叫更相减损术，是出自《九章算术》 """
def Gcd_JZ(n1,n2,i=0):    
    while n1%2==0 and n2%2==0:
        n1=n1/2
        n2=n2/2
        i+=1
    while n2!=n1:
        n1,n2=n2,abs(n1-n2)
    return n1 if i==0 else n1*2*i
    
"""最小公倍数 """
def lcm(n1,n2):
    """lowest common multiple function"""
    return n1 * n2 // gcd(n1, n2)

'''
硬算:
公倍数用最小数的倍数逐个测试；公因数用两个数的因数分解，从最大开始往最小比较，找到第一个一样的
'''
def lcm_gcd():

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
'''算法一：使用字符串方式，逐个找出符合条件的N位数，直到9位数'''
def div9():
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

'''算法二：逐个数字进行运算看是否满足要求'''
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
'''


    


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


#汉诺塔
'''
汉诺塔的移动可以用递归函数非常简单地实现,move(n, A,B,C)函数，它接收参数n，表示n个盘子;
参数A、C，表示3个柱子,B是中间柱；然后打印出把所有盘子从A借助B移动到C的方法;
'''
def HanoiMove(n,A='A',B='B',C='C'):
    if n==1:
        print(A,'-->',C)
    else:
        HanoiMove(n-1,A,C,B)
        HanoiMove(1,A,B,C)
        HanoiMove(n-1,B,A,C)
        


        
