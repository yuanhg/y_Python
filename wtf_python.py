#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 'some_string'
id(a)


# In[2]:


id('some' + '_' + 'string')


# In[3]:


a = 'wtf'
b = 'wtf'
a is b


# In[4]:


a = 'wtf!'
b = 'wtf!'
a is b


# In[5]:


a, b = 'wtf!', 'wtf!'
a is b


# In[6]:


some_dict = {}
some_dict[5.5] = "Ruby"
some_dict[5.0] = "JavaScript"
some_dict[5] = "Python"
some_dict[5.5]
some_dict[5.0] is some_dict[5]


# In[7]:


'''当在 "try...finally" 语句的 try 中执行 return, break 或 continue 后, finally 子句依然会执行.'''
'''函数的返回值由最后执行的 return 语句决定. 由于 finally 子句一定会执行, 所以 finally 子句中的 return 将始终是最后执行的语句'''
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
    
some_func()


# In[8]:


some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    pass
some_dict


# In[9]:


for i in range(4):
    print(i)
    i = 10


# In[10]:


array_1 = [1,2,3,4]
g1 = (x for x in array_1)
array_1 = [1,2,3,4,5]

array_2 = [1,2,3,4]
g2 = (x for x in array_2)
array_2[:] = [1,2,3,4,5]

print(list(g1))
print(list(g2))


# In[11]:


array = [1, 8, 15]
g = (x for x in array if array.count(x) > 0)
#print(list(g))
array = [2, 8, 22]
print(list(g))


# In[12]:


array = [1, 8, 15]
g = (x for x in array if array.count(x) > 0)
print(list(g))
array = [2, 8, 22]
print(list(g))


# In[13]:


a = 256
b = 256
a is b


# In[14]:


a = 257
b = 257
a is b


# In[15]:


a = 257; b = 257
a is b


# In[16]:


# 我们先初始化一个变量row
row = [""]*3 #row i['', '', '']
# 并创建一个变量board
board = [row]*3
print(board)
board[0][0] = "X"
print(board)


# In[17]:


board = [['']*3 for _ in range(3)]
print(board)
board[0][0] = "X"
print(board)


# In[18]:


'something' is not None


# In[19]:


'something' is (not None)


# In[20]:


from datetime import datetime

midnight = datetime(2018, 1, 1, 0, 0)
midnight_time = midnight.time()

noon = datetime(2018, 1, 1, 12, 0)
noon_time = noon.time()

if midnight_time:
    print("Time at midnight is", midnight_time)

if noon_time:
    print("Time at noon is", noon_time)


# In[21]:


some_list = [1, 2, 3]
some_dict = {
  "key_1": 1,
  "key_2": 2,
  "key_3": 3
}

some_list = some_list.append(4)
some_dict = some_dict.update({"key_4": 4})

print(some_list)
print(some_dict)


# In[22]:


a, b = a[b] = {}, 5
a


# In[23]:


import numpy as np

def energy_send(x):
    # 初始化一个 numpy 数组
    np.array([float(x)])

def energy_receive():
    # 返回一个空的 numpy 数组
    return np.empty((), dtype=np.float).tolist()

energy_send(123.456)
energy_receive()


# In[24]:


a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]
print(a)
print(b)


# In[25]:


a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]
print(a)
print(b)


# In[ ]:





# In[ ]:




