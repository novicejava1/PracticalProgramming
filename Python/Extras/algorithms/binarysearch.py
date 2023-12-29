import math

def binarysearch(arr, value, low, high):
    if high < low:
        return -1
    mid = math.floor(low + ((high - low ) / 2))
    if (arr[mid] > value):
        return binarysearch(arr, value, low, mid-1)
    elif (arr[mid] < value):
        return binarysearch(arr, value, mid+1, high)
    else:
        return mid

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
arr_mid = len(arr) // 2

index = binarysearch(arr, 70, 0, 13)
print(index)
print(arr[index])

