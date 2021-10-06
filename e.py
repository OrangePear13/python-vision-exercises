import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

rose = mpimg.imread('rose-piano.jpg')

rose1 = rose / 255

blur = [[[1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]]]

blur = np.array(blur)
a = convolve(rose1, blur, output=None, mode='reflect', cval=0.0, origin=0)

b = cv2.GaussianBlur(rose, (5, 5), sigmaX=0)

edge = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]
edge = np.array(edge)
rose1 = np.mean(rose1, axis=2)
c = convolve(rose1, edge)
c = np.where(c > 0.25, 1, 0)

d = cv2.Laplacian(rose, cv2.CV_8U, ksize=3)

e = cv2.Laplacian(b, cv2.CV_8U, ksize=3)

#plt.imsave('exercise5a.jpg', a)
plt.imsave('exercise5b.jpg', b)
plt.imsave('exercise5c.jpg', c)
plt.imsave('exercise5d.jpg', d)
plt.imsave('exercise5e.jpg', e)

plt.imshow(a)
plt.show()