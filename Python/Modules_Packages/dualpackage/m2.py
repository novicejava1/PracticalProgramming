#from . import m1                        # not allowed in nonpackage mode by either 2.X or 3.X
import m1

def somefunc():
    m1.somefunc()
    print('m2.somefunc')

if __name__ == '__main__':              # >>> import dualpackage.m2
    somefunc()