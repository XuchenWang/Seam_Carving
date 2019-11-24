'''
  File name: imageCarving.py
  Author: Xuchen Wang
  Date created:
'''
import numpy as np
from PIL import Image
import scipy.misc
from carv import carv


def main(I):
    nr = 20
    nc = 20
    I = scipy.misc.imresize(I,[420,600])
    scipy.misc.imsave('1_infile.jpg', I)
    carv(I, nr, nc)

if __name__ == "__main__":
    I = np.array(Image.open('1_try.jpg').convert('RGB'))
    main(I)
