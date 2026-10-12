# Functions file built to store commonly reused functions.
# Table of Contents:
# build_base_y -> Returns a number in a different base.
# count_divisor -> Counts number of unique divisors a number has. Built for P179 but not used, too inefficient.
# divisor_seive -> Uses seive technique to build all divisors through N. Returns list of all. can query to get an individual value's divisor count (see test cases, divL[x]) or look at all divisors at once. 
# factor_unique_primes -> Finds what the true prime factors are of a number. Could be improved to use prime_list instead.
# freq_dist # Build a freq distribution of any number of dice, d that have any number of sides, s. used in 205
# gen_pandigital -> generates a list of possible pandigitals.
# get_amicables -> get amicable numbers.
# is_abundant -> determines if a number is abundant. 
# is_palindrome -> determines if a number is a palindrome.
# is_prime -> Checks if a value is prime, returns T/F. Best for single prime checks.
# power_generator -> Build a set of all x**p where n is the ceiling. Works with power_sort
# power_sort -> build a dict where the keys are the sorted cubes and the values are the original x**p
# prefix_sums -> 
# prime_list_seive -> makes a list of primes less than a value using seive. Best for returning primes up to n.
# prime_list_trial -> makes list of primes using is_prime (trial division) technique. 
# proper_divisor -> gets proper divisors of a number.
# rotate -> Convert to deque of characters (double ended queue)
# rotate_w_deque -> Make a list of lists that consists of all possible ways to rotate through a value.
# triangle_problems -> max total from top to bottom in a triangle of numbers. used in 18. 


####################################
def build_base_y(n, y):
    
    # Set the base (y) you want the number system to be in. For problem 36 this is 2.
    # Divide the decimal (base 10) number by y repeatedly and record the remainders from bottom to top. 
    base_y_L = []
    val = n % y
    base_y_L.append(val)
    m , r = divmod(n, y)
    while m > 0:
        m , r = divmod(m , y)
        base_y_L.append(r)

    # Must reverse the list because right now the list is stored in the opposite order that we want. 
    # for example, build_base_two(13): base_two_L = [1, 0, 1, 1] but needs to be [1, 1, 0, 1]
    base_y_L_rev = base_y_L[::-1]
    base_y = int("".join(map(str,base_y_L_rev)))

    return base_y

# print(build_base_y(13, 2))
# # Expecting 1101
# print(build_base_y(585, 2))
# Expecting 1001001001
####################################
# build for problem 179, not used. Counts the number of divisors a number has. For large quantities (or high n) consider using divisor_seive().
def count_divisor(n):
    import math
    div = 1
    # Edge case of n = 1 or 0
    if n == 1:
        return div
    elif n == 0:
        div = 0
        return div
    elif n == 2:
        div = 2
        return div
    else:
        div += 1 # First, add the self-divisor
        limit = math.isqrt(n) + 1 + 1  # +1 first bc isqrt rounds down and we need to count that number. +1 again because right hand side of a range is exclusive.
        for i in range(2,limit): 
            if n % i == 0:
                div += 1 # count i
                # check if we need to count  n / (n/i) at this point of if it will be counted later.
                if (n / i) >= limit:
                    div += 1 
    return div

# Test cases
# print(count_divisor(6)) # Expect 4
# print(count_divisor(15)) # Expect 4 (1,3,5,15)
# print(count_divisor(16)) # Expect 5 (1, 2, 4, 8, 16)
# print(count_divisor(12)) # Expect 6 (1, 2, 3, 4, 6, 12)
# print(count_divisor(28)) # Expect 6 (1, 28, 2, 14, 4, 7)
####################################

# Used in Problem 179
def divisor_seive(N: int) -> list: # receives input of an int (ceiling of the range) and outputs a list of the count each indecies divisors
    divL = [0] * (N + 1)
    for i in range(1, N + 1): # + 1 for exclusive range boundary
        for m in range(i, N + 1, i): # iterate over multiples of i (by incrementing by i)
            divL[m] += 1 # Each multiple of i has an additional divisor (i) so we increment that value in the list by 1.
    return divL

# Test Cases
# print(divisor_seive(20))
# print(divisor_seive(35))
# print(divisor_seive(35)[20]) # Extract a specific divisor count for a specific number (this one pulls the number of divisors that the number 20 has.)
####################################

def factor_unique_prime(p):
    import math
    primes = []
    factors = []

    for i in range(2,math.isqrt(p) + 1,1):
        if is_prime(i):
            primes.append(i)

    next = p
    for prime in primes:
        while next % prime == 0:
            if prime not in factors:
                factors.append(prime)
            next //= prime # Divides current next by prime, rounds down to nearest whole number.

# This catches cases where the last prime factor is actually > sqrt(p), for example in case p = 26, 13 never makes it into primes. 
# This ensures 13 still gets added to the factors list. 
    if next > 1: 
        factors.append(next)
    return factors

# Test unique prime function against known answer. 
# print(factor_unique_prime(644))
# print(factor_unique_prime(14))
# print(factor_unique_prime(26))
# print(factor_unique_prime(84))
##########################################
# Build a freq distribution of any number of dice, d that have any number of sides, s
def freq_dist(s , d): # s is number of sides, d is number of dice
    import itertools
    dict_distrib = {i: 0 for i in range(d * 1, (s*d) + 1)} # set each value 0 for each key. Each key is a possible dice roll value.
    for combo in itertools.product(range(1,(s + 1)), repeat = d):
        for key in dict_distrib:
            if key == sum(combo):
                dict_distrib[key] += 1
                continue
    return dict_distrib
