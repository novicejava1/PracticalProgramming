### Enter the range of numbers
count = int(input("Enter the range of numbers to conver : "))
base = input("Enter the base to convert : ")
print("Range of numbers : ", str(count))
print("Base to convert : ", base)

### Convert the Decimal Digit to Octal
if base == "Oct":
    for i in range(count):
        print(oct(i))
elif base == "Hex":
    for i in range(count):
        print(hex(i))
elif base == "Binary":
    for i in range(count):
        print(bin(i))
else:
    print("Enter the correct base")



