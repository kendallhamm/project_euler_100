# Hamm 20 OCT 26

import time

start_time = time.perf_counter()

# There is certainly a way to do this without a million nested for loops. But this way makes sense to me so going to rock it. 
# Initially had 8 nested loops but was taking foreverrr to solve. By just removing that last loop (left the original code in place to show intial thought process) it took the solve time down from > 5 min (and to be clear I never got an answer, I just killed it around 5 min) to about 4 seconds. Acceptable. 
def main():
    ways = 0
    for a in range(0,2):
        for b in range(0,3):
            for c in range(0,5):
                for d in range(0,11):
                    for e in range(0,21):
                        for f in range(0,41):
                            for g in range(0,101):
                                temp = (200*a) + (100*b) + (50*c) + (20*d) + (10*e) + (5*f) + (2*g)
                                if temp <= 200:
                                    h = 200 - temp
                                    value = (200*a) + (100*b) + (50*c) + (20*d) + (10*e) + (5*f) + (2*g) + (1*h)
                                    if value == 200:
                                        ways += 1

                                # This technique is probably correct but takes wayyyyy too long. 
                                # By removing this last factor (h) and solving for it in a closed form way we cut down a ton of time reqd to solve. 
                                # for h in range(0,201):
                                #     value = (200*a) + (100*b) + (50*c) + (20*d) + (10*e) + (5*f) + (2*g) + (1*h) # Solving for pence, not pounds
                                #     if value == 200:
                                #         ways += 1
    print(ways)

main()

















end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
