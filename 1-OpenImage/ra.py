# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:30:43 2021

@author: Suna Ayhan
"""

import cv2

#içe aktarma
img = cv2.imread("messi5.jpg",0) #0 -> siyah beyaz

#görselleştirme
cv2.imshow("ilk resim",img)

k=cv2.waitKey(0) &0xFF
if k == 27: # 27 sayısı esc tuşuna denk gelir
    cv2.destroyAllWindows() #escye basınca tüm pencereleri kapat
    
elif k == ord('s'): #s tuşuna basınca 
    cv2.imwrite("mess_gray.png",img) #resmi siyah beyaz olarak kaydet
    cv2.destroyAllWindows()
