import cv2
import numpy as np

class SepiaFilter:
    def apply(self, frame):
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, sepia_filter)
        return cv2.clip(sepia_frame, 0, 255).astype(np.uint8)
