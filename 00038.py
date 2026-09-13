# Hamm
# 22 June 2026
from collections import Counter as cc


pd = list(range(1,10,1))
n = 9000
m = 1 # Multiplier

# Can start with 9000 because the largest pandigital will HAVE to start with a 9. so the first 4 digits will be 9000 x 1 of the first value and go up from there. 

# can tweak this slightly to get my original solution, unoptimized by resetting n = 2, and then choosing the largest value from the printed values. 

while n < 9999:
    numbs = list(range(m , n + 1 , 1))
    valL = [item * n for item in numbs]
    digitL = [int(digit) for val in valL for digit in str(val)]

    if cc(pd) == cc(digitL[:9]):
        digitI = "".join(map(str, digitL[:9])) # turn the multiplied list into a single value int.
        
        print(digitI)
    
    n += 1
