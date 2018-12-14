import cv2
import numpy as np
from scipy import signal

if __name__ == "__main__":
    I = cv2.imread("E:/images/The Beatles.jpg", cv2.IMREAD_GRAYSCALE)
    H1, W1 = I.shape[0:2]
    K = np.array([[-1, -2], [2, 1]], np.float32)
    H2, W2 = K.shape[0:2]
    c_full = signal.convolve2d(I, K, mode="full")
    kr, kc = 0, 0
    c_same = c_full[H2 - kr - 1:H1 + H2 - kr - 1, W2 - kc - 1:W1 + W2 - kc - 1]
    cv2.namedWindow("c_same")
    cv2.imshow("c_same", c_same)
    cv2.imshow("c_full", c_full)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
