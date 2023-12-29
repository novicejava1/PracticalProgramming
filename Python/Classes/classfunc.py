class student:
    pass

student.name = 'Bob'                        # Just objects with attributes
student.age = 40
student.result = 'pass'

def getresults(obj):
    return obj.result

x = student()                               
status1 = getresults(x)                     # calling a simple function using the class instance object

student.resultstats = getresults            # assigning class attribute to a function
status2 = x.resultstats()                   # invoking a class method. The first argument to the method is the instance object ie. subject

print(status1)
print(status2)