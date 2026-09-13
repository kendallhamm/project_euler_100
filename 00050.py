import math
import time

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

# Build a list of all primes from 2-n
def prime_list(n):
    a = 3
    prime_list = [2] # Start with 2 in the list
    while a <= n:
        if is_prime(a):
            prime_list.append(a)
        a += 2
    return prime_list


# Prefix Sums calcs a list of cumulative sums from a generated list of primes. 
# Good test number to refresh on what is happening here using a list of all primes <= 10 (prime_list(10))

def prefix_sums(c):
    # values_prime = prime_list(300_000)
    values_prime = prime_list(c) # Test case
    pre_sums = [0]

    # for each value in values_prime[] i will add the value (val) to the LAST item in pre_sums. 
    # initial iteration would be 0 + 2, the next would be 2 + 3 etc.
    for val in values_prime:
        pre_sums.append(pre_sums[-1] + val)

    return pre_sums

def main():
    ...
    # Main needs to build the prefix sums list.
    # Then it needs to iterate through each and subtract every precediing value from each individual in prefix sums and see if it is prime. 
    ceiling = 1000000
    prefix_sum_L = prefix_sums(ceiling)
    how_many_consec = 0
    largest_prime = 0
    prime_listed = prime_list(ceiling)
    # Convert to a set here bc it is much more efficient to search.
    prime_set = set(prime_listed)

    # We know that the final answer can't be larger than 1_000_000.
    # This quick loop lets us set the first point of our later loops by establishing an upper
    # limit to the process that makes sense and optimizes run time. WE could alternatively use a different technique
    # given below in commnets. Actually, the other technique ran faster (4.25 sec vs 4.66 seconds) but this optimization 
    # also make more sense conceptually. 
    for prime in prefix_sum_L:
        if prime < ceiling:
            continue
        else:
            max_length = prime
            break

    # Can stop at 21 based on problem statement. could also leave blank.
    # Could have used range(len(prefix_sum_L - 1, 21, -1)) but this requires a little of excess work. 
    # length is a window length of potential consect sums.
    for length in range(max_length, 21, -1): 
        for start in range(len(prefix_sum_L) - length):
            end = start + length

            # total is the value of a consecutive sum
            total = prefix_sum_L[end] - prefix_sum_L[start]


            if total > ceiling:
                break

            # Allows us to essentially quit as soon as we find the very first one.
            if total in prime_set:
                how_many_consec = length
                largest_prime = total
                print(f' Largest Prime: {largest_prime}')
                print(f' Consecutive Length: {how_many_consec}')
                return
                



main()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
