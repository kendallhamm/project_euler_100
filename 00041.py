import math
import itertools

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


# This function generates pandigital numbers of length x and returns them as a list. 
# To increment up between pandigitals of different len() you need to multiply x by 10. 
def gen_pandigital(x):
    pdL = []
    one_to_n = list(range(1,len(str(x)) + 1,1))
    for perm in itertools.permutations(one_to_n):
        pL = list(perm)
        pLS = []
        for p in pL:
            pLS.append(str(p))
        p = int("".join(pLS))
        pdL.append(p)
    return pdL


def main():
    max_pd = 0
    x = 1
    while len(str(x)) <= 9:
        pdL = gen_pandigital(x)
        for pd in pdL:
            if is_prime(pd) and pd > max_pd:
                max_pd = pd
        x *= 10
    print(max_pd)

main()