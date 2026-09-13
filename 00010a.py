# Reworked on 5 Aug 26 to assist with problem 50

import time
import math
# Start the timer
start_time = time.perf_counter()



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


def main():
    n = 1_999_999
    # n = 9
    sum_primes = 2
    while n > 0:
        if is_prime(n):
            sum_primes += n
        n -= 2
    print(sum_primes)

main()










# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
