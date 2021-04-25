# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:28:05 2021

@author: Suna Ayhan
"""

import cv2
import os

files = os.listdir()
img_path_list = []
for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
print(img_path_list)

# hog tanımlayıcısı
hog = cv2.HOGDescriptor()
# tanımlayıcıya SVM ekle
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for imagePath in img_path_list:
    print(imagePath)
    image = cv2.imread(imagePath)
    (rects, weights) = hog.detectMultiScale(image, padding = (8,8), scale = 1.05)
    for (x,y,w,h) in rects:
        cv2.rectangle(image, (x,y),(x+w, y+h),(0,0,255),3)
    cv2.imshow("yaya:",image)
    if cv2.waitKey(0) & 0XFF == ord("q"): continue
    