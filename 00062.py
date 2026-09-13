# Hamm 4 SEP 26

# This one was very difficult. Left my original approach mostly at the bottom. AFter I got that far and was really going nowhere Claude /learn suggested building a way to track all the individual cubes by the digits, after sorting them. This builds a much easier way to see what specific cubes are related/in same family. Then it becomes a length check (how many families of five) and from there, whats the smallest. 
# the ceiling to the problem was hard to grasp so I decided to check 'fields' 10x at a time in main()
# neat trick learned: setdefault() for adding/working with dicts!
import time
# Start the timer
start_time = time.perf_counter()

# Build a set of all x**p where n is the ceiling
# 62
def power_generator(n: int, p: int): # n is ceiling, p is power.
    # build a set of 'all' cubes. [0, 1, 8, 27...]
    is_cube = set()
    for x in range(0, n):
        is_cube.add(x**p)
    return is_cube

# build a dict where the keys are the sorted cubes and the values are the original x**p
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

def main():
    c = 10 # starting ceiling
    flag = True
    cubes_of_interest = [] # this will become a list of cube families of exactly 5 cubes.
    ans = None
    while flag: 
        cubes = power_generator(c, 3)
        cD = power_sort(cubes)
        for key in cD:
            if len(cD[key]) == 5:
                for indiv in cD[key]: # cD[key] values will all be lists of len 5. i need the individual values out of there. 
                    cubes_of_interest.append(indiv)

        # If we pulled no cubes of interest at this multiple of 10, we need to mult c by 10 and do it again. 
        # This approach does ask the computer to generate and compare the same cubes multiple times. First time it does range(1, 10^1), then the next time it does 1,10^2. Could optimize further if I wanted to but not worth it here. 
        if cubes_of_interest == []: 
            c *= 10
        else:
            ans = min(cubes_of_interest)
            print(ans)
            break




# Below here is the original technique I was trying. Leaving for posterity sake. Not a great approach!

# def check_perms(cL: set):
#     import itertools
#     for x in cL:
#         counter = 0
#         # Generate all the permutations of that number. They are stored as a tuple (1,2,3) so must use str comprehension to turn them into an int (123)
#         perms = set(itertools.permutations(str(x),len(str(x))))
#         # print(perms)
#         for perm in perms:
#             num = [int("".join(p)) for p in perm] # turns tuple into a list of ints
#             # print(num)
#             value = int("".join(map(str,num))) # turns list of ints into a single int
#             # print(value)
#             # Check that value is the same as x (throw out an example where x == 0001 bc len(x) and len(value are not equal))

#             if value in cL and len(str(value)) == len(str(x)):
#                 counter += 1
#             if counter == 5:
#                 return value

#     # If counter doesn't equal 5
#     return None
        


main()
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")

