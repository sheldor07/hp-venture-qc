import cv2
import csv
from modules.ocr_module import perform_ocr


def capture_from_camera(output_csv="recognized_text.csv"):
    cap = cv2.VideoCapture(2)

    with open(output_csv, "w", newline="") as csvfile:
        fieldnames = ["frame", "recognized_text"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        frame_count = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame, recognized_text = perform_ocr(frame)

            frame_filename = f"frames/frame_{frame_count}.png"
            cv2.imwrite(frame_filename, frame)
            writer.writerow(
                {"frame": frame_filename, "recognized_text": recognized_text}
            )

            cv2.imshow("OCR Feed", frame)

            frame_count += 1

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
