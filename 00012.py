import math


def triangle_num():
    a = 0
    numb = []
    incr = 1
    counter = 0
    t = 0
    factor_count = 0
    while factor_count <= 500:
        a += incr
        t = a + t
        # numb.append(t)
        counter += 1
        factors = []
        i = 1
        while i <= math.floor(t**.5):
            if t % i == 0:
                f = t // i
                factors.append(i)
                if f != i:
                    factors.append(f)
                i += 1
            else:
                i += 1
        if len(factors) > 500:
            factor_count = len(factors)
            print(t)
            break

            
   
def main():
    triangle_num()
main()