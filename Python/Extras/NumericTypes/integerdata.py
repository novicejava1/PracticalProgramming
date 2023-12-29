# Enter the Octal, Hex or Binary data
data = input("Enter the Octal, Hex or Binary data : ")

if data.startswith("0o"):
    print("Convert Octal to Integer")
    intdata = int(data, 8)
    print(intdata)
elif data.startswith("0x"):
    print("Convert Hexadecimal to Integer")
    intdata = int(data, 16)
    print(intdata)
elif data.startswith("0b"):
    print("Convert Binary to Integer")
    intdata = int(data, 2)
    print(intdata)
else:
    print("Enter the Correct data")