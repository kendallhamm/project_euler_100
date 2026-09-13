# Hamm 1 Jul 2026
# Had the right answer for a while but didn't trust my own work....

import math
import time
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
    n = 11
    trunc_primes = []
    while len(trunc_primes) < 11:
        if is_prime(n):

            # Decompose from L to R
            trunc_flagLR = True
            x = n

            while len(str(x)) > 1 and trunc_flagLR == True:
                x = int(str(x)[1:])
                if is_prime(x) != True:
                    trunc_flagLR = False
                    break
            
            # Decompose from R to L
            trunc_flagRL = True
            x = n

            while len(str(x)) > 1 and trunc_flagLR == True and trunc_flagRL == True:
                x = x // 10
                # print(x , n)
                if is_prime(x) != True:
                    trunc_flagRL = False
                    break

            if trunc_flagLR == True and trunc_flagRL == True:
                trunc_primes.append(n)
            n += 2

        else: n += 2

    print(trunc_primes)
    print(sum(trunc_primes))

main()
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")