##########################################
def gen_pandigital(x):
    # This function generates pandigital numbers of length x and returns them as a list. 
    # Refer to 41.py and 41improved.py for usage of this function. 
    import itertools
    pdL = []
    for perm in itertools.permutations(range(1,x + 1, 1)):
        p = int("".join(str(item) for item in perm))
        pdL.append(p)
    return pdL
##########################################
def get_amicable():
    # Refer to problem 21 for using this. 
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
    # print(amicables)
    return amicables
##########################################
def is_abundant(v: int):
    # used in problem 23
    if sum(proper_divisor(v)) > v:
        return True
    else:
        return False
##########################################
def is_palindrome(n):
    # From problem 36.
    # Pretty straight fwd, reverse the value and see if it is same as original value. 

    n_str = str(n)
    n_str_rev = n_str[::-1]
    if int(n_str) == int(n_str_rev):
        return True
    else:
        return False
# print(is_palindrome(1001))
# # Expect True
# print(is_palindrome(15))
# # Expect False
###################################
def is_prime(n):
    # This function checks if n is prime and returns True or False.

    import math
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

# print(is_prime(91))
####################################
# Build a set of all x**p where n is the ceiling
# 62
def power_generator(n: int, p: int): # n is ceiling, p is power.
    # build a set of 'all' cubes. [0, 1, 8, 27...]
    is_cube = set()
    for x in range(0, n):
        is_cube.add(x**p)
    return is_cube
###################################
# build a dict where the keys are the sorted cubes and the values are the original cubes
# must have the power set already built (see power_generator)
# 62
def power_sort(cL: set):
    cD = {}
    for x in cL:
        key = "".join(sorted(str(x)))
        # setdefault looks up a key and if it doesnt exist inserts that key with a default value. 
        # if key is in dict: ignores the default value and returns existing for action, we immediately append x to it.
        # if not in the dict it inserts the key with the default value ( [] in this case), hands us the empty list for action, we append x to it.
        cD.setdefault(key, []).append(x)
    return cD
###################################
def prefix_sums(c):
    # Used in problem 50
    # helpful to keep a running sum list.
    # Could be improved with a seive. 
    # values_prime = prime_list_trial(300_000)
    values_prime = prime_list_trial(c) # Test case
    pre_sums = [0]

    # for each value in values_prime[] i will add the value (val) to the LAST item in pre_sums. 
    # initial iteration would be 0 + 2, the next would be 2 + 3 etc.
    for val in values_prime:
        pre_sums.append(pre_sums[-1] + val)

    return pre_sums
####################################################
def prime_list_seive(n):
    import math
    # len is n+1 so that you can use the standard 0 based indexing.
    is_prime = [True] * (n + 1)
    # set the 0 value and 1 value to False right away.
    is_prime[0] = False
    is_prime[1] = False
    primes = []

    # Assume each number in range 2, n+1 is prime (call it p)
    for p in range(2,math.isqrt(n) + 1):
        # Check our assumption- is it really true?
        if is_prime[p]:
            # If it is, for each multiple of that number, make it false.
            # start at p*p, go to n + 1, increment p. 
            # Conceptually should start at 2p, then go 3p, 4p, 5p but because we're also starting at p = 2 in range we can just say p*p and that saves us an extra loop.
            for mult in range(p*p, n + 1, p):
                is_prime[mult] = False

    # after we finish the seive/building the list of True/False go back through and check each index to see if it is True/false.
    for idx in range(0, n+1):
        if is_prime[idx]:
            # If true build a list of actual numbers that are prime.
            primes.append(idx)
    return primes
#########################################
def prime_list_trial(n):
    a = 3
    primeL = [2] # Start with 2 in the list
    while a <= n:
        if is_prime(a):
            primeL.append(a)
        a += 2
    return primeL
#########################################
def proper_divisor(n):
    # Used in problem 23
    import math
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


# print(sorted(proper_divisor(1)))
# print(sorted(proper_divisor(2)))
# print(sorted(proper_divisor(3)))
######################################
def rotate_w_deque(num: int, k: int) -> int:
    from collections import deque
    # Convert to deque of characters (double ended queue)
    d = deque(str(num))
    print(d)

    # Deque rotates right by default, so invert k for left-shift consistency
    d.rotate(-k)

    return int("".join(d))

# print(rotate_w_deque(12345,1))
######################################
def rotate_w_deque(num: int, k: int) -> int:
    from collections import deque

    # Make a list of lists that consists of all possible ways to rotate through a value. 
    rotatedL = []
    # Convert to deque of characters (double ended queue)
    d = deque(str(num))

    while len(rotatedL) < len(str(num)):
        # Deque rotates right by default, so invert k for left-shift consistency
        d.rotate(-k)
        val = int("".join(d))
        rotatedL.append(val)

    return rotatedL
##################################
# Takes a triangle and finds the max total from top to bottom. Used in 18, 67.
def triangle_problems(triangle: list):
    for row in range(len(triangle) - 2, -1, -1): # start at second row from the bottom. End at 0, but bc the range is exclusive you actually have to tell it to end at -1. increm by -1.
        collapse_row = []
        psn = 0
        for item in triangle[row]:
            collapse_item_1 = item + triangle[row + 1][psn] # add item with the value immediately below it.
            collapse_item_2 = item + triangle[row + 1][psn + 1] # add item with the value below and 1 spot to the right. 
            collapse_row.append(max(collapse_item_1, collapse_item_2))
            psn += 1 # increm psn counter to move one more spot in that list.
        triangle[row] = collapse_row # replace the original row with my collapsed version. 
    # After all iterations triangle[row] is the top-most collapsed row, and the answer to the question. 
    return triangle[0][0]
# for test purposes
# triangle = [
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
# ]
# # answer should be 23

# # test:
# print(triangle_problems(triangle))

###################################