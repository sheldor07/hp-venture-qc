import sys
import os
import cv2

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.ocr_module import perform_ocr


def test_ocr_with_image(image_path, output_text_file):
    image = cv2.imread(image_path)
    result_image, recognized_text = perform_ocr(image)

    cv2.imshow("OCR Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Recognized Text:", recognized_text)

    with open(output_text_file, "w") as file:
        file.write(recognized_text)


if __name__ == "__main__":
    test_image_path = "/Users/yajatgulati/dev/hp-internship/tests/test-image.png"  # Replace with your test image path
    output_text_file = "/Users/yajatgulati/dev/hp-internship/tests/recognized_text.txt"  # Replace with your desired output text file path
    test_ocr_with_image(test_image_path, output_text_file)
