# Hamm 24 June 26

from math import factorial as ft

curious = []
n = 3

while n < 1_000_000: # Arbitrary upper bound.
    # Could instead have used 7 * ft(9) as the upper bound because the smallest 8 digit number is 10_000_000 which is larger than 8 * ft(9). so we know that the largest possible number can only have 7 digits.
    digits = [int(d) for d in str(n)]
    val = 0
    for d in digits:
        val += ft(d)
    if val == n:
        curious.append(val)
    n += 1

print(curious)
print(sum(curious))