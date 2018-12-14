import cv2
import numpy as np
import os


input_path = "./input_images"
output_path = "./output_images"


def average_of_image(image):
    n_rows, n_cols, n_channels = image.shape
    # 遍历图片
    a = np.zeros(n_channels)
    for i in range(n_rows):
        for j in range(n_cols):
            a += image[i, j]
    return a/(n_rows*n_cols)


def distance(vec1, vec2):
    return np.sqrt(np.sum(np.square(vec1-vec2)))


if not os.path.exists(output_path):
    os.makedirs(output_path)
index = 1
files = os.listdir(input_path)
for file in files:
    if not os.path.isdir(file):
        img = cv2.imread(os.path.join(input_path, file))
        if img is not None :
            # Select ROI
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # img_hsv = img
            r = cv2.selectROI(img_hsv)
            # Crop image
            imCrop = img_hsv[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            # 只取hue, saturation
            img_hs = img_hsv[:, :, 0:2]
            roi_hs = imCrop[:, :, 0:2]
            average = average_of_image(roi_hs)

            rows, cols, _ = img_hs.shape
            output = np.zeros(img_hs.shape[0:2], img_hs.dtype)
            # 遍历图片
            for i in range(rows):
                for j in range(cols):
                    if distance(average, img_hs[i,j]) > 40:
                        output[i, j] = 0
                    else:
                        output[i, j] = 255

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            dilated = cv2.dilate(output, kernel)
            cv2.imshow("final", dilated)
            cv2.waitKey(0)
            filename = os.path.join(output_path, file)
            cv2.imwrite(filename, dilated)

