# Find sum of all primes  < 2000000
# Prime is an int that only divides EVENLY by 1 and itself.
import math

n = 1999999
primes = [2]
while n > 1:
    s = n**.5
    limit = math.floor(s)
    if n % limit == 0 and limit != 1:
        n -= 2
        continue # skip the rest of the tests and move on to next number because it has a factor.
    else:
        factor_found = False
        v = limit
        while factor_found == False and v >= 1:
            if n % v == 0 and v == 1 and v not in primes:
                factor_found = True
                primes.insert(0 , n)
                break
            elif n % v != 0:
                factor_found = False
                v -= 1
                continue
            else:
                factor_found = True
                v -= 1
    n -= 2 #only move down odd numbers
print(primes)
print(sum(primes))