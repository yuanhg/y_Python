# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 08:16:05 2020
本程序用于记录2020年一年内股票账户空仓情况

@author: faqui
"""

import json
from datetime import datetime


#如果没有days.json文件，则创建；如有，则读入
try:
    with open('D://github//y_Python//bull_bear_days.json', 'r') as f:
        bull_bear_days = json.load(f)
except FileNotFoundError:
    bull_bear_days = {
        'bear_days': 0,
        'bull_days': 0,
        'bull_bear': [{'bull': '2020/01/01'}, 
                      ]
        }

    with open('D://github//y_Python//bull_bear_days.json', 'w') as f:
        json.dump(bull_bear_days, f)
else:
    print('All is done')


date = datetime.now()
date_str = date.strftime( '%Y/%m/%d' ) 

bull_bear = True
    
bull_bear_days['bull_bear'].append({'bear': date_str})

#tuple(int(x) for x in date.strftime( '%m/%d').split('/'))

{'bear':'2020/01/07'}



def trading_days(dt1, dt2):
    '''判断两个日期间的交易日数，含最后一个日期
    两个日期间的天数 - 周末 - 法定节假日'''
    
    holidays = ['2020/01/01', '2020/01/24', '2020/01/27', '2020/01/28', '2020/01/29', '2020/01/30', 
                '2020/04/06', '2020/05/01', '2020/05/04', '2020/05/05', '2020/06/25', '2020/06/26',
                '2020/10/01', '2020/10/02', '2020/10/05', '2020/10/06', '2020/10/07', '2020/10/08']
    
    """    
    holidays : {
            'month': ['01', '04', '05', '06', '10'],
            '01': ['01', '24', '27', '28', '29', '30'],
            '04': ['06'],
            '05': ['01', '04', '05'],
            '06': ['25', '26'],
            '10': ['01', '02', '05', '06', '07', '08']
            }
        
    dt1mon = dt1[5:7] #取得日期的单独月、日
    dt1day = dt1[8:]
    
    dt2mon = dt2[5:7]
    dt2day = dt2[8:]
    
    """
    #取出两个日期的数字范围，看假期是否在这个范围内，如在，则假期计数+1
    dt1num = int(''.join(dt1.split('/')))
    dt2num = int(''.join(dt2.split('/')))
    
    holiday_counts = 0
    
    for holiday in holidays:
        holiday_num = int(''.join(holiday.split('/')))
        if dt1num <= holiday_num and holiday_num <= dt2num :
            holiday_counts +=1
    
    #计算两个日期间的工作天数
    date1 = datetime.strptime(dt1,'%Y/%m/%d') #字符串日期转换datetiem格式
    date2 = datetime.strptime(dt2,'%Y/%m/%d')
    
    days1 = int(date1.strftime('%j')) 
    weekend_days1 = (days1 + 2) //7 *2 
    if date1.strftime('%a') == 'Sat' :  weekend_days1 += 1
    
    days2 = int(date2.strftime('%j'))
    weekend_days2 = (days2 + 2) //7 *2 
    if date2.strftime('%a') == 'Sat' :  weekend_days2 += 1
    
    #计算两个日期间的交易天数
    trading_days = (days2 - weekend_days2) - (days1 - weekend_days1) - holiday_counts
    
    return trading_days


def is_trading_day(date):
    '''判断date是否交易日，是返回true'''
    holidays = [(1, 1), (1, 24), (1, 27), (1, 28), (1, 29), (1, 30), 
                (4, 6), (5, 1), (5, 4), (5, 5), (6, 25), (6, 26),
                (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (10, 8)]
    
    change_days_off = [(1, 19), (2, 1), (4, 26), (5, 9), (6, 28), (9, 27), (10, 10)]
    
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if date in holidays: return False #节假日
    
    days = date[1] + sum(month_days[:(date[0] -1)])
    if ((days + 2) % 7) and ((days + 3) % 7)  == 0: return False #周六、日
    return True