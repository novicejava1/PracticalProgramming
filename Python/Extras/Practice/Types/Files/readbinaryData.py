#!/usr/bin/env python

import struct

data = open('bindata.txt', 'rb').read()

print(data)

print(data[4:8])

print(list(data))

unpacked = struct.unpack('>i4sh', data)

print(unpacked)