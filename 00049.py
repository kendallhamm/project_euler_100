# Hamm 27 JUL 26
# This is a good one to come back to. Not an actual programmatic, exhausitve solution. Made several assumptions (specifically, where in the sequence the arithmetic match would appear) that work but only because they work, not because it was a good assumption. 
import time
from itertools import permutations
import math


# Start the timer
start_time = time.perf_counter()

# --- Your code goes here ---

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

# Func scope:
# Take the number as input, build all possible combinations.
# Keep the combinations that are prime.

def combos(n: int):
    prime_options = []
    digitsL = [int(x) for x in str(n)]
    a = set(permutations(digitsL))
    for x in a:
        b = int("".join(map(str,x)))
        if is_prime(b):
            prime_options.append(b)
    prime_options = sorted(prime_options)
    L = len(prime_options)-1
    if L >= 2:
        if prime_options[L] - prime_options[L-1] == prime_options[L-1] - prime_options[L-2]:
            return prime_options
        else:
            return "cat"
    else:
        return "cat"

def main():
    n = 1001 # Default is 1001
    ans = []
    # breakpoint()
    while ans == []:
        digits = [int(d) for d in str(n)]
        if not is_prime(n):
            n += 2
            continue
        elif 0 in digits:
            n += 2
            continue
        else:
            var = combos(n)
            # print(var,type(var))
            if var != "cat":
                ans = var     
            n += 2
    L = len(ans) - 1 # (-1) to account for 0 based index
    indices = [L-2,L-1,L]
    final_ans = "".join(str(ans[i]) for i in indices)
    print(final_ans)

main()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
