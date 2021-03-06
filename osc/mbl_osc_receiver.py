from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
from osc4py3 import oscchannel as osch


class MBLOscReceiver:

    def __init__(self, server_name, address="127.0.0.1", port=9001):
        #
        self.finished = False
        self.server_name = server_name
        self.address = address
        self.port = port
        self.initialize()

    def initialize(self):
        self.message = ""
        self.scene = 0
        self.time = 0
        self.progress = 0
        self.numHeadSets = 0
        self.correlation = 0
        self.score = 0
        self.power1 = 0
        self.power2 = 0
        self.start()

    def start(self):
        osc_startup()
        osc_udp_server(self.address, self.port, self.server_name)
        osc_method("/Rvalues/*", self.load_r_values,
                   argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK + osm.OSCARG_MESSAGE)
        while not self.finished:
            # …
            osc_process()
            # …
        osc_terminate()

    def update(self, finished):
        # foo
        self.finished = finished
        if not self.finished:
            self.start()

    def load_r_values(self, address, s, x, y, message):
        # Will receive message address, and message data flattened in s, x, y
        print(s, x, y)
        pass

    # Getters
    def get_scene(self):
        return self.scene

    def get_time(self):
        return self.time

    def get_progress(self):
        return self.progress

    def get_numHeadSets(self):
        return self.numHeadSets

    def get_correlation(self):
        return self.correlation

    def get_score(self):
        return self.score

    def get_power1(self):
        return self.power1

    def get_power2(self):
        return self.power2

    # Setters
    def set_scene(self, scene):
        self.scene = scene

    def set_time(self, time):
        self.time = time

    def set_progress(self, progress):
        self.progress = progress

    def set_numHeadSets(self, numHeadSets):
        self.numHeadSets = numHeadSets

    def set_correlation(self, correlation):
        self.correlation = correlation

    def set_score(self, score):
        self.score = score

    def set_power1(self, power1):
        self.power1 = power1

    def set_power2(self, power2):
        self.power2 = power2
