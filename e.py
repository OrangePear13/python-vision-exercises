import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

rose = mpimg.imread('rose-piano.jpg')

blur = [[
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]]
blur = np.array(blur)
blur /= np.sum(blur)
a = convolve(rose, blur)

b = cv2.GaussianBlur(rose, (5, 5), sigmaX=0)

edge = [[
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]]
edge = np.array(edge)
c = convolve(rose, edge)

d = cv2.Laplacian(rose, cv2.CV_8U, ksize=3)

e = cv2.Laplacian(b, cv2.CV_8U, ksize=3)

plt.imshow(c)
plt.show()