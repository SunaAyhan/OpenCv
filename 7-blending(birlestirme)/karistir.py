# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:12:18 2021

@author: Suna Ayhan
"""

import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("img1.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(600,600))
img2 = cv2.resize(img2,(600,600))
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karistirilmis resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2= img2, beta=0.8, gamma=0) #alpha ve beta o resimlerin ne kadarını aldığını gösterir
plt.figure()
plt.imshow(blended)