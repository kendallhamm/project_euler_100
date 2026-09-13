# Hamm 3 Jul 26
import math
import time

# Start the timer
start_time = time.perf_counter()

x = 10
curious_num = []
curious_denom = []
vals = []

for num in range(x, 100, 1): # 1, 100, 1
    for denom in range(x + 1, 101, 1):
        num_str_L = list(str(num))
        num_int_L = [int(x) for x in num_str_L]
        denom_str_L = list(str(denom))
        denom_int_L = [int(x) for x in denom_str_L]
        if any(i in denom_int_L for i in num_int_L):
            matching = list(set(num_int_L).intersection(denom_int_L))
            i = matching[0]
            try:
                num_int_L.remove(i)
                denom_int_L.remove(i)
                numerator = num_int_L[0]
                denominator = denom_int_L[0]
                if num / denom == numerator / denominator and numerator < denominator:
                    curious_num.append(num)
                    curious_denom.append(denom)
            except ZeroDivisionError:
                continue
curious_num = [x for x in curious_num if x % 10 != 0]
curious_denom = [x for x in curious_denom if x % 10 != 0]
for x in range(0, len(curious_num)):
    vals.append(curious_num[x] / curious_denom[x])
print(f"FINAL ANSWER: {int((math.prod(vals)) * 10000)}") # Not sure a better way to do this. The ans is obv 100 based on the returned value of 0.01, or 1/100, but not sure how to programatically get there. The 10000x is just hard coded....
print(f"Curious Numerators: {curious_num}")
print(f"Curious Denominators: {curious_denom}")
print(f" Decimal Values: {vals}")



end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")