# Hamm 24 June 26

import math


ans = 0
def n_choose_r(n ,r):
    ways = int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    return ways
# print(n_choose_r(5, 3))
# print(n_choose_r(23, 10))

for n in range(1, 101, 1):
    r = 0
    for r in range(r, n + 1, 1):
        if n_choose_r(n,r) > 1_000_000:
            ans += 1

print(ans)