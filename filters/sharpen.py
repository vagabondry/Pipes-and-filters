import cv2
import numpy as np

class SharpenFilter:
    def apply(self, frame):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(frame, -1, kernel)
