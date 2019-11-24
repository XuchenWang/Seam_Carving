'''
  File name: carv.py
  Author: Xuchen Wang
  Date created:
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam, 
    sequentially and potentially along different directions.
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''
import numpy as np
import math
import scipy.misc
import imageio
from genEngMap import genEngMap
from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer
from rmHorSeam import rmHorSeam
from rmVerSeam import rmVerSeam


def carv(I, nr, nc):
    T = np.zeros([nr+1, nc+1])
    Trace = np.zeros([nr+1, nc+1]) #Trace matrix stores '1' if the current element comes from the upper element
                                    # stores '0' if comes from the left element
                                    # stores '0' at [0,0], just to fill the place
    Images = {}
    T, Trace, Images = recurvCarv(I, nr, nc, T, Trace, Images)

    img = Images[(nr, nc)]
    scipy.misc.imsave('1_outfile.jpg', img[:,:,:3])

    morph_list = []
    currR = nr
    currC = nc
    while not (currR == 0 and currC == 0):
        currDir = Trace[currR, currC]
        currImage = Images[(currR, currC)]
        morph_list.append(currImage[:,:,:3])
        if currDir == 0:  #get left
            currC = currC - 1
        elif currDir == 1:  #get upper
            currR = currR - 1
    morph_list.append(I)
    morph_list = morph_list[::-1]
    imageio.mimsave('./eval_curving.gif', morph_list)

    return img, T





def recurvCarv(I, nr, nc, T, Trace, Images):
    if nr==0 and nc==0:
        T[0,0] = 0
        Trace[0,0] = 0
        Images[(0,0)] = I
        return T, Trace, Images


    if nr==0:
        upper = math.inf
    else:
        if T[nr-1,nc] == 0:
            T, Trace, Images = recurvCarv(I, nr-1, nc, T, Trace, Images)
        upper = T[nr-1,nc]
        upperImage = Images[(nr-1,nc)]
        e = genEngMap(upperImage)
        My, Tby = cumMinEngHor(e)
        E = min(My[:,-1])
        upper = upper + E

    if nc==0:
        left = math.inf
    else:
        if T[nr,nc-1] == 0:
            T, Trace, Images = recurvCarv(I, nr, nc-1, T, Trace, Images)
        left = T[nr,nc-1]
        leftImage = Images[(nr,nc-1)]
        e = genEngMap(leftImage)
        Mx, Tbx = cumMinEngVer(e)
        E = min(Mx[-1,:])
        left = left + E

    if (upper >= left) :
        T[nr,nc] = left
        Trace[nr,nc] = 0
        Ix, E = rmVerSeam(leftImage, Mx, Tbx)
        Images[(nr, nc)] = Ix
    else:
        T[nr,nc] = upper
        Trace[nr,nc] = 1
        Iy, E = rmHorSeam(upperImage, My, Tby)
        Images[(nr, nc)] = Iy

    return T, Trace, Images




