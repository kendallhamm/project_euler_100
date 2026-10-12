import time
import math
from functions import prime_list_seive

# prime_list_seive(n) builds a list of all primes up to n

start_time = time.perf_counter()

# Logic:

# Start at 9 (first odd composite), called "comp"
# See what primes are less than it. Store in a temp list.
# attempt to solve: math.sqrt((comp - a_prime) / 2) 
# if ans is an integer, you're good and can move to next odd composite. 
# can determine int status by using % 1.
# if not an int you need to check another prime that is less than previous comp.
# if you check all the primes less than comp and none return ints you have found the answer.



def main():
    lotta_primes = prime_list_seive(10_000) # arbitrary cap here to efficiently find a lot of primes. Can incr if it doesn't work.
    flag = True
    counter = 9 # first odd composite
    while flag == True:
        
        if counter not in lotta_primes: # (If counter is composite)
            # Build a list of primes that are less than the counter.
            less_than_primes = [x for x in lotta_primes if x < counter]
            
            for i in less_than_primes:
                
                # if the evaluation has an integer solution the conjecture holds for this value.
                # increm counter by 2 and break this for loop 
                if math.sqrt((counter - i) / 2) % 1 == 0:
                    counter += 2
                    break
                
                # if the eval doesn't have an integer solution just go to the next i.
                elif math.sqrt((counter - i) / 2) % 1 != 0:
                    
                    # if no int soluiton AND you're on the last value of less_than_primes, then conjecture does not hold for this counter and you've found the answer.
                    if less_than_primes[len(less_than_primes)-1] == i:
                        flag = False
                        print(f'ans is {counter}')
                    
                    # if no int solution but not the last in this less_than_primes list you can just go to the next indexed item.
                    else:
                        continue
        else:
            # Only hit this when you increment into a prime (counter is in lotta_primes)
            counter += 2 

main()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")