'''
  File name: cumMinEngHor.py
  Author: Xuchen Wang
  Date created: Oct 21, 2019
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
import numpy as np

def cumMinEngHor(e):
    H = e.shape[0]
    W = e.shape[1]
    My = np.zeros([H,W])
    Tby = np.zeros([H,W])
    My[:, 0] = e[:, 0]

    for w in range(1, W):
        My[0,w] = e[0,w] + min(My[0,w-1], My[1,w-1])
        My[H-1, w] = e[H-1,w] + min(My[H-2,w-1], My[H-1,w-1])
        My[1:(H-1),w] = e[1:(H-1),w] + np.array([My[0:(H-2),w-1], My[1:(H-1),w-1], My[2:H,w-1]]).min(0)

        Tby[0,w] = np.argmin([My[0,w-1], My[1,w-1]])
        Tby[H-1, w] = np.argmin([My[H-2,w-1], My[H-1,w-1]])-1
        Tby[1:(H-1),w] = np.argmin([My[0:(H-2),w-1], My[1:(H-1),w-1], My[2:H,w-1]], axis=0) -1

    return My, Tby




