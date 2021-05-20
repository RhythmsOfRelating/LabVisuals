from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
from osc4py3 import oscchannel as osch
import time
#from mbl_osc_receiver import MBLOscReceiver

#osc_receiver = MBLOscReceiver("Rvalues")
#osc_receiver.initialize()

from mbl_lsl_receiver import MBLLSLReceiver

lsl_receiver = MBLLSLReceiver()
lsl_receiver.resolve_streams()
lsl_receiver.start_listener()
time.sleep(10)
lsl_receiver.stop_listener()