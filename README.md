# protozmq

# Install:

    pip install git+https://github.com/cta-sst-1m/protozmq


# Trying this out:

To use it, one must obviously start an event source, e.g.

    Build.MacOS/bin/DummyCameraServer --streams 1 --baseport 1234 --hertz 1

and then within python:

```python
>>from protozmq import EventSource
>>source = EventSource("tcp://localhost:1234", "L0")
>>message = source.receive_message()
```

and keep calling `receive_message()` to get the data from the real-time streams.
