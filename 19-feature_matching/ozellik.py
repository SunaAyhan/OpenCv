# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:26:08 2021

@author: Suna Ayhan
"""

import cv2
import matplotlib.pyplot as plt

# ana görüntüyü al
chos = cv2.imread("chocolates.jpg",0)
plt.figure()
plt.imshow(chos, cmap="gray")
plt.axis("off")

#aranacak olan görüntü
cho = cv2.imread("nestle.jpg",0)
plt.figure()
plt.imshow(chos, cmap="gray")
plt.axis("off")

# orb tanımlayıcısı
# köşe kenar gibi nesneye ait özellikler
orb = cv2.ORB_create()

#anahtar nokta tespiti
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

#bf matcher
bf= cv2.BFMatcher(cv2.NORM_HAMMING)

#noktaları eşleştir
matches = bf.match(des1, des2)

#mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)


# eslesen resimleri goster
plt.figure()
img_match = cv2.drawMatches(cho,kp1,chos,kp2, matches[:20],None, flags=2)
plt.imshow(img_match),plt.axis("off")

#sift
sift = cv2.xfeatures2d.SIFT_create()

#bf
bf=c2.BFMatcher()

# anahtar nokta

kp1, des1 = shift.detectAndCompute(cho, None)
kp2, des2 = shift.detectAndCompute(cho, None)

matches = bf.knnMatch(des1, des2, k=2)
guzel_eslesme = []

for match1, match2 in matches:
    
    if match1.distance < 0.75*match2.distance:
        guzel_eslesme.append([match1])
    
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho,kp1,chos,kp2,guzel_eslesme,None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("sift")













