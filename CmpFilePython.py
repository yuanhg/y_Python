#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#



def pipi():
    with open('D:/wallpapers/hima820190129110000fd.png','rb') as pi1, open('D:/wallpapers/hima820190129103000fd.png','rb') as pi2:
        for line1 ,line2 in zip(pi1,pi2):
            print(len(line1),len(line2))
            for i in range(len(line2)):
                if line1[i]!=line2[i]:
                    print("第",i+1,"位不同，正确的数字是",line1[i],"不是",line2[i])
                
                       
input()
