# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:16:45 2021

@author: Suna Ayhan
"""
from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss

mon = {"top":300, "left":770, "width":250, "height":100}
sct = mss()
width = 125
height = 50

# model yukle
model = model_from_json(open("model.json","r").read())
model.load_weights("trex_weight.h5")

labels=["Down","Right","Up"]
framerate_time = time.time()
counter = 0
i=0
delay=0.4
key_down_pressed = False
while True:
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im2 = np.array(im.convert("L").resize((width, height)))
    im2 = im2 / 255

    X = np.array([im2])
    X = X.reshape(X.shape[0],width, height, 1)
    r=model.predict(X)
    result = np.argmax(r)
    if result == 0:
        keyboard.press(keyboard.KEY_DOWN)
        key_down_pressed = True
    elif result == 2:
        if key_down_pressed:
            keyboard.release(keyboard.KEY_DOWN)
        time.sleep(delay)
        keyboard.press(keyboard.KEY_UP)        
        keyboard.press(keyboard.KEY_UP)
        if i < 1500: # 1500den sonra oyun hızlanıyor
            time.sleep(0.3)
        elif 1500<i<5000:
            time.sleep(0.2)
        else:
            time.sleep(0.17)
        keyboard.press(keyboard.KEY_DOWN)
        keyboard.release(keyboard.KEY_DOWN)
    counter += 1
    if (time.time()-framerate_time)>1:
        counter = 0
        framerate_time=time.time()
        if i <=1500:
            delay -= 0.003
        else:
            delay -= 0.005
        if delay < 0:
            delay = 0
        print("---------------------")
        print("Down: {} \nRight:{} \nUp: {} \n".format(r[0][0],r[0][1],r[0][2]))
        i += 1
            
    

























