# FFmpeg MJPEG Stream Recorder

This Python script allows you to record MJPEG video streams using FFmpeg. It handles real-time streaming, sets recording durations, and ensures graceful termination of the FFmpeg process to finalize the output file properly.

## Features

- Records MJPEG streams from URLs.
- Allows specifying a recording duration.
- Gracefully stops the FFmpeg process to finalize recordings.
- Captures and logs FFmpeg output for debugging.

## Requirements

- Python 3.7 or later
- FFmpeg installed and available in your system's `PATH`

### Verify FFmpeg Installation

Run the following command to verify FFmpeg is installed:

```bash
ffmpeg -version
```

If not installed, you can download FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) or install it via a package manager like `brew`, `apt`, or `choco`.

## Setup

1. Clone or download the repository.
2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > Note: This script uses only the standard Python library, so no additional dependencies are required.

3. Verify the script by running the example in `ingest.py`.

## Usage

To record an MJPEG stream, specify the following parameters:

- **URL**: The URL of the MJPEG stream.
- **Duration**: The length of the recording in seconds.
- **Output**: The file path where the recording will be saved.

### Example

Modify the parameters in the script or pass them programmatically:

```python
TEST_URL = "http://takemotopiano.aa1.netvolante.jp:8190/nphMotionJpeg?Resolution=640x480&Quality=Standard&Framerate=30"
OUTPUT_FILE = "output.avi"  # File format can be .mp4 or .avi
DURATION = 6  # Duration of the recording in seconds

recorder = FFmpegRecorder(url=TEST_URL, duration_in_sec=DURATION, output=OUTPUT_FILE)
recorder.start()
```

### Command Line Execution

You can run the script directly:

```bash
python ingest.py
```

## Code Structure

- **`FFmpegRecorder`**: A class that manages the FFmpeg process lifecycle.
  - **`__init__`**: Initializes the recording parameters.
  - **`start`**: Starts the recording process.
  - **`stop`**: Stops the FFmpeg process gracefully using `SIGINT`.

## FFmpeg Arguments Explained

- `-re`: Ensures FFmpeg reads the input in real-time.
- `-use_wallclock_as_timestamps 1`: Uses wall-clock timestamps to handle streams without duration metadata.
- `-t`: Specifies the recording duration in seconds.
- `-c:v copy`: Copies the video codec without re-encoding for better performance.

## Output Formats

By default, the script saves recordings as `.avi` files for better compatibility with MJPEG streams. However, you can use `.mp4` if preferred.

## Debugging

Enable detailed FFmpeg logs by adding `-loglevel debug` to the `ffmpeg_args`:

```python
"-loglevel", "debug",
```

## Contributing

Feel free to fork the repository, submit issues, or open pull requests to contribute improvements.

## License

This project is licensed under the MIT License.

Emi Roberti - Happy coding
