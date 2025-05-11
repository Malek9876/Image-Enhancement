# License Plate OCR Enhancer

This project is designed to enhance the readability of license plate images by applying various image processing techniques and performing Optical Character Recognition (OCR). The detected numbers on the license plate are then replaced with corresponding images from a database to create a clearer representation of the license plate.

## Project Structure

```
license-plate-ocr-enhancer
├── src
│   ├── main.py                # Entry point for the application
│   ├── ocr.py                 # Functions for performing OCR
│   ├── image_processing.py     # Image processing functions
│   ├── plate_replacement.py    # Logic for replacing detected numbers
│   ├── database               # Contains digit images (0-9)
│   │   ├── 0.png
│   │   ├── 1.png
│   │   ├── 2.png
│   │   ├── 3.png
│   │   ├── 4.png
│   │   ├── 5.png
│   │   ├── 6.png
│   │   ├── 7.png
│   │   ├── 8.png
│   │   └── 9.png
│   └── utils.py               # Utility functions
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd license-plate-ocr-enhancer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your license plate images in the appropriate directory.
2. Run the application:
   ```
   python src/main.py
   ```

3. The processed license plate image will be displayed, and the enhanced version will be saved to disk.

## Functionality

- **Image Processing**: The project applies gray + top-hat transformations and sharpening to enhance the license plate image.
- **OCR**: The OCR module extracts text from the processed image using pytesseract.
- **Plate Replacement**: Detected numbers are replaced with corresponding images from the database, improving the visual clarity of the license plate.

## Dependencies

The project requires the following Python packages:

- OpenCV
- pytesseract
- NumPy
- Matplotlib

Ensure that these packages are installed before running the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.