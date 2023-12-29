x = 10

def func():
    global x;
    x = x + 10
    print(x)

func()

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)