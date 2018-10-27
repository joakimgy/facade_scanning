import cv2
import numpy as np
import math
import sys
from matplotlib import pyplot as plt

inputimage ='img/red_wall2.jpg'

def 	image_edge_detection (inputimage):
	img = cv2.imread(inputimage,0)

	# Canny edge detection
	edges = cv2.Canny(img, 100, 200)

	# Hough lines
	#minLineLength = 100
	#maxLineGap = 10
	#lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=15,
	#lines=np.array([]),minLineLength=minLineLength,maxLineGap=maxLineGap)
	#if lines is not None:
	#	for line in lines:
	#		for x1,y1,x2,y2 in line:
	#		    # print "From (%d, %d) to (%d, %d)" % (x1,y1,x2,y2)
	#		    # Calculate line angle
	#		    angleDeg = abs(math.atan2(y2-y1,x2-x1)*180/np.pi)
	#		    # Only include line with angles > 80 degrees (almost vertical)
	#		    if angleDeg > 80:
	#			cv2.line(img,(x1,y1),(x2,y2),(0,0,255),4)
	#			no_lines = no_lines + 1
	#	print "Number of vertical lines: %d" % no_lines

	# Show images
	#cv2.imshow('Hough',img)
	plt.subplot(121),plt.imshow(img,cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

	plt.show()

	#k = cv2.waitKey(5) & 0xFF
	#if k == 27:
	#break

	cv2.destroyAllWindows()
	cap.release()
	return
	
	
if __name__ == '__main__':
    # Map command line arguments to function arguments.
    if sys.argv[0] ==None:
    	image_edge_detection()
    else:
    	image = sys.argv[0]
    	image_edge_detection(image)
