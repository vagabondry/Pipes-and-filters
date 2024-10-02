
# Pipes-and-Filters Video Processing Application

This project demonstrates the **Pipes-and-Filters** architectural pattern, applied to a video stream. The application reads video frames, applies multiple filters, and visualizes the processed frames in real-time.

## Features

- **Black and White Filter**: Converts video frames into grayscale.
- **Inversion Filter**: Inverts the colors of the video frames.
- **Mirror Filter**: Mirrors the video frames horizontally.
- **Sharpen Filter**: Sharpens the video frames for better clarity.
- **Custom Filters**: Easily extendable to apply new filters by adding additional components.

## How It Works

The system processes each video frame through a series of filters connected in a pipeline (pipe and filter architecture). The pipeline reads frames from a video source, applies the filters sequentially, and visualizes the result in real-time.

1. **Frame Input**: Captures video frames from a source (e.g., webcam or video file).
2. **Filter Application**: Each frame passes through multiple filters (black and white, inversion, mirror, sharpen, etc.).
3. **Frame Output**: The processed frame is displayed on the screen.

## Getting Started

### Prerequisites

- **Python 3.12**: Required for running the scripts.
- **OpenCV**: Used for video processing.

   Install via pip:
   ```bash
   pip install opencv-python
   ```
   
### Installation
Clone the repository:

```bash
git clone https://github.com/vagabondry/Pipes-and-filters.git
cd Pipes-and-filters
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python video_handler.py
```
### Usage
By default, the application processes the video stream from your webcam. The following filters will be applied:

- Black and White
- Inversion
- Mirror
- Sharpen

You can modify the pipeline to add or remove filters, or introduce custom filters by extending the code.

## Code Structure
```filters/```: Contains the implementation of the individual filters (```black_and_white.py```, ```inversion.py```, ```mirror.py```, ```sharpen.py```).

```video_handler.py```: Entry point of the application, where the pipeline and filters are configured.

```pipe_manager.py```: Manages the creation and connection of the filters in the pipeline, ensuring that each filter processes frames sequentially and efficiently.

```requirements.txt```: List of dependencies required to run the project.

## How to Add a New Filter
To add a new filter, follow these steps:

1. Create a new filter class in the ```filters/``` directory.
2. Implement the ```apply``` method for your specific filter.
3. Add your filter to the pipeline in the ```video_handler.py``` file and ensure it's managed by ```pipe_manager.py```.

## Contributing
Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.
