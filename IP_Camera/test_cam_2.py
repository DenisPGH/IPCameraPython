
from picamera.array import PiRGBArray  # Generates a 3D RGB array
from picamera import PiCamera  # Provides a Python interface for the RPi Camera Module
import time  # Provides time-related functions
import cv2  # OpenCV library

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
raw_capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    raw_capture.truncate(0)
    if key == ord("q"):
        break


