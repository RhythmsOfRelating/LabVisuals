import osc4py3

class MBLOscReceiver:


    def __init__(self, port=9001):
        #init 
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

    def update():
        
