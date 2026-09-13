# Hamm 13 JUN 26

numbs = []
a = 2
b = 2
while a <= 100:
    while b <= 100:
        numbs.append(a**b)
        b += 1
    b = 2
    a += 1

dupe_removed = list(set(numbs))
print(len(dupe_removed))