# 3 AUG 26
# Hamm
import time
import math

# Start the timer
start_time = time.perf_counter()


# c is number of columns.
# Row 1: 2*c + 1 total choice opportunities
# Row 2 through row n-1: 2*c + 1 choice opportunities
# Row n (final row): c choice opportunties
# This is a SE lattice path- all movements are east or south. 
# Final state is (2, -2) in all cases.
# In actual problem the final state is (20, -20)
# Wikipedia: 
    # https://en.wikipedia.org/wiki/Lattice_path
    # The number of NE (note NE not SE) lattice paths from (0,0) to (a,b) 
    # counts the number of combinations of a objects out of a set of 
    # a + b objects. 
    # The number of lattice paths from (0,0) to (n,k) is equal to the 
    # binomail coefficient (n + k) over n.

n = 20
k = 20
ans = math.comb(n+k, k)
print(ans)

# Wow with the help of that wikipedia article this was actually cake. 

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
