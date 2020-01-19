#!/usr/bin/env python3 
# -*- coding: UTF-8 -*-


import os
import shutil
import hashlib
from PIL import Image

#确定存储文件夹，若不存在则创建
if os.path.exists('d:\\wallpapers')==False:
    os.mkdir('d:\\wallpapers')
wp_savepath = 'd:\\wallpapers'

#读取目录下的文件名，并将数字部分存储在一个list中，用于后面判断是否重复
wp_name_list = []
wp_names = os.listdir(wp_savepath)
for wp_name in wp_names:
    wp_name_list.append( wp_name[-8:-4] )

#动态获取系统存放壁纸图片的位置
wp_folder = os.getenv('LOCALAPPDATA')+(
    '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy'
    '\LocalState\Assets')

#列出所有文件，找到壁纸文件
wp_names = os.listdir(wp_folder)
for wp_name in wp_names:
    wp_path = os.path.join(wp_folder,wp_name)
    #文件太小则忽略
    if (os.path.getsize(wp_path)/1024) < 200 :
        continue
    #文件是竖图则忽略
    img=Image.open(wp_path)
    if img.width<img.height:
        continue
    #hashlib作为文件名，同时判断是否已经保存了这个壁纸文件
    md5=hashlib.md5()
    md5.update(wp_name.encode('utf-8'))
    md5_name = md5.hexdigest()
    '''转化为10进制后取后4位作为文件序号'''
    md5_name = str(int(md5_name,16)%10000)
    '''如果目录里有相同序号，说明这个壁纸文件已经存储了，忽略'''
    if md5_name in wp_name_list:
        continue
    '''构造新的存储文件名'''
    wp_name = 'wp_'+md5_name+ '.jpg'
    wp_savename=os.path.join(wp_savepath, wp_name)
    shutil.copyfile(wp_path, wp_savename)

