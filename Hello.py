#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello,World!')
print('The quick brown fox','jumps over','the lazy dog')
name = input('Please enter your name: ')
print('hello,',name)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
