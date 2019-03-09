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

def cmp_file(file_path1,file_path2):
    with open(file_path1,'rb') as pi1, open(file_path2,'rb') as pi2:
        for line1 ,line2 in zip(pi1,pi2):
            print(len(line1),len(line2))
            for i in range(len(line2)):
                if line1[i]!=line2[i]:
                    print("第",i+1,"位不同，正确的数字是",line1[i],"不是",line2[i])
