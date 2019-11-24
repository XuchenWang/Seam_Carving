'''
  File name: rmHorSeam.py
  Author: Xuchen Wang
  Date created: Oct 21, 2019
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''

import numpy as np

def rmHorSeam(I, My, Tby):
    # Your Code Here
    Iy0 = I[:,:,0].copy().flatten('F') # flatten the matrix with col major for red
    Iy1 = I[:,:,1].copy().flatten('F') # flatten the matrix with col major for green
    Iy2 = I[:,:,2].copy().flatten('F') # flatten the matrix with col major for blue

    H = I.shape[0]
    W = I.shape[1]
    currW = W-1
    currH = np.argmin(My[:,W-1])
    E = min(My[:,W-1])

    while (currW != -1):
        direction = Tby[int(currH), int(currW)]
        Iy0 = np.delete(Iy0, int(currW*H+currH))
        Iy1 = np.delete(Iy1, int(currW*H+currH))
        Iy2 = np.delete(Iy2, int(currW*H+currH))
        currW -= 1
        currH += direction

    Iy0 = Iy0.reshape([H-1, W], order='F')
    Iy1 = Iy1.reshape([H-1, W], order='F')
    Iy2 = Iy2.reshape([H-1, W], order='F')
    Iy = np.stack([Iy0,Iy1,Iy2],axis=2)
    return Iy, E

