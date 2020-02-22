#!/usr/bin/env python
# coding: utf-8

import json

from datetime import datetime
import calendar
import tkinter as tk
from tkinter import ttk

from tkinter.tix import Tk, Button, Balloon, Label, Entry #升级的组合控件包

#from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
from tkinter.constants import *

import tkinter.font as tkFont



def trading_days(dt1, dt2):
    '''判断两个日期间的交易日数，含最后一个日期
    两个日期间的天数 - 周末 - 法定节假日'''
    
    holidays = ['2020-01-01', '2020-01-24', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', 
                '2020-04-06', '2020-05-01', '2020-05-04', '2020-05-05', '2020-06-25', '2020-06-26',
                '2020-10-01', '2020-10-02', '2020-10-05', '2020-10-06', '2020-10-07', '2020-10-08']
    
    #取出两个日期的数字范围，看假期是否在这个范围内，如在，则假期计数+1
    dt1num = int(''.join(dt1.split('-')))
    dt2num = int(''.join(dt2.split('-')))
    
    holiday_counts = 0
    
    for holiday in holidays:
        holiday_num = int(''.join(holiday.split('-')))
        if dt1num <= holiday_num and holiday_num <= dt2num :
            holiday_counts +=1
    
    #计算两个日期间的工作天数
    date1 = datetime.strptime(dt1,'%Y-%m-%d') #字符串日期转换datetiem格式
    date2 = datetime.strptime(dt2,'%Y-%m-%d')
    
    days1 = int(date1.strftime('%j')) 
    weekend_days1 = (days1 + 2) //7 *2 
    if date1.strftime('%a') == 'Sat' :  weekend_days1 += 1
    
    days2 = int(date2.strftime('%j'))
    weekend_days2 = (days2 + 2) //7 *2 
    if date2.strftime('%a') == 'Sat' :  weekend_days2 += 1
    
    #计算两个日期间的交易天数
    trading_days = (days2 - weekend_days2) - (days1 - weekend_days1) - holiday_counts
    
    return trading_days


#如果没有bull_bear_days.json文件，则创建；如有，则读入
try:
    with open('bull_bear_days.json', 'r') as f:     
#    with open('C://Users//faqui//Documents//github//y_Python//bull_bear_days.json', 'r') as f:
        bull_bear_days = json.load(f)
except FileNotFoundError:
    bull_bear_days = {
        'bull_days': 0,
        'bear_days': 0,
        'bull_bear':'bull',
        'bull_bear_day': ['2020-01-01',]
        }

    with open('bull_bear_days.json', 'w') as f:
#    with open('C://Users//faqui//Documents//github//y_Python//bull_bear_days.json', 'w') as f:
        json.dump(bull_bear_days, f)
else:
    pass


root = Tk() # 初始化Tk()  root便是你布局的根节点了，以后的布局都在它之上

root.title("行者桑结") # 设置窗口标题

width = root.winfo_reqwidth() + 400 #窗口大小
height = root.winfo_reqheight() + 100 #窗口大小
x, y = (root.winfo_screenwidth()  - width )/2, (root.winfo_screenheight() - height)/2
#root.attributes("-toolwindow", 1)  #参数1，设置工具栏样式窗口。#参数1，没有最大化和最小化的按钮。
#root["background"] = "DarkBlue"
root["bd"] = 4
root["relief"] = GROOVE #RAISED
root.geometry('%dx%d+%d+%d' % (width, height, x, y ) ) #窗口位置居中,设置窗口大小 注意：是x 不是*

root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

root.tk.eval('package require Tix') #引入升级包，这样才能使用升级的组合控件

#创建一个状态显示标签
info_status = Label(root, width=300, relief=GROOVE, font=("Arial",13), fg='red', bd=1, anchor = SW)
info_status.place(x=0,y=0, relx=0/20,rely=7/8, relwidth=20/20,relheigh=3/30,anchor=NW)


