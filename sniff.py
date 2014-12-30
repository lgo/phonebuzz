#!/usr/bin/env python2

import scapy.all as scapy
import time

# interface to use, should normally be mon0
interface = "mon0"

# minutes since the device was last seen before the doorbell will consider it a new visit
MINUTES_SINCE = 4
SECONDS_SINCE = MINUTES_SINCE * 60

observedclients = {}
registeredclients = {}

# Packet subtypes to watch
stamgmtstypes = (0, 2, 4)

def sniff_management(p):
    """
    Management for the sniffed packets.
    Keeps a record of seen MAC addresses and checks them against registered addresses to notify with

    ARGS:
     p - Sniffed Packet
    """

    # Make sure the packet has the Scapy Dot11 layer present
    if p.haslayer(scapy.Dot11):

        # Different levels of packet sniffing...
        #if True:
        #if p.type == 0:
        if p.type == 0 and p.subtype in stamgmtstypes:
            curtime = int(time.time())
            if p.addr2 not in observedclients:
                notify(p.addr2)

                print "Newly discovered - {0}".format(p.addr2)
                print p.type
                print p.subtype
            else:
                time_since = curtime - observedclients[p.addr2]
                if time_since > SECONDS_SINCE:
                    notify(p.addr2)

                    print "Revisited - {0}".format(p.addr2)
                    
            observedclients[p.addr2] = curtime


def notify(address):
    """
    Sends out a notification to another service about the seen person
    """
    pass

scapy.sniff(iface=interface, prn=sniffmgmt)