#!/usr/bin/env python

import struct

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)

values = struct.unpack('>i4sh', data)
print(values)