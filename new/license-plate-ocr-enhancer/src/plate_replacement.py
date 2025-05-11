import cv2
import numpy as np
import os

def load_digit_images(database_path):
    digit_images = {}
    for i in range(10):
        img_path = os.path.join(database_path, f"{i}.png")
        digit_images[str(i)] = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    return digit_images

def replace_digits_with_images(plate_image, detected_digits, digit_images):
    for digit, (x, y, w, h) in detected_digits.items():
        if digit in digit_images:
            digit_image = digit_images[digit]
            digit_image_resized = cv2.resize(digit_image, (w, h))
            plate_image[y:y+h, x:x+w] = digit_image_resized
    return plate_image

def process_plate_with_replacement(plate_image, detected_digits, database_path):
    digit_images = load_digit_images(database_path)
    enhanced_plate_image = replace_digits_with_images(plate_image, detected_digits, digit_images)
    return enhanced_plate_image