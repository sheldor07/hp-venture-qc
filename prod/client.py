import cv2
import time
import telnetlib
import numpy as np


# Telnet functions
def initialize_telnet_connection(host="192.168.1.78"):
    tn = telnetlib.Telnet(host)
    tn.read_eager()
    tn.write(b"admin\r\n")
    time.sleep(2)
    tn.write(b"\r\n")
    tn.read_eager()
    time.sleep(2)
    tn.write(b"\r\n")
    tn.read_very_lazy()
    tn.write(b"\r\n")
    return tn


def show_telnet_feed(tn):
    cv2.namedWindow("Telnet Feed")

    while True:
        # Command to request the next frame (this depends on your camera's API, adjust as necessary)
        tn.write(b"GI\r\n")
        time.sleep(0.1)

        # Read image data
        image_data = tn.read_very_lazy()

        # Decode image data (assuming it's in JPEG format)
        np_arr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Display the frame
        if frame is not None:
            cv2.imshow("Telnet Feed", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


def capture_image_from_telnet(tn):
    tn.write(b"GI\r\n")
    time.sleep(2)
    image_data = tn.read_very_lazy()
    image_filename = "captured_image_telnet.jpg"
    with open(image_filename, "wb") as image_file:
        image_file.write(image_data)
    print(f"Image saved as {image_filename}")


if __name__ == "__main__":
    while True:
        command = (
            input(
                "Enter 'feed' for Telnet feed, 'capture_telnet' to capture from Telnet, or 'exit' to quit: "
            )
            .strip()
            .lower()
        )
        if command == "feed":
            tn = initialize_telnet_connection()
            show_telnet_feed(tn)
            tn.close()
        elif command == "capture_telnet":
            tn = initialize_telnet_connection()
            capture_image_from_telnet(tn)
            tn.close()
        elif command == "exit":
            break
