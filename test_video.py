import os
import numpy as np
import cv2

os.chdir('C:\\Users\\l.piccolo\\Pictures')
cap = cv2.VideoCapture('4199675334_66c3e3d61d_z.jpg')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #fgmask = fgbg.apply(frame)

    #res = cv2.bitwise_and(frame,frame,mask=fgmask)
    if ret==True:
        #print "hello!"
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        fc = cap.get(CV_CAP_PROP_FRAME_COUNT)
        cap.set(fc, 0)
        #print "ret not True!"
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
