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
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()

def toggle_filter(pipe_manager, filter_instance, filter_name):
    if filter_instance in pipe_manager.filters:
        pipe_manager.filters.remove(filter_instance)
        print(f"{filter_name} filter deactivated.")
    else:
        pipe_manager.add_filter(filter_instance)
        print(f"{filter_name} filter activated.")

# Set up Filters
pipe_manager = PipeManager()

bw_filter = BlackAndWhiteFilter()
mirror_filter = MirrorFilter()
invert_filter = InvertColorsFilter()
sharpen_filter = SharpenFilter()

# Start Video Stream and Filter Management
print("Video stream started. Press the corresponding keys to toggle filters:")
print("'1' - Black and White filter")
print("'2' - Mirror filter")
print("'3' - Invert Colors filter")
print("'4' - Sharpen filter")
print("Press 'q' to quit the video.")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame through the filters
    processed_frame = pipe_manager.process(frame)
    cv2.imshow('Processed Frame', processed_frame)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        toggle_filter(pipe_manager, bw_filter, "Black and White")
    elif key == ord('2'):
        toggle_filter(pipe_manager, mirror_filter, "Mirror")
    elif key == ord('3'):
        toggle_filter(pipe_manager, invert_filter, "Invert Colors")
    elif key == ord('4'):
        toggle_filter(pipe_manager, sharpen_filter, "Sharpen")
    elif key == ord('q'):
        print("Exiting video stream.")
        break

cap.release()
cv2.destroyAllWindows()
 
