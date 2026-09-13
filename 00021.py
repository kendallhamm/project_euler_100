import time
import math

# Start the timer
start_time = time.perf_counter()

def proper_divisor(n):
    p_divL = [1]
    for i in range(2,math.isqrt(n) + 1):
        if n % i == 0:
            p_divL.append(n // i)
            if i != n // i:
                p_divL.append(i)
    # Edge case of n = 1 or 0 (no proper divisors)
    if n == 1 or n == 0: 
        p_divL = []
    return p_divL

def get_amicable():
    amicables = []
    a = 1 # In this function a is only a counter. b and c  are the amicables. 
    while a < 10_000: #10_000
        # if a in amicables:
        #     continue
        # Get sum of proper divisors of a
        a_p_div_sum = sum(proper_divisor(a))

        b = a_p_div_sum
        # print(b)

        # Get sum of proper divisors of b,the sum(proper_divisors(a))
        b_p_div_sum = sum(proper_divisor(b))
        c = b_p_div_sum
        # print(c)

        # Test if a == c. If so, append both to list of amicables assuming they aren't already in that list and a != b.
        if c == a and a != b:
            if c not in amicables:
                amicables.append(c)
            if a not in amicables:
                amicables.append(a)
            
        a += 1
    print(amicables)
    return amicables

def main():
    ans = sum(get_amicable())
    print(ans)

    
    

main()

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
