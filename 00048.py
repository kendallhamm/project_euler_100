n = 1
val = 0
while n <= 1000:
    val += n**n
    n += 1

print(str(val)[-10:])