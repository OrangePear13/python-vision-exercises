import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

lake = mpimg.imread('lake.jpg')

vectorized = lake.reshape((-1, 3))
vectorized = np.float32(vectorized)

term_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

#3
_3, label3, center3 = cv2.kmeans(vectorized, 3, bestLabels=None,
criteria=term_criteria, attempts=10, flags=0)

result3 = np.uint8(center3)[label3.flatten()]
result3 = result3.reshape((lake.shape))

#5
_5, label5, center5 = cv2.kmeans(vectorized, 5, bestLabels=None,
criteria=term_criteria, attempts=10, flags=0)

result5 = np.uint8(center5)[label5.flatten()]
result5 = result5.reshape((lake.shape))

#7
_7, label7, center7 = cv2.kmeans(vectorized, 7, bestLabels=None,
criteria=term_criteria, attempts=10, flags=0)

result7 = np.uint8(center7)[label7.flatten()]
result7 = result7.reshape((lake.shape))

plt.imsave('exercise-6-3.jpg', result3)
plt.imsave('exercise-6-5.jpg', result5)
plt.imsave('exercise-6-7.jpg', result7)

plt.imshow(result7)
plt.show()