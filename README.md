# OCR and Camera Feed Integration

This project demonstrates how to perform OCR using Tesseract and OpenCV and how to integrate it with a live camera feed. The project is structured to be modular for easy testing and maintenance.

## Project Structure

```
project_root/
│
├── modules/
│ ├── init.py
│ ├── ocr_module.py
│ └── camera_module.py
│
├── tests/
│ ├── test_ocr_from_image.py
│ ├── test_ocr_from_camera.py
│
└── README.md
```

## Modules

### 1. OCR Module (`modules/ocr_module.py`)

This module handles the OCR functionality using Tesseract. It provides a function to perform OCR on an image and return the image with bounding boxes and the recognized text.

### 2. Camera Module (`modules/camera_module.py`)

This module captures video from the camera, uses the OCR module to process each frame, and saves the recognized text and frames with bounding boxes.

## Tests

### 1. Test OCR with Image (`tests/test_ocr_from_image.py`)

This script tests the OCR functionality using a static image. Update the `test_image_path` variable with the path to your test image and run the script.

### 2. Test OCR with Camera (`tests/test_ocr_from_camera.py`)

This script tests the OCR functionality using a live camera feed. It captures video from the camera, performs OCR on each frame, and saves the results.

## Setup

1. Install the necessary libraries:

   ```bash
   pip install opencv-python pytesseract
   ```

2. Ensure Tesseract is installed and update the path in `modules/ocr_module.py`:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
   ```

3. Run the test scripts:

   - Test OCR with a static image:

     ```bash
     python tests/test_ocr_from_image.py
     ```

   - Test OCR with a camera feed:
     ```bash
     python tests/test_ocr_from_camera.py
     ```

4. The recognized text will be saved in `recognized_text.csv` and frames will be saved in the `frames` directory.

## Example Usage

1. **Test OCR with Static Image**:
   Place a test image named `test_image.png` in the project directory and run the `test_ocr_from_image.py` script.

2. **Test OCR with Camera Feed**:
   Ensure your camera is connected and run the `test_ocr_from_camera.py` script. The live feed with recognized text will be displayed, and results will be saved in the specified CSV file and frames directory.

## Notes

- Modify the Tesseract path in `modules/ocr_module.py` as needed.
- Ensure the `frames` directory exists or modify the script to create it if necessary.
- Adjust the camera source in `modules/camera_module.py` if using a different camera.
