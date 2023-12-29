def hellopython():
        return "Hello Python World"

result = hellopython()
print(result)

def times(x, y):
    return x*y

product = times(10, 20)
print(product)
print(dir(times))
print(times.__name__)
print(__name__)

repetition = times("Madam", 10)
print(repetition)