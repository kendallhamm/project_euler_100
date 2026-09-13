# Hamm 18 June 26
# Great problem to really write out the pattern on a sheet of paper and work through!

interest = 0
n = 1
square_size = 3
value = 1
increm = 2

while square_size <= 1001:
    while interest < 4:
        next_numb = n + increm
        value += next_numb
        interest += 1
        n = next_numb
    square_size += 2
    increm += 2
    interest = 0

print(value)
    