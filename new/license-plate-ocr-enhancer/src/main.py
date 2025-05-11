import cv2
import numpy as np
from ocr import perform_ocr
from image_processing import apply_image_processing
from plate_replacement import replace_plate_numbers
import os

def main():
    # Load the original license plate image
    plate_image_path = r"C:\Users\Admin\Desktop\TD_INFO\Traitement image\SR_ROI.png"  # Update with your image path
    original_plate_image = cv2.imread(plate_image_path)

    if original_plate_image is None:
        print(f"Error: Could not load image at {plate_image_path}")
        return

    # Step 1: Process the image
    processed_image = apply_image_processing(original_plate_image)

    # Step 2: Perform OCR to detect numbers
    detected_numbers = perform_ocr(processed_image)

    # Step 3: Replace detected numbers with corresponding images from the database
    enhanced_plate_image = replace_plate_numbers(original_plate_image, detected_numbers)

    # Step 4: Save the final enhanced plate image
    output_path = 'enhanced_plate_output.png'
    cv2.imwrite(output_path, enhanced_plate_image)
    print(f"Final enhanced plate saved as '{output_path}'")

if __name__ == "__main__":
    main()