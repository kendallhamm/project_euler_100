# This would be a good one to go back and refine. Chat suggest that I am handling leading 0 pandigital permutations incorrectly (checked after got the right answer) but just so happens that no correct solutions have a leading zero, so it doesn't matter. 
# could refine solution to make sure that the leading zero thing is accounted for correctly. 

import itertools
import time

# Start the timer
start_time = time.perf_counter()

# This function generates pandigital numbers of length x and returns them as a list. 
# Refer to 41.py and 41improved.py for usage of this function. 
def gen_pandigital(x):
    pdL = []
    for perm in itertools.permutations(range(0,x + 1, 1)):
        p = int("".join(str(item) for item in perm))
        pdL.append(p)
    return pdL

def sub_string_div():
    # Test the substring divisibility constraints specific to problem 43.
    all_pandigital = gen_pandigital(9)
    pandigital_sum = 0
    for pandigital in all_pandigital:
        pd_L = [int(digit) for digit in str(pandigital)]
        d_080910 = int("".join(str(num) for num in pd_L[7:9 + 1]))
        if d_080910 % 17 != 0:
            continue
        d_070809 = int("".join(str(num) for num in pd_L[6:8 + 1]))
        if d_070809 % 13 != 0:
            continue
        d_060708 = int("".join(str(num) for num in pd_L[5:7 + 1]))
        if d_060708 % 11 != 0:
            continue
        d_050607 = int("".join(str(num) for num in pd_L[4:6 + 1]))
        if d_050607 % 7 != 0:
            continue
        d_040506 = int("".join(str(num) for num in pd_L[3:5 + 1]))
        if d_040506 % 5 != 0:
            continue
        d_030405 = int("".join(str(num) for num in pd_L[2:4 + 1]))
        if d_030405 % 3 != 0:
            continue
        d_020304 = int("".join(str(num) for num in pd_L[1:3 + 1]))
        if d_020304 % 2 != 0:
            continue
        pandigital_sum += pandigital
    return pandigital_sum

def main():
    ans = sub_string_div()
    print(ans)

main()

# --- Your code goes here ---
# Code code codey code code
# ---------------------------

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")


