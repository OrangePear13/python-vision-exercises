import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

besties = mpimg.imread('trump-putin.jpg')

besties[52:, :395] = [0, 0, 0]
besties[25:, 625:] = [0, 0, 0]

plt.imsave('exercise-2.jpg', besties)

plt.imshow(besties)
plt.show()