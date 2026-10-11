# Hamm 10 OCT 26
import time
from functions import is_prime

start_time = time.perf_counter()
# Note- |a| < 1000 and |b| <= 1000
# a and b both must start at -1000 and go to 1000, n starts at 0 for each possible comb of a and b.
# This solution is a brute force technique- it is trying every possible combination of a and b and then using n, starting at 0. 

def quad(a, b, n):
    y = n**2 + a*n + b
    return y

def main():
    counter = 0
    for a in range(-1000,1000,1):
        for b in range(-1000,1001,1):
            flag = True # Loop control flag for n, more straightforward to me to write a while loop than a for loop since the number of iterations is unkn.
            n = 0
            while flag == True:
                if is_prime(quad(a,b,n)):
                    n += 1
                else: # if not prime we can move to the next values of a and b.
                    # but check to see if this amount of consecutive primes is larger than the current one we're caching. If it is larger we want to store this one as counter.
                    # We also need to store a and b so we can mult them at the end. 
                    if counter < n:
                        counter = n
                        bigA = a
                        bigB = b
                        bigN = n
                    flag = False
    ans = bigA * bigB
    print(f'a = {bigA}')
    print(f'b = {bigB}')
    print(f'n = {bigN}')
    print(f'Quadratic Equation reads n**2 + ({bigA}*n) + {bigB}')
    print(f'answer = {ans}')

main()

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")