max_digits = (9*1) + (90*2) + (899*3) + (8999*4) + (89999*5) + (899999*6)
temp = list(range(1,max_digits))
numb = "".join(str(n) for n in temp)

def get_nth_digit(numb, n):
    numb_str = str(numb)
    return int(numb_str[n - 1])

d_1 = get_nth_digit(numb , 1)
d_10 = get_nth_digit(numb , 10)
d_100 = get_nth_digit(numb , 100)
d_1000 = get_nth_digit(numb , 1000)
d_10000 = get_nth_digit(numb , 10000)
d_100000 = get_nth_digit(numb , 100000)
d_1000000 = get_nth_digit(numb , 1000000)

ans = d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

print(ans)