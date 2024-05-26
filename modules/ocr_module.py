import pytesseract
from pytesseract import Output
import cv2

# Path to tesseract executable (update this path with the correct absolute path)
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def perform_ocr(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    d = pytesseract.image_to_data(gray, output_type=Output.DICT)

    n_boxes = len(d["level"])
    for i in range(n_boxes):
        (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    recognized_text = " ".join(
        [d["text"][i] for i in range(n_boxes) if d["text"][i].strip()]
    )
    return image, recognized_text
