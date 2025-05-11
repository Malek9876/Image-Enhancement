import cv2
import numpy as np

def apply_gray_tophat(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image.copy()
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    tophat = cv2.morphologyEx(gray_image, cv2.MORPH_TOPHAT, kernel)
    enhanced_image = cv2.add(gray_image, tophat)
    
    return enhanced_image

def sharpen_image(image):
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    return sharpened_image

def preprocess_license_plate(image):
    enhanced_image = apply_gray_tophat(image)
    sharpened_image = sharpen_image(enhanced_image)
    return sharpened_image