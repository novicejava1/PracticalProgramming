#!/usr/bin/env python

class Person:
    def __init__(self, name, jobs, age=None) -> None:           # class = data + logic
        self.name = name
        self.jobs = jobs
        self.age = age
    
    def info(self):
        return (self.name, self.jobs)
    

rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.info())                  # call instance methods
print(rec2.info())

print(rec1.jobs)                    # retrieve instance attributes
print(rec2.jobs)