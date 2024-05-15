import cv2


def show_webcam_feed():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Display the live feed
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Display the frame
        cv2.imshow("Webcam Feed", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()


def capture_image_from_webcam():
    # Open the webcam (device 0 by default)
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        cap.release()
        return

    # Save the captured image
    image_filename = "captured_image.jpg"
    cv2.imwrite(image_filename, frame)
    print(f"Image saved as {image_filename}")

    # Release the webcam
    cap.release()


if __name__ == "__main__":
    while True:
        command = (
            input(
                "Enter 'feed' to show webcam feed, 'capture' to capture an image, or 'exit' to quit: "
            )
            .strip()
            .lower()
        )
        if command == "feed":
            show_webcam_feed()
        elif command == "capture":
            capture_image_from_webcam()
        elif command == "exit":
            break
