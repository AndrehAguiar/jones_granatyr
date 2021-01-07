import cv2
"""
OpenCV to python
opencv_python‑4.4.0‑cp39‑cp39‑win_amd64.whl
https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
"""

print(cv2.__version__)
image = cv2.imread('images/opencv-python.jpg')
imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', imagegray)
cv2.imshow('Original', image)
cv2.waitKey()
