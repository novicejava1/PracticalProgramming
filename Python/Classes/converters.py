#!/usr/bin/env python

from streams import Processor

class Uppercase(Processor):
    
    def converter(self, data):
        return data.upper()
    
if __name__ == '__main__':
    import sys
    import os
    cwd = os.getcwd()
    print(cwd)
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()