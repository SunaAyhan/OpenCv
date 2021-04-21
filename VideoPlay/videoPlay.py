# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:58:10 2021

@author: Suna Ayhan
"""

import cv2
import time
video_name = "MOT17-04-DPM.mp4"

#video içe aktar
cap = cv2.VideoCapture(video_name)

# video yuksekliği ve genişliği
print("genislik: ",cap.get(3))
print("yukseklik: ",cap.get(4))

if cap.isOpened() == False:
    print("error")
    
while True: #tüm videoyu izle
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) # kullanmazsak video çok hızlı oynar
        cv2.imshow("video",frame)
    else: break
    if cv2.waitKey(1) & 0xFF == ord("q"): # q'ya basınca videoyu durdur
        break
cap.release() #stop capture
cv2.destroyAllWindows()