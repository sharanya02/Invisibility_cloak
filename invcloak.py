import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(60):
    ret,background = cap.read()
background = np.flip(background,axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value,0)
    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])
    #use the value given below to turn any blue cloth into the invisibility cloak
     #lower_blue = np.array([101,50,38])
   # upper_blue = np.array([110,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red = np.array([170,120,50])
    upper_red = np.array([180,255,255])
    #lower_blue = np.array([120,50,38])
    #upper_blue = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    # Addition of the two masks to generate the final mask.
    mask = mask1+mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    # Replacing pixels corresponding to cloak with the background pixels.
    img[np.where(mask==255)] = background[np.where(mask==255)]
    cv2.imshow('Display',img)
    close_key = cv2.waitKey(10) & 0xFF
    if close_key == 27:
        break
cv2.destroyAllWindows()
