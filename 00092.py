# 29 JUL 26
# Reflection: This works but takes aobut 30 seconds. It should take 2-5 tops. 
# I don't think my chain_vals list is working like I think it is, but my counters (one and eightynine) are working correctly. 


import time
# review the problem 14 solution on website
# Start the timer
start_time = time.perf_counter()

# chain_vals list should become a record of all the values we've computed where the index is the number(10) and the list value is the sum(square digits). Ex: chain_vals[10] = 1, chain_vals[44] = 32
# Execute chain opns, return either 1 or 89 (end of chain)
def run_chain(n):
    ss = 0
    c = n
    if c == 1 or c == 89:
        if c == 1:
            chain_vals[c-1] = 1
            return c
        elif c == 89:
            chain_vals[c-1] = 89
            return c
    if chain_vals[c-1] != 0:
        # Get the value of that index:
        return chain_vals[c-1]
    while c != 1 and c != 89 and ss != 1 and ss != 89:
        digits = [int(d) for d in str(c)]
        squares = []
        for d in digits:
            squares.append(d**2)
        ss = sum(squares)
        if ss == 1:
            chain_vals[c-1] = ss
        elif ss == 89:
            chain_vals[c-1] = ss
        c = ss
    return ss

def main():
    a = 1 # should be one (1)

    # Count of one's and count of eightynines.
    one = 0
    eightynine = 0

    while a <= ceiling:
        ran_chain = run_chain(a)

        # Add to the counters one and eightynine
        if ran_chain == 89:
            eightynine += 1
        elif ran_chain == 1:
            one += 1
        a += 1
    print(f' Number of 1s: {one}')
    print(f' Number of 89s: {eightynine}')
    print(f' Number of 1s + number of 89s: {one} + {eightynine} = {one + eightynine}')
    print(f'89 value: {chain_vals[89-1]}')
    print(f'570 value: {chain_vals[570-1]}')
    # print(f'570-600 values: {chain_vals[570-1:600-1]}')
    print(f'1-567 values: {chain_vals[1-1:567-1]}')
    print(f'567-570 value: {chain_vals[567-1:570-1]}')


ceiling = 9_999_999
size_list = 9_999_999 # Should be able to be (7 * 9**2) = 567. Not sure why that doesn't work. 
chain_vals = [0] * size_list # Chain exactly as long as the amount of starting numbers
main()


# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
