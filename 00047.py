import time
import math

# Start the timer
start_time = time.perf_counter()

# --- Your code goes here ---
# Code code codey code code
# ---------------------------



# This function checks if n is prime and returns True or False.
def is_prime(n):
    if n < 2: # 1, 0, negative all false
        return False
    if n == 2: # 2 is only even prime.
        return True
    if n % 2 == 0: # All other evens are Composite (false)
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
        # If this n % i test runs all the way through all i's and does not trigger False the number n must be prime. 
    return True

def factor_unique_prime(p):
    primes = []
    factors = []

    for i in range(2,math.isqrt(p) + 1,1):
        if is_prime(i):
            primes.append(i)

    next = p
    for prime in primes:
        while next % prime == 0:
            if prime not in factors:
                factors.append(prime)
            next //= prime # Divides current next by prime, rounds down to nearest whole number.

# This catches cases where the last prime factor is actually > sqrt(p), for example in case p = 26, 13 never makes it into primes. 
# This ensures 13 still gets added to the factors list. 
    if next > 1: 
        factors.append(next)
    return factors

# Test unique prime function against known answer. 
# print(factor_unique_prime(644))
print(factor_unique_prime(14))
print(factor_unique_prime(26))
print(factor_unique_prime(84))

def main():
    x = 1 # Was able to start here because through trial and error I cleared the space from 0 to 10_000
    len_val = 4
    while x < 1_000_000:
        if len(factor_unique_prime(x)) == len_val:
            if len(factor_unique_prime(x + 1)) == len_val:
                if len(factor_unique_prime(x + 2)) == len_val:
                    if len(factor_unique_prime(x + 3)) == len_val:
                        print(x)
                        print(factor_unique_prime(x))
                        print(x + 1)
                        print(factor_unique_prime(x + 1))
                        print(x + 2)
                        print(factor_unique_prime(x + 2))
                        print(x + 3)
                        print(factor_unique_prime(x + 3))
                        break

        x += 1

main()









# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
