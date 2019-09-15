#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Example Fibonacci sequence: 0,1,1,2,3,5,8,13,21,34, ..."""


# In[2]:


'''使用递归生成斐波那契数列'''
n = input('Enter the number of terms:')
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
for i in range(int(n)):
    print(fibo(i),end=' ')


# In[3]:


'''使用循环、yield生成函数生成斐波那契数列'''
n = input('Enter the number of terms:')
def fibo(n):
    f0, f1 = 0, 1
    for _ in range(int(n)):
        yield f0
        f0, f1 = f1, f0+f1
fibs = list(fibo(int(n)))
print(fibs)


# In[4]:


'''使用yield生成函数生成斐波那契数列'''
n = input('Enter the number of terms:')
def fibo():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1
fibs = fibo()
for _ in range(int(n)):
    print (next(fibs), ',',end='')


# In[5]:


'''使用Lambda, Reduce函数生成斐波那契数列'''
from functools import reduce
n = input('Enter the number of terms:')
def fibo(n):
    '''reduce函数返回的数为list，x+[x[-1]+x[-2]]是列表相加，range确定次数,[0,1]是初始值'''
    return reduce(lambda x, _: x+[x[-1]+x[-2]],range(int(n)-2), [0,1])
print(fibo(int(n)))


# In[6]:


'''使用Lambda, Map函数生成斐波那契数列'''
n = input('Enter the number of terms:')
def fibo(n):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, n)))
    return fib_list[:n]

print(fibo(int(n)))


# In[7]:


'''使用Lambda, Map函数生成斐波那契数列'''
#n = input('Enter the number of terms:')
def fibo(n):
    fib_list = [0, 1]
    list(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, n)))
    return fib_list[:n]

print(fibo(11))


# In[ ]:




