#!/usr/bin/env python

import secrets

rainbow = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

print(secrets.choice(rainbow))                  # choose a random rainbow color

maxrandnum = 65536

print(secrets.randbelow(maxrandnum))            # choose a random number below the maxrandnum

maxrandbits = 256

print(secrets.randbits(256))                    # choose a random integer with 256 bits

print(secrets.token_bytes(10))                  # generate a random token of 10 bytes

print(secrets.token_hex(10))                    # generate a random token of 10 bytes in hex code

print(secrets.token_urlsafe(16))