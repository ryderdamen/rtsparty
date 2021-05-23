import cv2
import threading
import logging


class Stream():
    """Class for managing stream from camera"""

    def __init__(self, stream_uri=None, **kwargs):
        self.stream_uri = stream_uri
        self.live = kwargs.get('live', True)
        self._setup_stream()
        self.live_frame = None
        if self.live:
            self._start_background_thread()

    def __del__(self):
        self._cleanup_stream()

    def _setup_stream(self):
        """Set up the video stream"""
        self.live_frame = None
        if not self.stream_uri:
            self.stream_uri = 0
        self.client = cv2.VideoCapture(self.stream_uri)

    def _cleanup_stream(self):
        """Clean up the video stream"""
        self.client.release()

    def reconnect(self):
        """Force a reconnection of the stream"""
        self._cleanup_stream()
        self._setup_stream()

    def _camera_buffer_thread(self):
        """Action to perform in thread"""
        while True:
            ret, live_frame = self.client.read()
            if ret:
                self.live_frame = live_frame
            else:
                logging.error('Stream error, restarting stream')
                self.reconnect()

    def _start_background_thread(self):
        """Start the background thread for updating images"""
        self.thread = threading.Thread(name='camera_buffer', target=self._camera_buffer_thread)
        self.thread.setDaemon(True)
        self.thread.start()

    def is_frame_empty(self, frame):
        """Checks if the frame is empty"""
        return str(type(frame)) == str(type(None))

    def get_frame(self):
        """Returns a frame from the camera"""
        if self.live:
            if not self.is_frame_empty(self.live_frame):
                return self.live_frame
            else:
                return None
        else:
            # Return from the buffer
            ret, frame = self.client.read()
            return frame

    def view(self):
        """Previews the frame on screen"""
        try:
            while True:
                frame = self.get_frame()
                if not self.is_frame_empty(frame):
                    cv2.imshow('Camera Preview', frame)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        except KeyboardInterrupt:
            pass
