'''
Created on Oct 9, 2017

@author: eugenep
'''
import socket

'''
cool string is matching count except one
[] () {} balanced

import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

get_ip_address('eth0')  # '192.168.0.110'
'''



print socket.gethostbyname(socket.gethostname())