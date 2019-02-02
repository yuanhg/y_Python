#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def num_pi():
    '''此函数在10亿位π中寻找出现的次数，并打印出现的位置。如果刚好出现在最后，则打印不出最后出现的位置'''
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



寻找一串数字在π中的位置
'''
def fninpi():
    ss=str(input("Pls input a Number :"))
    ts=''
    
    with open('D:/data_files/Pi - Dec - Chudnovsky.txt','r')    as  pif:
        for line in pif:
            '''构造第一个和输入数字字符串等长的字符串'''
            for i in range(len(ss)):
                ts=ts+line[i]
            '''如果字符串和目标字符串不匹配，字符串自动向后滑动1位，直至相等'''
            n=len(ss)
            num=1
            while True:
                if ss==ts:
                    print("在圆周率小数点第",n-len(ss)-1,"位第",num,"次出现了",line[(n-len(ss)):n])
                    ts=ts[1:]+line[n]
                    num+=1
                else:
                    ts=ts[1:]+line[n]
                n+=1
            

