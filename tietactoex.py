#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Editor Yuan Honggang
# Copyright 1.0

xo_lock = [[0,0,0],[0,0,0],[0,0,0]]
x_value = [[3,2,3],[2,4,2],[3,2,3]]
o_value = [[3,2,3],[2,4,2],[3,2,3]]
xo_value = [[0,0,0],[0,0,0],[0,0,0]]
l_value = [0,0,0,0,0,0,0,0]
xo_point = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

# initial map
ttt = {}
for i in range(91):
    if i in [14,15,16,18,19,20,22,23,24,
             40,41,42,44,45,46,48,49,50,
             66,67,68,70,71,72,74,75,76]:
        ttt[i] = ' '
    else:
        ttt[i] = '*'

#一个字典，表示1-9个下棋空位在列表ttt中的序号
dt = {1:15, 2:19, 3:23, 4:41, 5:45, 6: 49, 7:67, 8:71, 9:75}

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


# In[2]:


# return point(i,j) available
def availablepoint():
    tt = []
    for i in range(3):
        for j in range(3):
            if xo_lock[i][j] == 0:
                tt.append([i,j])
    return tt


# In[3]:


#return the max value point selected in point available, one or more equal value
def alternativepoint(tt,player='x'):
    t = []
    xo_value = [max(x,y) for x,y in zip(o_value,x_value)]
   
    for i in range(len(tt)):
        t.append([xo_value[tt[i][0]][tt[i][1]],tt[i][0],tt[i][1]])
    '''sorted from Max to Min value'''
    
    t.sort(reverse=True)
    if len(t) == 1:
        '''if only one item , return it'''
        return t
    
    for i in range(len(t)):
        if t[i][0] > t[i+1][0]:
            return t[:i+1]
        if i+1 == len(t):
            return t


# In[4]:


#lock xo, and revalue x_value and o_value
def lockrevalue(p=[0,0], player='x'):
    if player == 'x':
        xo_lock[p[0]][p[1]] = 1
    if player == 'o':
        xo_lock[p[0]][p[1]] = -1
    
    l_value[0] = sum(xo_lock[0])
    l_value[1] = sum(xo_lock[1])
    l_value[2] = sum(xo_lock[2])
    l_value[3] = xo_lock[0][0]+xo_lock[0][1]+xo_lock[0][2]
    l_value[4] = xo_lock[1][0]+xo_lock[1][1]+xo_lock[1][2]
    l_value[5] = xo_lock[2][0]+xo_lock[2][1]+xo_lock[2][2]
    l_value[6] = xo_lock[0][0]+xo_lock[1][1]+xo_lock[2][2]
    l_value[7] = xo_lock[0][2]+xo_lock[1][1]+xo_lock[2][0]
    
    #print(l_value)
    
    if l_value[0] == 1:
        x_value[0][0] *= 2
        x_value[0][1] *= 2
        x_value[0][2] *= 2
    if l_value[0] == 2:
        x_value[0][0] *= 4
        x_value[0][1] *= 4
        x_value[0][2] *= 4
    if l_value[0] == -1:
        o_value[0][0] *= 2
        o_value[0][1] *= 2
        o_value[0][2] *= 2
    if l_value[0] == -2:
        o_value[0][0] *= 4
        o_value[0][1] *= 4
        o_value[0][2] *= 4
        
    if l_value[1] == 1:
        x_value[1][0] *= 2
        x_value[1][1] *= 2
        x_value[1][2] *= 2
    if l_value[1] == 2:
        x_value[1][0] *= 4
        x_value[1][1] *= 4
        x_value[1][2] *= 4
    if l_value[1] == -1:
        o_value[1][0] *= 2
        o_value[1][1] *= 2
        o_value[1][2] *= 2
    if l_value[1] == -2:
        o_value[1][0] *= 4
        o_value[1][1] *= 4
        o_value[1][2] *= 4
        
    if l_value[2] == 1:
        x_value[2][0] *= 2
        x_value[2][1] *= 2
        x_value[2][2] *= 2
    if l_value[2] == 2:
        x_value[2][0] *= 4
        x_value[2][1] *= 4
        x_value[2][2] *= 4
    if l_value[2] == -1:
        o_value[2][0] *= 2
        o_value[2][1] *= 2
        o_value[2][2] *= 2
    if l_value[2] == -2:
        o_value[2][0] *= 4
        o_value[2][1] *= 4
        o_value[2][2] *= 4
    
    if l_value[3] == 1:
        x_value[0][0] *= 2
        x_value[1][0] *= 2
        x_value[2][0] *= 2
    if l_value[3] == 2:
        x_value[0][0] *= 4
        x_value[1][0] *= 4
        x_value[2][0] *= 4
    if l_value[3] == -1:
        o_value[0][0] *= 2
        o_value[1][0] *= 2
        o_value[2][0] *= 2
    if l_value[3] == -2:
        o_value[0][0] *= 4
        o_value[1][0] *= 4
        o_value[2][0] *= 4
    
    if l_value[4] == 1:
        x_value[0][1] *= 2
        x_value[1][1] *= 2
        x_value[2][1] *= 2
    if l_value[4] == 2:
        x_value[0][1] *= 4
        x_value[1][1] *= 4
        x_value[2][1] *= 4
    if l_value[4] == -1:
        o_value[0][1] *= 2
        o_value[1][1] *= 2
        o_value[2][1] *= 2
    if l_value[4] == -2:
        o_value[0][1] *= 4
        o_value[1][1] *= 4
        o_value[2][1] *= 4
        
    if l_value[5] == 1:
        x_value[0][2] *= 2
        x_value[1][2] *= 2
        x_value[2][2] *= 2
    if l_value[5] == 2:
        x_value[0][2] *= 4
        x_value[1][2] *= 4
        x_value[2][2] *= 4
    if l_value[5] == -1:
        o_value[0][2] *= 2
        o_value[1][2] *= 2
        o_value[2][2] *= 2
    if l_value[5] == -2:
        o_value[0][0] *= 4
        o_value[1][0] *= 4
        o_value[2][0] *= 4
        
    if l_value[6] == 1:
        x_value[0][0] *= 2
        x_value[1][1] *= 2
        x_value[2][2] *= 2
    if l_value[6] == 2:
        x_value[0][0] *= 4
        x_value[1][1] *= 4
        x_value[2][2] *= 4
    if l_value[6] == -1:
        o_value[0][0] *= 2
        o_value[1][1] *= 2
        o_value[2][2] *= 2
    if l_value[6] == -2:
        o_value[0][0] *= 4
        o_value[1][1] *= 4
        o_value[2][2] *= 4
        
    if l_value[7] == 1:
        x_value[0][2] *= 2
        x_value[1][1] *= 2
        x_value[2][0] *= 2
    if l_value[7] == 2:
        x_value[0][2] *= 4
        x_value[1][1] *= 4
        x_value[2][0] *= 4
    if l_value[7] == -1:
        o_value[0][2] *= 2
        o_value[1][1] *= 2
        o_value[2][0] *= 2
    if l_value[7] == -2:
        o_value[0][2] *= 4
        o_value[1][1] *= 4
        o_value[2][0] *= 4
        
    

