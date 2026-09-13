# Hamm 4 July 2026
import time

start_time = time.perf_counter()
triangleL = []
pentagonL = []
hexagonL = []



def triangle_L(n):
    val = int((n * (n + 1)) / 2)
    triangleL.append(val)
    return triangleL

def pentagon_L(n):
    val = int((n * ((3 * n) - 1)) / 2)
    pentagonL.append(val)
    return pentagonL

def hexagon_L(n):
    val = int((n * ((2 * n) - 1)))
    hexagonL.append(val)
    return hexagonL

def main():
    n = 1

    while n <= 100000: # Wild guess- started at n <= 1000, incr by 1 order of magnitude until I got an ans. 
        triL = triangle_L(n)
        penL = pentagon_L(n)
        hexL = hexagon_L(n)
        n += 1
    
    common_values = set(triL) & set(penL) & set(hexL)

    # Result is what values are in all those sets.
    result = list(common_values)
    print(result)

    
main()


# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
