
def duplicate(arr):
    tortise = arr[0]
    hare = arr[0]
    print("tortise : ", tortise)
    print("hare : ", hare)

    while True:
        tortise = arr[tortise]
        hare = arr[arr[hare]]
        print("tortise : ", tortise)
        print("hare : ", hare)
        if tortise == hare:
            break

    ptr1 = arr[0]
    ptr2 = tortise
    while ptr1 != ptr2:
        print(ptr1)
        print(ptr2)
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]
        print(ptr1)
        print(ptr2)

    return ptr1

arr = [3, 5, 1, 2, 4, 5]
print(arr)
print(duplicate(arr))
