import math
from collections import deque
import time

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

def rotate_w_deque(num: int, k: int) -> int:
    # Make a list of lists that consists of all possible ways to rotate through a value. 
    rotatedL = []
    # Convert to deque of characters (double ended queue)
    d = deque(str(num))
    length = len(str(num))
    while len(rotatedL) < length:
        # Deque rotates right by default, so invert k for left-shift consistency
        d.rotate(-k)
        val = int("".join(d))
        rotatedL.append(val)

    return rotatedL

def main():
    n = 7
    unacceptables = [0, 2, 4, 5, 6, 8]
    circ_primes = [2, 3, 5]
    while n < 1_000_000:
        # Make a list of all digits in n.
        nL = [int(digit) for digit in str(n)]
        unacceptable_present = any(item in nL for item in unacceptables)
        if unacceptable_present:
            n += 2
            continue
        else: 
            # Call rotate_w_deque function
            test_rotations = rotate_w_deque(n,1)
            all_test_rotates_GO = True
            for rotate in test_rotations:
                # Test that number in is_prime
                if not is_prime(rotate):
                    all_test_rotates_GO = False
                    break
            if all_test_rotates_GO == True: 
                circ_primes.append(n)
        n += 2
    print(circ_primes)
    print(len(circ_primes))
                    
main()

# Notes:
# We think that every digit in the number must be 1,3,7,9.
# Presence of any other digit than 1,3,7,9 automatically throws it out of consideration. 
# Exceptions: 2, 5 when number is less than 10.

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
