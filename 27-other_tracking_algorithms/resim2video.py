# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:46:27 2021

@author: Suna Ayhan
"""
"""
- veri setini (ok)
- veri seti indir (ok)
- resim2video (ok)
- eda -> gt
""" 
import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt


pathIn = r"img1"
pathOut = "video.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

fps = 25
size = (1920, 1080)

out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)
for i in files:
    print(i)
    filename = pathIn + "\\" + i
    img = cv2.imread(filename)
    out.write(img)
out.release()
cv2.destroyAllWindows()
































