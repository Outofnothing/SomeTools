import cv2
import numpy as np

In = cv2.imread("E:\\images\\crown.jpg", cv2.IMREAD_GRAYSCALE)
Imax = np.max(In)
Imin = np.min(In)
Omin, Omax = 0, 255
a = (Omax-Omin)/(Imax-Imin)
b = Omin - a*Imin
out = a*In + b
out = out.astype(np.uint8)
cv2.imshow("I", In)
cv2.imshow("O", out)
cv2.waitKey()
cv2.destroyAllWindows()

