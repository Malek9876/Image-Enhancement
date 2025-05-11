import cv2
import pytesseract

def perform_ocr(image):
    """Perform OCR on the given image and return the detected text."""
    if len(image.shape) == 2:
        img_rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    else:
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Use pytesseract to extract text
    custom_config = r'--oem 3 --psm 7'  # Use default OCR Engine and single line mode
    detected_text = pytesseract.image_to_string(img_rgb, config=custom_config)
    
    return detected_text.strip()

def extract_numbers(detected_text):
    """Extract numbers from the detected text."""
    return ''.join(filter(str.isdigit, detected_text))

def get_number_images(numbers):
    """Retrieve corresponding images for the detected numbers from the database."""
    number_images = {}
    for number in numbers:
        img_path = f'database/{number}.png'
        number_images[number] = cv2.imread(img_path)
    return number_images

def overlay_number_images(base_image, number_images, positions):
    """Overlay the number images onto the base image at specified positions."""
    for number, position in zip(number_images.keys(), positions):
        if number in number_images:
            number_img = number_images[number]
            x, y = position
            base_image[y:y+number_img.shape[0], x:x+number_img.shape[1]] = number_img
    return base_image