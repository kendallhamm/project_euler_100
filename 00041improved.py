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
def gen_pandigital(x): 
    for perm in itertools.permutations(range(1, x + 1, 1)):
        # pL = list(perm)
        # pLS = []
        # for p in pL:
        #     pLS.append(str(p))
        # p = int("".join(pLS))
        # My original solution included the above lines which makes 2 lists that are only used once. The below is more pythonic and reduces memory usage. 
        yield int("".join(str(item) for item in perm))
    #     pdL.append(p)
    # print(len(pdL))
    # return pdL


def main():
    max_pd = 0
    for x in range(1, 10, 1): # Stopping at 10 because largest theoretical pandigital is 987_654_321
        # pdL = gen_pandigital(x)
        for pd in gen_pandigital(x):
            if is_prime(pd) and pd > max_pd:
                max_pd = pd
    print(max_pd)



main()
