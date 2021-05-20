from pylsl import StreamInlet, resolve_stream
from threading import Thread

# more info on LSL in python here: https://github.com/labstreaminglayer/liblsl-Python
# more info on LSL in general here: https://labstreaminglayer.readthedocs.io/info/getting_started.html
# you can get LSL from pip: python -m pip install pylsl

class MBLLSLReceiver:

    def __init__(self):
        self.thread = None
        self.listen = False
        self.inlet = None

    def resolve_streams(self):
        print("looking for RValues stream")
        # note that you can resolve streams according to different
        # parameters, including 'type'
        # resolve_stream will find any streams on the local area network
        # lsl config files can be used to limit and tweak network searching
        streams = resolve_stream('name', 'RValues')
        print("establishing stream inlet for")
        # the streams items are of the type StreamInfo
        # you can print the details as a bit of xml
        print(streams[0].as_xml())
        # to establish a connection
        self.inlet = StreamInlet(streams[0])

    def start_listener(self):
        if self.inlet is None:
            print("no lsl inlet is established")
            return False
        if self.thread:
            print("already listening")
            return False
        self.thread = Thread(
            target=self._listen
        )
        self.listen = True
        self.thread.start()

    def stop_listener(self):
        self.listen = False
        self.thread.join()
        self.thread = None

    def _listen(self):
        while self.listen==True:
            # one comment about this:
            # don't worry about the timestamps, these are CPU times associated with each
            # data point and LSL has lots of fancy tools for using these to synchronize
            # multiple data streams
            # since the visualization is just displaying the newest value,
            # and since we are only dealing with one stream at a time
            # the actual time of each value is not important for us
            # also, this method will block, so if no data is available,
            # this loop will hang
            # you can pass it a timeout value if you need to
            data, timestamp = self.inlet.pull_sample()
            print(timestamp, data)

