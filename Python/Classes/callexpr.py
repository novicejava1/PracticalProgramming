#!/usr/bin/env python

from typing import Any


class Callee():

    def __call__(self, *args: Any, **kwds: Any) -> Any:             # Intercept instance calls
        print('Called:', args, kwds)                                # Accept arbitrary arguments

C = Callee()
C(1, 2, 3)                              # C is a callable object
C(1, 2, 3, x=4, y=5)
