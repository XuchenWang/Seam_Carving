'''
  File name: rmVerSeam.py
  Author: Xuchen Wang
  Date created: Oct 21, 2019
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''

import numpy as np

def rmVerSeam(I, Mx, Tbx):
    Ix0 = I[:,:,0].copy().flatten() # flatten the matrix with col major for red
    Ix1 = I[:,:,1].copy().flatten() # flatten the matrix with col major for green
    Ix2 = I[:,:,2].copy().flatten() # flatten the matrix with col major for blue

    H = I.shape[0]
    W = I.shape[1]
    currW = np.argmin(Mx[H-1,:])
    currH = H-1
    E = min(Mx[H-1,:])

    while (currH != -1):
        direction = Tbx[int(currH), int(currW)]
        Ix0 = np.delete(Ix0, int(currH*W+currW))
        Ix1 = np.delete(Ix1, int(currH*W+currW))
        Ix2 = np.delete(Ix2, int(currH*W+currW))
        currH -= 1
        currW += direction

    Ix0 = Ix0.reshape([H, W-1])
    Ix1 = Ix1.reshape([H, W-1])
    Ix2 = Ix2.reshape([H, W-1])
    Ix = np.stack([Ix0,Ix1,Ix2],axis=2)
    return Ix, E
