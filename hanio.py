# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:16:30 2019

@author: faqui
"""

def hanoi(n, a, b, c):
    if n==1:
        print("Number ", n, "from ", a, "to ", c)
    else:
        hanoi(n-1, a, c, b)
        print("Number ", n, "from ", a, "to ", c)
        hanoi(n-1, b, a, c)
        
hanoi(99, 'a', 'b', 'c')