# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:27:55 2021

@author: Suna Ayhan
"""

import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#esikleme
_, thresh_img = cv2.threshold(img,thresh = 60, maxval=255,type=cv2.THRESH_BINARY) # 60 ile 255 arasını beyaz yap siyah yapmak için binary_inv kullan.
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

#uyarlamalı esik degeri
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()