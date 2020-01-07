# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 08:16:05 2020
本程序用于记录2020年一年内股票账户空仓情况

@author: faqui
"""


def is_trading_day(date):
    '''判断date是否交易日，是返回true'''
    holidays = [(1, 1), (1, 24), (1, 27), (1, 28), (1, 29), (1, 30), 
                (4, 6), (5, 1), (5, 4), (5, 5), (6, 25), (6, 26),
                (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (10, 8)]
    
    change_days_off = [(1, 19), (2, 1), (4, 26), (5, 9), (6, 28), (9, 27), (10, 10)]
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if date in holidays: return False #节假日
    days = date[1] + sum(month_days[:(date[0] -1)])
    if ((days + 2) % 7) and ((days + 3) % 7)  == 0: return False #周六、日
    return True

from datetime import datetime
date = datetime.now()
days = int(date.strftime('%j'))
weekend_days = (days + 2) //7 *2 #如果周六，+1天
date.strftime('%a') == 'Sat'




