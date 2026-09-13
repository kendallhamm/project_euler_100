# Hamm 16 JUL 26

import time

# Start the timer
start_time = time.perf_counter()

large = 0
a = 1
b = 2
for a in range(1,100,1):
    for b in range(2,100,1):
        cL = []
        c = a**b
        for i in str(c):
            cL.append(int(i))
        if sum(cL) > large:
            large = sum(cL)

print(large)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")