# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:53:11 2021

@author: Suna Ayhan
"""
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydedici
writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height)) #forcc çerçeve sıkıştırıcı (işletim sistemine göre fark eder)

while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    #kaydet
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):break
cap.release()
writer.release()
cv2.destroyWindows()