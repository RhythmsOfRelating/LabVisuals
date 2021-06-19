import threading


class StopThread(threading.Thread):
    """ Implementation of a stoppable thread class with a stop() method"""

    def __init__(self, *args, **kwargs):
        super(StopThread, self).__init__(*args, **kwargs)
        self.stop_event = threading.Event()

    def stop_thread(self):
        self.stop_event.set()

    def stopped_thread(self):
        return self.stop_event.is_set()