class Calendar:

    def __init__(s, point = None, position = None):
        # point    提供一个基点，来确定窗口位置
        # position 窗口在点的位置 'ur'-右上, 'ul'-左上, 'll'-左下, 'lr'-右下
        #s.master = tk.Tk()
        s.master = tk.Toplevel()
        s.master.withdraw()
        fwday = calendar.SUNDAY

        year = datetime.now().year
        month = datetime.now().month
        locale = None
        sel_bg = '#ecffc4'
        sel_fg = '#05640e'

        s._date = datetime(year, month, 1)
        s._selection = None # 设置为未选中日期

        s.G_Frame = ttk.Frame(s.master)

        s._cal = s.__get_calendar(locale, fwday)

        s.__setup_styles()       # 创建自定义样式
        s.__place_widgets()      # pack/grid 小部件
        s.__config_calendar()    # 调整日历列和安装标记
        # 配置画布和正确的绑定，以选择日期。
        s.__setup_selection(sel_bg, sel_fg)

        # 存储项ID，用于稍后插入。
        s._items = [s._calendar.insert('', 'end', values='') for _ in range(6)]

        # 在当前空日历中插入日期
        s._update()

        s.G_Frame.pack(expand = 1, fill = 'both')
        s.master.overrideredirect(1)
        s.master.update_idletasks()
        width, height = s.master.winfo_reqwidth(), s.master.winfo_reqheight()
        if point and position:
            if   position == 'ur': x, y = point[0], point[1] - height
            elif position == 'lr': x, y = point[0], point[1]
            elif position == 'ul': x, y = point[0] - width, point[1] - height
            elif position == 'll': x, y = point[0] - width, point[1]
        else: x, y = (s.master.winfo_screenwidth() - width)/2, (s.master.winfo_screenheight() - height)/2
        s.master.geometry('%dx%d+%d+%d' % (width, height, x, y)) #窗口位置居中
        s.master.after(300, s._main_judge)
        s.master.deiconify()
        s.master.focus_set()
        s.master.wait_window() #这里应该使用wait_window挂起窗口，如果使用mainloop,可能会导致主程序很多错误

    def __get_calendar(s, locale, fwday):
        # 实例化适当的日历类
        if locale is None:
            return calendar.TextCalendar(fwday)
        else:
            return calendar.LocaleTextCalendar(fwday, locale)

    def __setitem__(s, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            s._canvas['background'] = value
        elif item == 'selectforeground':
            s._canvas.itemconfigure(s._canvas.text, item=value)
        else:
            s.G_Frame.__setitem__(s, item, value)

    def __getitem__(s, item):
        if item in ('year', 'month'):
            return getattr(s._date, item)
        elif item == 'selectbackground':
            return s._canvas['background']
        elif item == 'selectforeground':
            return s._canvas.itemcget(s._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(s, item)})
            return r[item]

    def __setup_styles(s):
        # 自定义TTK风格
        style = ttk.Style(s.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(s):
        # 标头框架及其小部件
        Input_judgment_num = s.master.register(s.Input_judgment)  # 需要将函数包装一下，必要的
        hframe = ttk.Frame(s.G_Frame)
        gframe = ttk.Frame(s.G_Frame)
        bframe = ttk.Frame(s.G_Frame)
        hframe.pack(in_=s.G_Frame, side='top', pady=5, anchor='center')
        gframe.pack(in_=s.G_Frame, fill=tk.X, pady=5)
        bframe.pack(in_=s.G_Frame, side='bottom', pady=5)

        lbtn = ttk.Button(hframe, style='L.TButton', command=s._prev_month)
        lbtn.grid(in_=hframe, column=0, row=0, padx=12)
        rbtn = ttk.Button(hframe, style='R.TButton', command=s._next_month)
        rbtn.grid(in_=hframe, column=5, row=0, padx=12)
        
        s.CB_year = ttk.Combobox(hframe, width = 5, values = [str(year) for year in range(datetime.now().year, datetime.now().year-11,-1)], validate = 'key', validatecommand = (Input_judgment_num, '%P'))
        s.CB_year.current(0)
        s.CB_year.grid(in_=hframe, column=1, row=0)
        s.CB_year.bind('<KeyPress>', lambda event:s._update(event, True))
        s.CB_year.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text = '年', justify = 'left').grid(in_=hframe, column=2, row=0, padx=(0,5))

        s.CB_month = ttk.Combobox(hframe, width = 3, values = ['%02d' % month for month in range(1,13)], state = 'readonly')
        s.CB_month.current(datetime.now().month - 1)
        s.CB_month.grid(in_=hframe, column=3, row=0)
        s.CB_month.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text = '月', justify = 'left').grid(in_=hframe, column=4, row=0)

        # 日历部件
        s._calendar = ttk.Treeview(gframe, show='', selectmode='none', height=7)
        s._calendar.pack(expand=1, fill='both', side='bottom', padx=5)

        ttk.Button(bframe, text = "确 定", width = 6, command = lambda: s._exit(True)).grid(row = 0, column = 0, sticky = 'ns', padx = 20)
        ttk.Button(bframe, text = "取 消", width = 6, command = s._exit).grid(row = 0, column = 1, sticky = 'ne', padx = 20)
        
        
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 1, relheigh = 2/200)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 198/200, relwidth = 1, relheigh = 2/200)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 2/200, relheigh = 1)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 198/200, rely = 0, relwidth = 2/200, relheigh = 1)

    def __config_calendar(s):
        # cols = s._cal.formatweekheader(3).split()
        cols = ['日','一','二','三','四','五','六']
        s._calendar['columns'] = cols
        s._calendar.tag_configure('header', background='grey90')
        s._calendar.insert('', 'end', values=cols, tag='header')
        # 调整其列宽
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            s._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='center')

    def __setup_selection(s, sel_bg, sel_fg):
        def __canvas_forget(evt):
            canvas.place_forget()
            s._selection = None

        s._font = tkFont.Font()
        s._canvas = canvas = tk.Canvas(s._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<Button-1>', __canvas_forget)
        s._calendar.bind('<Configure>', __canvas_forget)
        s._calendar.bind('<Button-1>', s._pressed)

    def _build_calendar(s):
        year, month = s._date.year, s._date.month

        # update header text (Month, YEAR)
        header = s._cal.formatmonthname(year, month, 0)

        # 更新日历显示的日期
        cal = s._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(s._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            s._calendar.item(item, values=fmt_week)

    def _show_select(s, text, bbox):
        """为新的选择配置画布。"""
        x, y, width, height = bbox

        textw = s._font.measure(text)

        canvas = s._canvas
        canvas.configure(width = width, height = height)
        canvas.coords(canvas.text, (width - textw)/2, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=s._calendar, x=x, y=y)

    def _pressed(s, evt = None, item = None, column = None, widget = None):
        """在日历的某个地方点击。"""
        if not item:
            x, y, widget = evt.x, evt.y, evt.widget
            item = widget.identify_row(y)
            column = widget.identify_column(x)

        if not column or not item in s._items:
            # 在工作日行中单击或仅在列外单击。
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # 这个月的行是空的。
            return

        text = item_values[int(column[1]) - 1]
        if not text: # 日期为空
            return

        bbox = widget.bbox(item, column)
        if not bbox: # 日历尚不可见
            s.master.after(20, lambda : s._pressed(item = item, column = column, widget = widget))
            return

        # 更新，然后显示选择
        text = '%02d' % text
        s._selection = (text, item, column)
        s._show_select(text, bbox)

    def _prev_month(s):
        """更新日历以显示前一个月。"""
        s._canvas.place_forget()
        s._selection = None

        s._date = s._date - timedelta(days=1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _next_month(s):
        """更新日历以显示下一个月。"""
        s._canvas.place_forget()
        s._selection = None

        year, month = s._date.year, s._date.month
        s._date = s._date + timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _update(s, event = None, key = None):
        """刷新界面"""
        if key and event.keysym != 'Return': return
        year = int(s.CB_year.get())
        month = int(s.CB_month.get())
        if year == 0 or year > 9999: return
        s._canvas.place_forget()
        s._date = datetime(year, month, 1)
        s._build_calendar() # 重建日历

        if year == datetime.now().year and month == datetime.now().month:
            day = datetime.now().day
            for _item, day_list in enumerate(s._cal.monthdayscalendar(year, month)):
                if day in day_list:
                    item = 'I00' + str(_item + 2)
                    column = '#' + str(day_list.index(day)+1)
                    s.master.after(100, lambda :s._pressed(item = item, column = column, widget = s._calendar))

    def _exit(s, confirm = False):
        """退出窗口"""
        if not confirm: s._selection = None
        s.master.destroy()

    def _main_judge(s):
        """判断窗口是否在最顶层"""
        try:
            #s.master 为 TK 窗口
            #if not s.master.focus_displayof(): s._exit()
            #else: s.master.after(10, s._main_judge)

            #s.master 为 toplevel 窗口
            if s.master.focus_displayof() == None or 'toplevel' not in str(s.master.focus_displayof()): s._exit()
            else: s.master.after(10, s._main_judge)
        except:
            s.master.after(10, s._main_judge)

        #s.master.tk_focusFollowsMouse() # 焦点跟随鼠标

    def selection(s):
        """返回表示当前选定日期的日期时间。"""
        if not s._selection: return None

        year, month = s._date.year, s._date.month
        return str(datetime(year, month, int(s._selection[0])))[:10]

    def Input_judgment(s, content):
        """输入判断"""
        # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
        if content.isdigit() or content == "":
            return True
        else:
            return False


def set_var(date_str_now):
    global date_str, bull_bear_days
    #button的变量
    global bull_button_state, bull_button_relief, bull_button_bg, bull_button_fg
    global bear_button_state, bear_button_relief, bear_button_bg, bear_button_fg
    #label的变量
    global bull_text, bull_relwidth, bull_label_bg, bull_label_fg 
    global bear_text, bear_relx, bear_relwidth, bear_label_bg, bear_label_fg 
    global bull_bear_text, bull_bear_relx, bull_bear_relwidth 
    
    #文件记录   
    date_str_last = bull_bear_days['bull_bear_day'][-1]
    days = trading_days(date_str_last, date_str_now) 
    if days < 0 : days = 0 
    bull_days = 0
    bear_days = 0
    if bull_bear_days['bull_bear'] == 'bull': 
        bull_days = bull_bear_days['bull_days'] + days
        bear_days = bull_bear_days['bear_days']
    if bull_bear_days['bull_bear'] == 'bear': 
        bull_days = bull_bear_days['bull_days']
        bear_days = bull_bear_days['bear_days'] + days
        
    #默认显示当天日期
    date_str.set(date_str_now) 

    #设置色条上字符串text，初始位置，长度等变量初始化值
    all_days = 243

    bull_text.set(str(bull_days))
    bear_text.set(str(bear_days))
    bull_bear_text.set(str(all_days - bull_days - bear_days))

    bull_relwidth=bull_days/243

    bear_relx = (bull_days + 20)/243
    bear_relwidth=bear_days/243

    bull_bear_relx = (bull_days + bear_days + 20)/243
    bull_bear_relwidth=(all_days - bull_days - bear_days -40 )/243
    
    #设置按钮状态, 色条现实状态
    if bull_bear_days['bull_bear'] == 'bull':
        bull_button_state = DISABLED
        bull_button_relief = SUNKEN 
        bull_button_bg = 'Red'
        bull_button_fg = 'White'  
        bull_label_bg = 'Red'
        bull_label_fg = 'White'          
        bear_button_state = NORMAL
        bear_button_relief = RAISED
        bear_button_bg = 'DarkGreen'
        bear_button_fg = 'Black'    
        bear_label_bg = 'DarkGreen'
        bear_label_fg = 'White'
        
    if bull_bear_days['bull_bear'] == 'bear':
        bear_button_state = DISABLED
        bear_button_relief = SUNKEN
        bear_button_bg = 'Green'
        bear_button_fg = 'White'
        bear_label_bg = 'Green'
        bear_label_fg = 'White'        
        bull_button_state = NORMAL
        bull_button_relief = RAISED 
        bull_button_bg = 'DarkRed'
        bull_button_fg = 'Black'
        bull_label_bg = 'DarkRed'
        bull_label_fg = 'Black'
        

date = datetime.now()
date_str_now = date.strftime( '%Y-%m-%d' )

#日期、状态字符串变量
date_str = tk.StringVar()
bull_bear_str = bull_bear_days['bull_bear']

#色条上字符串变量
bull_text = tk.StringVar()
bear_text = tk.StringVar()
bull_bear_text = tk.StringVar()

#设置按钮、色条等参数
set_var(date_str_now)


#实现日期选择按钮，以及日期输入。通过气球和状态栏说明操作说明
#Calendar((x, y), 'ur').selection() 获取日期，x,y为点坐标
def date_str_gain():
    for date in [Calendar((x, y), 'ur').selection()]:
        if date:
            date_str.set(date)
            set_var(date)
            
date = Entry(root, textvariable = date_str, bd=2
            ).place(x=0,y=0, relx=5/20,rely=1/8, relwidth=6/20,relheigh=3/30)
            
date_button = Button(root, text = '转换日期:', command = date_str_gain, 
                     relief = SUNKEN, font = ("Arial",11), bd = 2 )
date_button.place(x=0,y=0, relx=2/20,rely=1/8, relwidth=3/20,relheigh=3/30)

date_balloon = Balloon(root, statusbar=info_status)
date_balloon.bind_widget(date_button, balloonmsg='', statusmsg='说明：点按这个按钮设置日期。')


#实现交易转换按钮
def bull_bear_button_call():
    global bull_label, bear_label, bull_bear_str
    if bull_button.configure('relief')[-1] == SUNKEN:
        bull_button.configure(state=NORMAL, fg="black", relief=RAISED, bg='DarkRed')
        bull_label.configure(bg='DarkRed', fg='black')
        bear_button.configure(state=DISABLED, relief=SUNKEN, bg='green')
        bear_label.configure(bg='green', fg='white')
        bull_bear_str = 'bear'
    else:
        bull_button.configure(state=DISABLED, fg="black", relief=SUNKEN, bg='red')
        bull_label.config(bg='Red', fg='white')
        bear_button.configure(state=NORMAL, fg="black", relief=RAISED, bg='DarkGreen')
        bear_label.configure(bg='DarkGreen', fg='black')
        bull_bear_str = 'bull'

#转换按钮
bull_button = Button(root, text='BULL', bg=bull_button_bg, fg=bull_button_fg, state=bull_button_state, relief=bull_button_relief,
                     activebackground = "red", activeforeground = "black", disabledforeground = "white", 
                     bd=5, font=("Arial",12), width=6, 
                     command = bull_bear_button_call)
bull_button.place(x=0,y=0, relx=2/20, rely=2.5/8, relwidth=2/20, relheigh=5/30, anchor=NW)

bull_balloon = Balloon(root, statusbar=info_status)
bull_balloon.bind_widget(bull_button, balloonmsg='', statusmsg='说明：点按这个按钮,改变牛熊状态：红色代表牛，绿色代表熊。')

bear_button = Button(root, text='BEAR', bg=bear_button_bg, fg=bear_button_fg, state=bear_button_state, relief=bear_button_relief,
                     activebackground = "green", activeforeground = "black", disabledforeground = "white", 
                     bd=5, font=("Arial",12), width=6, 
                     command = bull_bear_button_call)
bear_button.place(x=0,y=0, relx=4/20, rely=2.5/8, relwidth=2/20, relheigh=5/30, anchor=NW)

bear_balloon = Balloon(root, statusbar=info_status)
bear_balloon.bind_widget(bear_button, balloonmsg='', statusmsg='说明：点按这个按钮,改变牛熊状态：红色代表牛，绿色代表熊。')

#交易使用红色和绿色色条表示交易的进展
bull_label = Label(root, textvariable = bull_text, relief=SUNKEN, bg=bull_label_bg, fg=bull_label_fg, bd=0, anchor=CENTER)
bull_label.place(x=0,y=0, relx=20/243,rely=4/8, relwidth=bull_relwidth, relheigh=4/30)

bear_label = Label(root, textvariable = bear_text, relief=SUNKEN, bg=bear_label_bg, fg=bear_label_fg,bd=0, anchor=CENTER)
bear_label.place(x=0,y=0, relx=bear_relx,rely=4/8, relwidth=bear_relwidth, relheigh=4/30)

bull_bear_label = Label(root, textvariable = bull_bear_text, anchor=CENTER,  relief=SUNKEN, bg='gray', bd=2
                ).place(x=0,y=0, relx=bull_bear_relx, rely=4/8, relwidth=bull_bear_relwidth, relheigh=4/30)

#退出按钮

#保存设定的数据到文件
def set_json():
    global bull_bear_days, date_str, bull_bear_str
    
    if bull_bear_days['bull_bear'] != bull_bear_str :
        days = trading_days(bull_bear_days['bull_bear_day'][-1], date_str.get())
        if bull_bear_days['bull_bear'] == 'bull': bull_bear_days['bull_days'] += days
        if bull_bear_days['bull_bear'] == 'bear': bull_bear_days['bear_days'] += days
    
        bull_bear_days['bull_bear'] = bull_bear_str
        bull_bear_days['bull_bear_day'].append(date_str.get())
        
        with open('bull_bear_days.json', 'w') as f:       
#        with open('C://Users//faqui//Documents//github//y_Python//bull_bear_days.json', 'w') as f:
            json.dump(bull_bear_days, f)
        
    root.destroy()
    
quit_button = Button(root, text = '保存退出:', command = set_json, 
                     relief = RAISED, font = ("Arial",12), bd = 3
                    ).place(x=0,y=0, relx=2/20,rely=6/8, relwidth=3/20,relheigh=3/30)    

root.mainloop()

