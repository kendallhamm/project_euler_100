fib = []

fib.append(1)
fib.append(1)
flag = False
n = 3
m = 1
while flag == False:
    f_n = fib[m] + fib[m-1]
    fib.append(f_n)
    if len(str(f_n)) == 1000:
        print(len(fib))
        flag = True
        break

    m += 1
    n += 1
