import cv2
import time
import telnetlib
import numpy as np


# Telnet functions
def initialize_telnet_connection(host="localhost"):
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


def extract_jpeg_data(data):
    start_marker = b"\xff\xd8"
    end_marker = b"\xff\xd9"
    start = data.find(start_marker)
    end = data.find(end_marker, start)

    if start != -1 and end != -1:
        return data[start : end + len(end_marker)]
    else:
        return None


def show_telnet_feed(tn):
    cv2.namedWindow("Telnet Feed")

    while True:
        # Command to request the next frame
        tn.write(b"GI\r\n")
        time.sleep(0.1)

        # Read image data
        image_data = tn.read_until(b"\n> ")

        # Debug: Print length and type of the received data
        print(f"Received data length: {len(image_data)}")
        print(f"Received data type: {type(image_data)}")

        # Print the first 100 bytes of the received data in hexadecimal format
        print("First 100 bytes of received data:", image_data[:100].hex())

        # Extract the JPEG data from the received data
        jpeg_data = extract_jpeg_data(image_data)
        if jpeg_data is None:
            print("Error: JPEG markers not found.")
            continue

        # Debug: Print first 100 bytes of the extracted JPEG data in hexadecimal format
        print("First 100 bytes of JPEG data:", jpeg_data[:100].hex())

        # Decode image data (assuming it's in JPEG format)
        np_arr = np.frombuffer(jpeg_data, np.uint8)
        if np_arr.size == 0:
            print("Error: Received empty image data.")
            continue

        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if frame is None:
            print("Error: Failed to decode image.")
            continue

        # Display the frame
        cv2.imshow("Telnet Feed", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


def capture_image_from_telnet(tn):
    tn.write(b"GI\r\n")
    time.sleep(2)
    image_data = tn.read_until(b"\n> ")

    # Extract the JPEG data from the received data
    jpeg_data = image_data
    if jpeg_data is None:
        print("Error: JPEG markers not found.")
        return

    image_filename = "output/captured_image_telnet.jpg"
    with open(image_filename, "wb") as image_file:
        image_file.write(jpeg_data)
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
