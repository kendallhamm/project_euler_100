import math

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
    n = 600_851_475_143
    divisor = 3
    largest_prime_factor = 0
    while divisor < n**.5:
        if is_prime(divisor):
            if n % divisor == 0:
                largest_prime_factor = divisor
        divisor += 2
    print(largest_prime_factor)

main()
            