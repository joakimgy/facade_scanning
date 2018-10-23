import cv2
import numpy as np
import math

cap = cv2.VideoCapture(-1)

while(1):

    # Take each frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Canny edge detection
    edges = cv2.Canny(frame, 100, 200)
    
    # Hough lines
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=15,
        lines=np.array([]),minLineLength=minLineLength,maxLineGap=maxLineGap)
    if lines is None:
        continue
    no_lines = 0;
    for line in lines:
        for x1,y1,x2,y2 in line:
            # print "From (%d, %d) to (%d, %d)" % (x1,y1,x2,y2)
            # Calculate line angle
            angleDeg = abs(math.atan2(y2-y1,x2-x1)*180/np.pi)
            # Only inclued line with angles > 80 degrees (almost vertical)
            if angleDeg > 80:
                cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),4)
                no_lines = no_lines + 1
    print "Number of vertical lines: %d" % no_lines

    # Show images
    cv2.imshow('Hough',frame)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
