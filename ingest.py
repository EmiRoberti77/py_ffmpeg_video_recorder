import subprocess
import time
from threading import Timer
import random

class FFmpegRecorder:
    def __init__(self, url: str, duration_in_sec: int, output: str):
        if not url or not duration_in_sec or not output:
            raise ValueError("Invalid parameters provided to FFmpegRecorder.")
        self.url = url
        self.duration_in_sec = duration_in_sec
        self.output = output
        self.ffmpeg_process = None

    def start(self):
        ffmpeg_args = [
            "ffmpeg",
            "-re",  # Process in real-time
            "-use_wallclock_as_timestamps", "1",  # Use real-time timestamps
            "-i", self.url,
            "-t", str(self.duration_in_sec),
            "-c:v", "copy",
            self.output,
        ]
        print("Starting FFmpeg with arguments:", " ".join(ffmpeg_args))

        try:
            # Start the FFmpeg process
            self.ffmpeg_process = subprocess.Popen(
                ffmpeg_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            # Create a timer to stop the process gracefully after duration_in_sec
            timer = Timer(self.duration_in_sec, self.stop)
            timer.start()

            # Capture and log stdout and stderr
            stdout, stderr = self.ffmpeg_process.communicate()
            print("FFmpeg stdout:", stdout.decode("utf-8"))
            print("FFmpeg stderr:", stderr.decode("utf-8"))

            # Wait for the process to complete
            self.ffmpeg_process.wait()
            if self.ffmpeg_process.returncode == 0:
                print(f"Recording completed successfully: {self.output}")
            else:
                print(f"FFmpeg exited with code {self.ffmpeg_process.returncode}")

        except Exception as e:
            print(f"Error during recording: {str(e)}")
        finally:
            if self.ffmpeg_process and self.ffmpeg_process.poll() is None:
                self.stop()

    def stop(self):
        if self.ffmpeg_process and self.ffmpeg_process.poll() is None:
            print("Stopping FFmpeg process gracefully...")
            self.ffmpeg_process.terminate()  # Send SIGTERM to FFmpeg
            try:
                self.ffmpeg_process.wait(timeout=5)
                print("FFmpeg process terminated successfully.")
            except subprocess.TimeoutExpired:
                print("FFmpeg did not terminate, forcing kill.")
                self.ffmpeg_process.kill()


if __name__ == "__main__":
    # Example usage
    while True:
        TEST_URL = "http://takemotopiano.aa1.netvolante.jp:8190/nphMotionJpeg?Resolution=640x480&Quality=Standard&Framerate=30"
        id = random.randint(0,1000)
        OUTPUT_FILE = f"/Users/user/recording/output{id}.mp4"
        DURATION = 10  # seconds
        recorder = FFmpegRecorder(url=TEST_URL, duration_in_sec=DURATION, output=OUTPUT_FILE)
        recorder.start()
        print('completed', OUTPUT_FILE)
