import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
if __name__=="__main__":
    if len(sys.argv)>1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print("ERROR")
    rows, cols = image.shape
	pixelSequence = image.reshape([rows*cols,1])
	numberbins=256
	histogram, bins, patch = plt.hist(pixelSequence, numberbins,facecolor='red',histtype='bar')
	plt.xlabel(u"gray Level")
	plt.ylabel(u"number of pixels")
	y_maxValue= np.max(histogram)
	plt.axis([0,255,0,y_maxValue])
	plt.show
