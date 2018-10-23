import cv2
import numpy as np

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
    print "Number of lines: " + str(len(lines))
    for line in lines:
        for x1,y1,x2,y2 in line:
            #print "From (%d, %d) to (%d, %d)" % (x1,y1,x2,y2)
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    # Show images
    cv2.imshow('Hough',frame)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
