import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve
'''
test = np.zeros(shape=(8, 8))

test[2:4, 1:3] = 1
test[2:4, 5:7] = 1
test[4:5, 3:5] = 1
test[5:7, 2:6] = 1
test[([7, 7], [2, 5])] = 1

plt.imshow(test, cmap='gray')
plt.show()
'''

img = np.zeros(shape=(10, 10))
img[1:9, 1] = 1
img[1, 2:9] = 1
img[2:8, 8] = 1
img[7, 3:8] = 1
img[3:7, 3] = 1
img[3, 4:7] = 1
img[4:6, 6] = 1
img[5, 5] = 1

plt.imsave('exercise-1.jpg', img)

plt.imshow(img, cmap='gray')
plt.show()