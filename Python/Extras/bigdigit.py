import sys

print(sys.argv[0])
data = input("Enter the number : ")
zero = ["**", "****", "**"]
one = ["*", "*", "*"]
two = ["**", "* ", "**"]
three = ["**", " *", "**"]
bigdigit = (zero, one, two, three,)
printdigit = []

try:
    number = int(data)
    print(number)
    for each in str(number):
        if each == "0":
            print("printing 0")
            printdigit.append(each)
        elif each == "1":
            print("printing 1")
            printdigit.append(each)
        elif each == "2":
            print("printing 2")
            printdigit.append(each)
        else:
            print("printing 3")
            printdigit.append(each)
except ValueError as err:
    print(err)

print(printdigit)

for row in range(3):
    for col in range(len(printdigit)):
        digit = printdigit[col]
        if digit == "0":
            print(zero[row], end = " ")
        elif digit == "1":
            print(one[row], end = " ")
        elif digit == "2":
            print(two[row], end = " ")
        else:
            print(three[row], end = " ")
    print("\n")

