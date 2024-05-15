# Camera Feed and Image Capture

This repository contains scripts for displaying live feed and capturing images from both a webcam and a Telnet-connected camera. The project is divided into three main directories:

1. **cam_test**: Basic structure and code for live feed and capturing images using a local webcam.
2. **prod**: Scripts for connecting to a Telnet-connected camera and handling live feed and image capture.
3. **test**: Mock Telnet server and client scripts for testing the functionality with test images.

## Directory Structure

```plaintext
.
├── cam_test
│   ├── live_feed.py
│   └── capture_image.py
├── prod
│   ├── client_script.py
├── test
│   ├── mock_telnet_server.py
│   └── client_script.py
└── README.md
