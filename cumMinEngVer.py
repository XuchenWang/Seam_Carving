'''
  File name: cumMinEngVer.py
  Author: Xuchen Wang
  Date created: Oct 21, 2019
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''
import numpy as np

def cumMinEngVer(e):
    H = e.shape[0]
    W = e.shape[1]
    Mx = np.zeros([H,W])
    Tbx = np.zeros([H,W])
    Mx[0, :] = e[0, :]

    for h in range(1, H):
        Mx[h,0] = e[h,0] + min(Mx[h-1,0], Mx[h-1,1])
        Mx[h, W-1] = e[h, W-1] + min(Mx[h-1,W-2], Mx[h-1,W-1])
        Mx[h, 1:(W-1)] = e[h, 1:(W-1)] + np.array([Mx[h-1, 0:(W-2)], Mx[h-1, 1:(W-1)], Mx[h-1, 2:W]]).min(0)

        Tbx[h,0] = np.argmin([Mx[h-1,0], Mx[h-1,1]])
        Tbx[h, W-1] = np.argmin([Mx[h-1,W-2], Mx[h-1,W-1]])-1
        Tbx[h, 1:(W-1)] = np.argmin([Mx[h-1, 0:(W-2)], Mx[h-1, 1:(W-1)], Mx[h-1, 2:W]], axis=0) -1

    return Mx, Tbx


