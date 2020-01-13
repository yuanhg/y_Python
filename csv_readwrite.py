#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import csv


# In[4]:


with open('D:\\data_files\\ownthink_v2.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for index, read in enumerate(reader):
        print(read)
        if index > 30: break  #sys.exit(0)


# In[26]:


import csv
def new_ownthink(lines=100):
    file_path = 'D:\\data_files\\ownthink_v2.csv'
    save_path = 'D:\\data_files\\ownthink_v0.csv'

    with open(file_path,'r',encoding='UTF-8') as fr:
        data = csv.reader(fr)   
        '''开始写文件'''
        with open(save_path,'w',newline='', encoding='UTF-8') as fs:
            writer = csv.writer(fs,dialect='excel')
            for index, read in enumerate(data):
                if index < lines:
                    writer.writerow(read)
                else:
                    break 
            print('All is done')
    with open('D:\\data_files\\ownthink_v0.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for index, read in enumerate(reader):
            print(read)
            if index > 30: break 


# In[27]:


new_ownthink()


# In[ ]:




