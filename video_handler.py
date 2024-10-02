import cv2
from filters.black_and_white import BlackAndWhiteFilter
from filters.mirror import MirrorFilter
from filters.inversion import InvertColorsFilter
from filters.sharpen import SharpenFilter
from pipe_manager import PipeManager

def video_stream(pipe_manager):
    cap = cv2.VideoCapture(0)  # 0 for webcam or provide video file path
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        processed_frame = pipe_manager.process(frame)
        cv2.imshow('Processed Frame', processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Set up Filters
pipe_manager = PipeManager()
pipe_manager.add_filter(BlackAndWhiteFilter())
pipe_manager.add_filter(MirrorFilter())
pipe_manager.add_filter(InvertColorsFilter())
pipe_manager.add_filter(SharpenFilter())

# Start Video Stream
video_stream(pipe_manager)
