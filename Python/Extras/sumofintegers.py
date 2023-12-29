total = 0
count = 0

while True:
    data = input("Enter the integer : ")
    if data:
        try:
            number = int(data)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break

if count:
    print(total, count)
