import cv2
import numpy as np
import math
import sys
from matplotlib import pyplot as plt

inputimage ='img/bricks.jpg'

orig_image = cv2.imread(inputimage)
img = cv2.imread(inputimage,0)
blurred = cv2.GaussianBlur(img, (3, 3), 0)


#---- apply automatic Canny edge detection using the computed median----
v = np.median(img)
sigma=0.33
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))

#----- Otsu method for edge detection
high_thresh, thresh_im = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lowThresh = 0.5*high_thresh

# Canny edge detection with blurred image
blurrededges = cv2.Canny(blurred, lower, upper)
# canny edge detection with gray scaled image
greyedges = cv2.Canny(img, lower, upper)


# Hough lines
#min for redwall = 35, max = 200
#min for close_up = 5, max = 1500 this settings works on redwall and building also
#min for brick_wall2 = 190, max 200
#glas_building min = 10, max = 300
#whole_building min =10, max = 40
#big_building min 10, max 1400
minLineLength = 20
maxLineGap = 15
lines = cv2.HoughLinesP(image=greyedges,rho=1,theta=np.pi/180, threshold=100,
lines=np.array([]),minLineLength=minLineLength,maxLineGap=maxLineGap)
if lines is not None:
	no_lines=0
	for line in lines:
		for x1,y1,x2,y2 in line:
		    # print "From (%d, %d) to (%d, %d)" % (x1,y1,x2,y2)
		    # Calculate line angle
		    angleDeg = abs(math.atan2(y2-y1,x2-x1)*180/np.pi)
		    # Only include line with angles > 80 degrees (almost vertical)
		    if angleDeg > 80:
			cv2.line(orig_image,(x1,y1),(x2,y2),(0,0,255),10)
			no_lines = no_lines + 1
	print "Number of vertical lines: %d" % no_lines

# Show images
cv2.namedWindow('Hough',cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hough', 720,720/16*9)
cv2.resizeWindow('Canny', 720,720/16*9)
cv2.imshow('Hough', orig_image)
cv2.imshow('Canny', greyedges)

cv2.waitKey(0)
	

cv2.destroyAllWindows()


	
	
#if __name__ == '__main__':
    # Map command line arguments to function arguments.
#    if sys.argv[0] ==None:
#    	image_edge_detection()
 #   else:
 #   	image = sys.argv[0]
 #   	image_edge_detection(image)
