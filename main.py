import numpy as np
import cv2

#connect to webcam
cap = cv2.VideoCapture(0)
#initializes the background subtraction module
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    #capture one frame from webcam
    ret, frame = cap.read()
    #extract mask for foreground-background split
    fgmask = fgbg.apply(frame)
    #apply mask to extracted frame
    res = cv2.bitwise_and(frame,frame,mask=fgmask)
    
    #display the resulting frame
    cv2.imshow('frame',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