# In[5]:


#检查是否有选手获胜，即连成3连线
def win():
    if str(ttt[dt[1]]) + str(ttt[dt[2]]) + str(ttt[dt[3]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[2]]) + str(ttt[dt[3]]) == 'OOO':
        return 1
    if str(ttt[dt[4]]) + str(ttt[dt[5]]) + str(ttt[dt[6]]) == 'XXX' or str(ttt[dt[4]]) + str(ttt[dt[5]]) + str(ttt[dt[6]]) == 'OOO':
        return 1
    if str(ttt[dt[7]]) + str(ttt[dt[8]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[7]]) + str(ttt[dt[8]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[1]]) + str(ttt[dt[4]]) + str(ttt[dt[7]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[4]]) + str(ttt[dt[7]]) == 'OOO':
        return 1
    if str(ttt[dt[2]]) + str(ttt[dt[5]]) + str(ttt[dt[8]]) == 'XXX' or str(ttt[dt[2]]) + str(ttt[dt[5]]) + str(ttt[dt[8]]) == 'OOO':
        return 1
    if str(ttt[dt[3]]) + str(ttt[dt[6]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[3]]) + str(ttt[dt[6]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[1]]) + str(ttt[dt[5]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[5]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[3]]) + str(ttt[dt[5]]) + str(ttt[dt[7]]) == 'XXX' or str(ttt[dt[3]]) + str(ttt[dt[5]]) + str(ttt[dt[7]]) == 'OOO':
        return 1
    return 0


# In[6]:

showttt()
play = 0
xo = ['X', 'O']
while True:
    if play == 0:
        #检查可选剩余可选数字
        nums = []
        for i in range(1,10):
            if ttt[dt[i]] == i :
                nums.append(i)
        if nums == []:
            print("Nobody Win")
            break

        print('请(%s)选择落子处的数字：' %(xo[play]), end='')
        playnum = int(input())
        if playnum not in nums:
              continue
        ttt[dt[playnum]] = 'X'
        showttt()
        lockrevalue(xo_point[playnum],player='x')
        if win():
            print(xo[play], 'Player Win')
            break
        play = 1
        
    if play == 1:
        #print(xo_lock)
        tt = availablepoint()
        #print(tt)
        t = alternativepoint(tt,player='o')
        if t == None:
            break
        #print(t)
        p = [t[0][1],t[0][2]]
        #print(p)
        for i in range(1,10):
            if xo_point[i] == p:
                playnum = i
                print('计算机选择（%s)落子' %(playnum))
                #print(dt[playnum])
                ttt[dt[playnum]] = 'O'
                showttt()
                lockrevalue(xo_point[playnum],player='o')
                if win():
                    print(xo[play], 'Player Win')
                    break
                play = 0



