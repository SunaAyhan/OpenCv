# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:14:57 2021

@author: Suna Ayhan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi aktar
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
print(img.shape)
plt.figure()
plt.imshow(img, cmap="gray"),plt.axis("off")


# harris corner detection
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")


# shi tomsai detection
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 120, 0.01, 10) # 120 => tespit edilecek köşe sayısı
corners = np.int64(corners)

# köşelere circle çizdir
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)
    
    
plt.imshow(img)
plt.axis("off")


























