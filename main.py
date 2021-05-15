from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
from osc4py3 import oscchannel as osch


def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    pass

def handlerfunction2(address, s, x, y):
    # Will receive message address, and message data flattened in s, x, y
    print(address)
    print(s, x, y)
    pass

# Start the system.
osc_startup()

# Make server channels to receive packets.
osc_udp_server("127.0.0.1", 9001, "Rvalues")
#osc_udp_server("0.0.0.0", 3724, "anotherserver")

# Associate Python functions with message address patterns, using default
# argument scheme OSCARG_DATAUNPACK.
osc_method("/Rvalues/*", handlerfunction)
# Too, but request the message address pattern before in argscheme
osc_method("/Rvalues/*", handlerfunction2, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

# Periodically call osc4py3 processing method in your event loop.
finished = False
while not finished:
    # …
    osc_process()
    # …

# Properly close the system.
osc_terminate()