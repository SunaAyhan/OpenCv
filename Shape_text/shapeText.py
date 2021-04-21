# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:52:10 2021

@author: Suna Ayhan
"""
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8) #siyah bir resim oluştur
cv2.imshow("siyah",img)

#çizgi
#resim,baslangic noktasi,bitis noktasi, renk, kalınlık
cv2.line(img,(100,100),(100,300),(0,255,0),3) 
cv2.imshow("cizgi",img)

#dikdörtgen
cv2.rectangle(img,(0,0),(256,256),(255,0,0), cv2.FILLED)
cv2.imshow("dikdortgen",img)

#çember
#resim,merkez,yarıçap,renk
cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("cember",img)


#metin
# resim, baslangic noktasi, yazı tipi, kalınlık, renk
cv2.putText(img,"resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("metin",img)
a = cv2.waitKey(1)