P = "mad"
T = "aadammadammadam"

def find_brute(T, P):
    n, m = len(T), len(P)
    print(n, m)

    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


data = find_brute(T, P)
print(data)


