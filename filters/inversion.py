import cv2

class InvertColorsFilter:
    def apply(self, frame):
        return cv2.bitwise_not(frame)
