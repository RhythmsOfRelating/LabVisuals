from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
from osc4py3 import oscchannel as osch

from mbl_osc_receiver import MBLOscReceiver

osc_receiver = MBLOscReceiver("Rvalues")
osc_receiver.initialize()