import random

rows = 4
cols = 7

for row in range(rows):
    for col in range(cols):
        number = random.randint(0, 1)
        print("{0:5}".format(number), end=" ")
    print("\n")
