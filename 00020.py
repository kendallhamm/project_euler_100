# Hamm 11 June 2026
# Easiest problem to date!!!

import math
int_list = []

string_list = list(str(math.factorial(100)))
print(string_list)

for i in string_list:
  val = int(i)
  int_list.append(val)

print(sum(int_list))

