import numpy as np

def showboard(nb):
    w = nb.shape[1]#列
    h = nb.shape[0]#行
    for i in range(h):
        for j in range(w):
            if nb[i][j] == 0:#未落子
                if i*w+j <10:
                    print('|  %d '%(i*w+j), end='')
                elif i*w+j <100:
                    print('| %d'%(i*w+j), end='')
                else:
                    print('|%d'%(i*w+j), end='')
            if nb[i][j] == 1:#x落子
                print('| X ', end='')
            if nb[i][j] == -1:#o落子
                print('| O ', end='')
            if j == w-1:
                print('|')
                for i in range(4*w):
                    if (i+1 == 4*w)!=0:
                        print('-')
                    else:
                        print('-', end='')


ox = np.zeros((9,9), dtype=int )
ox[4][5] = 1
showboard(ox)
