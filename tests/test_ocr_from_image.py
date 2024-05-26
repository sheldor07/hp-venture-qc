import cv2
from modules.ocr_module import perform_ocr


def test_ocr_with_image(image_path):
    image = cv2.imread(image_path)
    result_image, recognized_text = perform_ocr(image)

    cv2.imshow("OCR Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Recognized Text:", recognized_text)


if __name__ == "__main__":
    test_image_path = "test_image.png"  # Replace with your test image path
    test_ocr_with_image(test_image_path)
