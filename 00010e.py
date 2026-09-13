# n is number of interest
import math
n = 2000000
is_prime = [True] * (n)
is_prime[0] = False
is_prime[1] = False
primes = []
p = 2
sqrtnfloor = math.floor(n**.5)

while p <= sqrtnfloor:
    if is_prime[p]: # Same as if is_prime[p] == True
        for multiple in range(p*p , n , p):
            is_prime[multiple] = False

    p += 1

for position, value in enumerate(is_prime):
    if value == True:
        primes.append(position)

print(primes)
print(sum(primes))