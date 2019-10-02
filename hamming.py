from scipy import special


def check_hamming(n, k, d):
    t = (d - 1) // 2
    total = 0
    for i in range(t + 1):
        total += special.comb(n, i)
    return total <= 2 ** (n - k)


d = 1
n = 10
k = 6
while check_hamming(n, k, d):
    d += 1
d -= 1
print(d)
# 4
