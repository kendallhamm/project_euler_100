import time

# Start the timer
start_time = time.perf_counter()

# --- Your code goes here ---
# Code code codey code code
# ---------------------------

# (X ** 1/n) returns the nth root. 
# print(4 ** (1/2)) # ==2
# Odd rounding behavior in the test case of 16807, not behaving as an int, so rounding to 5 decimal places. 
# Need to determine what the actual search space is here. 
# This code is correct but will never find the right ans testing all known numbers. 
"""
# My first version without any optimization. Works for the test cases because they are small but not for anything else. 
x = 1
exist = []
while x <= 16_807:
    digit_count = len(str(x))
    b = round(x ** (1/digit_count),5)
    if b % 1 == 0:
        exist.append(int(x))
    x += 1

print(exist)
"""


x = 1
z = 0
y = 9
exist = []
while x > 0:
    if len(str(y**x)) == x:
        x += 1
    else:
        # z is the last value that len(9**x) == x
        z = x - 1
        break

while z > 0 and y > 0:
    # If y ** z has same number of digits as value of z, we want to store that number in our list and subtract 1 from y.
    if len(str(y ** z)) == z:
        exist.append(y ** z)
        y -= 1
    # Otherwise we want to start back at 9 and count down z one. Then rerun the first if statement in this loop.
    else:
        y = 9
        z -= 1

print(exist)
print(len(exist))



# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
