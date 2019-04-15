# coding: utf-8
# Editor Yuan Honggang
# Copyright 1.0

# main data
#0表示未落子，1表示x落子，-1表示o落子，初始没有落子
#xo_lock  = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
#xo_value = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3}

# 使用字典initial map data
ttt = {}
#一个字典，表示1-9个下棋空位在字典ttt中的序号
dt = {1:15, 2:19, 3:23, 4:41, 5:45, 6: 49, 7:67, 8:71, 9:75}

def initialttt():
    for i in range(91):
        if i in [14,15,16,18,19,20,22,23,24,
             40,41,42,44,45,46,48,49,50,
             66,67,68,70,71,72,74,75,76]:
            ttt[i] = ' '
        else:
            ttt[i] = '*'
    for i in range(1, 10):
        ttt[dt[i]] = i
    
def showttt():
    for i in range(len(ttt)):
        if (i+1)%13 != 0:
            if ttt[i] == '*':
                print(' ', end='')
            else:
                print(ttt[i],  end='')
        else:
            if ttt[i] == '*':
                print(' ' )
            else:
                print(ttt[i])

# check if win
def checkwin():
    #检查行
    for i in range(1,8,3):
        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == 3:
            return 1
    #检查列
    for i in range(1,4):
        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == 3:
            return 1
    #检查斜线
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == 3:
        return 1
    if xo_lock[1] + xo_lock[5] + xo_lock[9] == 3:
        return 1
    
    #检查行
    for i in range(1,8,3):
        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == -3:
            return -1
    #检查列
    for i in range(1,4):
        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == -3:
            return -1
    #检查斜线
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == -3:
        return -1
    if xo_lock[1] + xo_lock[5] + xo_lock[9] == -3:
        return -1

    return 0

#lock xo, and revalue x_value and o_value
def lockrevalue(point=1, player='x'):
    if player == 'x':
        xo_lock[point] = 1
    if player == 'o':
        xo_lock[point] = -1
        
    #分别评估剩余空格对x、o两方的价值，计入x_value，o_value
    #行列如果有两子情况出现，则另一个空位是对双方来说价值最高的
    #行列如果有一子情况出现，则另两个个空位是对双方来说价值次高的
    
    #价值归初始状态
    #xo_value = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3}
    for i in range(1,10):
        if xo_lock[i] != 0:
            xo_value[i] = 0
            
    #判断3行中空位价值
    for i in range(1,8,3):
        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == 2 or xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == -2:
            for j in range(3):
                if xo_lock[i+j] == 0:
                    xo_value[i+j] += 99

        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == 1 or xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == -1:
            #如果存在两个空位，价值次高，否则价值不变
            if [xo_lock[i] , xo_lock[i+1] , xo_lock[i+2]].count(0) == 2:
                for j in range(3):
                    if xo_lock[i+j] == 0:
                        xo_value[i+j] += 33
                    
    #判断3列中空位价值，落子处价值归0
    for i in range(1,4):
        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == 2 or xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == -2:
            for j in range(0,7,3):
                if xo_lock[i+j] == 0:
                    xo_value[i+j] += 99

        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == 1 or xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == -1:
            #如果存在两个空位，价值次高，否则价值不变
            if [xo_lock[i] , xo_lock[i+3] , xo_lock[i+6]].count(0) == 2:
                for j in range(0,7,3):
                    if xo_lock[i+j] == 0:
                        xo_value[i+j] += 33
       
    #检查两条斜线
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == 2 or xo_lock[3] + xo_lock[5] + xo_lock[7] == -2:
        for j in range(3,8,2):
            if xo_lock[j] == 0:
                xo_value[j] += 99

    if xo_lock[1] + xo_lock[5] + xo_lock[9] == 2 or xo_lock[1] + xo_lock[5] + xo_lock[9] == -2:
        for j in range(1,10,4):
            if xo_lock[j] == 0:
                xo_value[j] += 99
                    
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == 1 or xo_lock[3] + xo_lock[5] + xo_lock[7] == -1:
        #如果存在两个空位，价值次高，否则价值不变
        if [xo_lock[3] , xo_lock[5] , xo_lock[7]].count(0) == 2:
            for j in range(3,8,2):
                if xo_lock[j] == 0:
                    xo_value[j] += 33

    if xo_lock[1] + xo_lock[5] + xo_lock[9] == 1 or xo_lock[1] + xo_lock[5] + xo_lock[9] == -1:
        #如果存在两个空位，价值次高，否则价值不变
        if [ xo_lock[1] , xo_lock[5] , xo_lock[9] ].count(0) == 2:
            for j in range(1,10,4):
                if xo_lock[j] == 0:
                    xo_value[j] += 33

# return point(i) available [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
def availablepoint():
    ap = 0
    max = 0
    for i in range(1,10):
        if xo_value[i] > max:
            max = xo_value[i]
            ap = i
    return ap

#开始运行程序


while True:
    print("请选择先手，输入x代表选手先走，输入o代表计算机先走，输入q退出游戏：")
    playerturn = input("请输入 x / o / q ：")
    xo_lock  = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    xo_value = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3}
    if playerturn == 'x':
        player = 'x'
        initialttt()
    elif playerturn == 'o':
        player = 'o'
        initialttt()
    else:
        break
    showttt()

    while True:
        if player == 'x':
            #检查可选剩余可选数字
            nums = []
            for i in range(1,10):
                if ttt[dt[i]] == i :
                    nums.append(i)
            if nums == []:
                print("平局")
                break

            print('请选手选择落子处的数字：', end='')
            playnum = int(input())
            if playnum not in nums:
                  continue
            ttt[dt[playnum]] = 'X'
            #showttt()
            lockrevalue(playnum, player)

            if checkwin() == 1:
                print('选手 赢')
                break
            player = 'o'

        if player == 'o':
            playnum = availablepoint()
            if playnum == 0:
                print('平局')
                break
            
            print('计算机选择（%s)落子' %(playnum))
            ttt[dt[playnum]] = 'Q'
            #showttt()
            lockrevalue(playnum,player)

            if checkwin() == -1:
                print('计算机 赢')
                break
            player = 'x'
            
        showttt()
