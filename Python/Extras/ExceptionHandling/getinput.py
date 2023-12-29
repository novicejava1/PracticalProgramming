i = 0
while i < 5:
    try:
        x = int(input("Enter a valid integer : "))
        break
    except ValueError:
        print("Not a valid integer to process")
    i = i + 1
