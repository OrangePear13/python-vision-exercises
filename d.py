import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

strawberry = mpimg.imread('strawberry.jpg')

strawberry_height, _1, _2 = strawberry.shape

sb1 = np.copy(strawberry)

sb1 = sb1[np.arange(0, strawberry_height, 2)]

sb1 = 255 - sb1

sb1 = np.flip(sb1, axis=1)

plt.imsave('exercise-4.jpg', sb1)

plt.imshow(sb1)
plt.show()