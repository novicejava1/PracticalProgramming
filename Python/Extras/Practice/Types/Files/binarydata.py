#!/usr/bin/env python

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('bindata.txt', 'wb')
file.write(packed)

file.close()