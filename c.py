import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

a = mpimg.imread('striped-leaf-pattern-0.jpg')
b = mpimg.imread('striped-leaf-pattern-1.jpg')

a = np.where(a == 0, b, a)

plt.imsave('exercise-3.jpg', a)

plt.imshow(a)
plt.show()