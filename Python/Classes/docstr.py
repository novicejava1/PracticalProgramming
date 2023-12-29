#!/usr/bin/env python

"""I am: docstr.__doc__"""

def func(args):
    """I am: docstr.func.__doc__"""
    pass

class spam:
    """I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"""
    def method(self):
        """I am: spam.method.__doc__ or self.method.__doc__"""
        print(self.__doc__)
        print(self.method.__doc__)

if __name__ == '__main__':
    import docstr
    print(docstr.__doc__)
    print(docstr.func.__doc__)
    print(docstr.spam.__doc__)
    print(docstr.spam.method.__doc__)

    x = spam()
    print("-" * 100)
    print(x.__doc__)
    x.method()