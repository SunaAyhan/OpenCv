# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:38:40 2021

@author: Su
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img_vis)
print(img.shape)

img_hist = cv2.calcHist([img],channels=[0],mask=None, hisSize=[256],ranges=[0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)
color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = cv2.calcHist([img],channels=[0],mask=None, hisSize=[256],ranges=[0,256])
    plt.plot(hist, color=c)
    
#maskeleme

golden_gate=cv2.imread("goldenGate.jpg")
golden_gate_vis= cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure(),plt.imshow(mask, cmap="gray")
mask[1500:2000,1000:2000] = 255
plt.figure(),plt.imshow(mask, cmap="gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
plt.figure(),plt.imshow(masked_img_vis, cmap="gray"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        )
