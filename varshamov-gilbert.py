from scipy import special


def check_varshamov(n, k, d):
    total = 0
    for i in range(d - 1):
        total += special.comb(n - 1, i)
    return total < 2 ** (n - k)


d = 1
n = 10
k = 6
while check_varshamov(n, k, d):
    d += 1
d -= 1
print(d)
# 3
