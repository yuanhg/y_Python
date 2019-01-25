#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/9/25
# @Author  : 圈圈烃
# @File    : NICT_download
# @Description: http://himawari8.nict.go.jp/ 向日葵8号卫星实时图片下载
#
#
from PIL import Image
import requests
import re
import datetime


def download_img(url, img_save_path):
    img = requests.get(url)
    with open(img_save_path, "wb") as fwi:
        fwi.write(img.content)
        print(img_save_path + "图片下载成功")


def fill_img(img, img_save_path):
    width, height = 1920, 1080      # 电脑屏幕大小
    new_img = Image.new(img.mode, (width, height), color='black')
    new_img.paste(img, (int(width/2 - 250), int(height/2 - 250)))
    new_img.save(img_save_path)
    print(img_save_path + "图片合成成功")


def dl_main():
    # 获取当前系统时间
    utc_today = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)  # 获取GMT时间并减去30分钟
    delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")  # 时间格式化
    # 分钟向下取整
    delat_utc_today_list = list(delat_utc_today)
    delat_utc_today_list[-1] = "0"
    delat_utc_today = "".join(delat_utc_today_list)
    # 整合为链接 格式为：http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/2018/09/25/065000_0_0.png
    img_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/" + delat_utc_today + "00_0_0.png"
    name = delat_utc_today.replace("/", "_") + "00_0_0.png"  # 获取图片名字
    # 图片保存路径
    img_save_path = "d:/wallpapers" + name
    new_img_save_path = "d:/wallpapers/f_" + name
    # 下载图片
    download_img(img_url, img_save_path)
    # 合成图片
    img = Image.open(img_save_path)
    fill_img(img, new_img_save_path)
    return new_img_save_path


if __name__ == '__main__':
    dl_main()

'''
--------------------- 
作者：圈圈烃 
来源：CSDN 
原文：https://blog.csdn.net/Q_QuanTing/article/details/82854444 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
