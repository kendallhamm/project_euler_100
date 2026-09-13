# Hamm 4 July 2026
solutions = {}
p = 1000

while p > 0:
    temp_list = []
    for a in range(1, (p - 2) + 1, 1 ):
        for b in range(a + 1, (p - a - 1) + 1, 1 ):
            c = p - a - b
            if (a**2) + (b**2) == c**2 and a + b + c == p:
                temp_list.append(a)
                temp_list.append(b)
                temp_list.append(c)
    if len(temp_list) > 0:
        solutions[p] = len(temp_list) / 3
    p -= 1

print(f"Max Value: {max(solutions.values())}")
print(f"P for max number of solutions: {max(solutions, key=solutions.get)}")