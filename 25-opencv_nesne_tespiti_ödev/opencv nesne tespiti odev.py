# opencv kütüphanesini içe aktaralım
import cv2 


# numpy kütüphanesini içe aktaralım
import numpy as np

# resmi siyah beyaz olarak içe aktaralım resmi çizdirelim
img = cv2.imread("odev2.jpg")

# resim üzerinde bulunan kenarları tespit edelim ve görselleştirelim edge detection
edges = cv2.Canny(image=img, threshold1 = 200, threshold2=250)
cv2.imshow("kenarlar", edges)
# yüz tespiti için gerekli haar cascade'i içe aktaralım
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# yüz tespiti yapıp sonuçları görselleştirelim
face_rect = face_cascade.detectMultiScale(img, minNeighbors = 3)
for (x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,255,255),10)
cv2.imshow("faces",img)
# HOG ilklendirelim insan tespiti algoritmamızı çağıralım ve svm'i set edelim
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())



# resme insan tespiti algoritmamızı uygulayalım ve görselleştirelim
(rects, weights) = hog.detectMultiScale(img, padding=(8, 8), scale=1.05)

for (xA, yA, xB, yB) in rects:
    cv2.rectangle(img, (xA, yA), (xB, yB), (0, 0, 255), 2)
	
cv2.imshow("insan Tespiti", img)


cv2.waitKey(0)

cv2.destroyAllWindows()