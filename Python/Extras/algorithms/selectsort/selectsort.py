import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    min_ind = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_ind]:
            min_ind = j
    A[i], A[min_ind] = A[min_ind], A[i]
    print(A)
