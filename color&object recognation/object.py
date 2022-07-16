import cv2
import sys
from cv2 import getTrackbarPos
import numpy as np
cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
def on_trackbar(pos):
    pass
 

while True:
    ret_val, img = cam.read() 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray,(0,0),1.0)
    circles = cv2.HoughCircles(blr,cv2.HOUGH_GRADIENT,1,50,param1 = 120, param2=10,minRadius=50,maxRadius = 100)
    dst = img.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx,cy,radius = circles[0][i]
            print(cx,cy)
            # cv2.circle(dst,(cx,cy),int(radius),(0,0,225),2,cv2.LINE_AA)
    cv2.imshow("img",dst)
    
    if cv2.waitKey(1) == 27:
        break  