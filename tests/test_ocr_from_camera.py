import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.camera_module import capture_from_camera

if __name__ == "__main__":
    capture_from_camera()
