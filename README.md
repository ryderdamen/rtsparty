# RTSParty
A RTSP module that makes it easy to grab live frames from a RTSP stream. This package basically just wraps cv2 and lets you grab the latest frame from the camera, instead of relying on the buffer.


## Usage
```python
from rtsparty import Stream


stream = Stream('rtsp://username:password@10.0.0.1/endpoint/', live=True)

# Get a live frame from the camera
live_frame_from_camera = stream.get_frame()

# Force a reconnection
stream.reconnect()

# Show a live view of the stream
stream.view()
```

To grab the latest frame from the camera no matter what, construct the stream with live=True (or leave it out, it's the default):

```python
stream = Stream(live=True)
stream = Stream()
```

To use the buffer, which may not provide the most live images from the camera, set live to False.

```python
stream = Stream(live=False)
```

By leaving out the first argument in the Stream constructor, it will by default use the default video capture device on your machine (your webcam most likely).
