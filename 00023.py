# Hamm 19 July 2026

# Thoughts
# Build a list of all the abundant numbers.
# test each value from 26-28123 to see if any two numbers in that list of abundant numbers can be added together to get it.
# Would only need to check the abundants in the list that are less than the value of interest (anything larger wont add into it.)
# Need to do some kind of cominatronics to test each of those values in each possible config to make sure that they don't sum to the original val.

import math
from itertools import combinations
import time

# Start the timer
start_time = time.perf_counter()

def proper_divisor(n):
    p_divL = [1]
    for i in range(2,math.ceil(n**.5) + 1):
        if n % i == 0:
            p_divL.append(n // i)
            p_divL.append(i)
    p_divL= set(p_divL)

    return sorted(p_divL)


def is_abundant(v: int):
    if sum(proper_divisor(v)) > v:
        return True
    else:
        return False
    
def test_addition_combinations(numbers: list):
    # numbers here is the abundant list.
    # This function finds how many possible numbers can be created by adding 2 abundant numbers. 
    results = set()
    dbl_numbers = set()
    for x in numbers:
        dbl_numbers.add(x*2)

    for combo in combinations(numbers,2):
        results.add(sum(combo))

    # Combinations does not account for examples where one number is paired with itself- such as (12,12) or (24,24). 
    # To account for them we add a set full of these possible sums (dbl_numbers) as well. 
    results = results | dbl_numbers
    return results

def main():
    abundantL = []
    ans = 0
    ceiling = 28123+1 # right lim should be 28123+1 (plus 1 to account for range exclusivity)
    for n in range(12, ceiling,1): 
        if is_abundant(n):
            abundantL.append(n)
    
    # Test to see if any of the values between 1 and ceiling to see if they can be written as the sum of two abundants. Add the ones that cannot to ans.
    add_combos = test_addition_combinations(abundantL)
    for value in range(1,ceiling):
        if value not in add_combos:
            ans += value

    print(ans)

main()


end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
