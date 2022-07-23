'''
import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
while (1):
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # BGR을 HSV로 변환해줌
    lower_blue = np.array([100,100,120])
    upper_blue = np.array([150,255,255])
    lower_green = np.array([50, 150, 50]) # 초록색 범위
    upper_green = np.array([80, 255, 255])
    lower_red = np.array([150, 50, 50]) # 빨강색 범위
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    cv2.imshow('frame',frame)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    cv2.destroyAllWindows()
''' 

import cv2
import numpy as np

camm = cv2.VideoCapture(0)    

while(1):
    ret, frame = camm.read()    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    lower_blue = np.array([100,100,120])       
    upper_blue = np.array([150,255,255])

    lower_green = np.array([50, 150, 50])         
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([150, 50, 50])        
    upper_red = np.array([180, 255, 255])

   
    mask = cv2.inRange(hsv, lower_blue, upper_blue)    
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)     
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)  
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)   

    cv2.imshow('frame',frame)       
    cv2.imshow('Blue', res)           
    cv2.imshow('Green', res1)   
    cv2.imshow('red', res2)        

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
