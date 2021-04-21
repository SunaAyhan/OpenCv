# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:37:45 2021

@author: Suna Ayhan
"""

import cv2

#resmi oku
img = cv2.imread("lenna.png")

#boyutunu öğren
print("resim boyutu: ",img.shape)
cv2.imshow("orijinal",img)

# boyutlandır
imgResized=cv2.resize(img,(800,800))
print(" resized img shape: ",imgResized.shape)
cv2.imshow("img resized",imgResized)

#kırp
imgCropped = img[:200,0:300]
cv2.imshow("kirpilmis",imgCropped)