values = 0
f_lst = []
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0 , 10):
            for d in range(0 , 10):
                e = (a**4) + (b**4) + (c**4) + (d**4)
                if len(str(e)) == 4:
                    e_lst = []
                    for char in str(e):
                        e_lst.append(int(char))
                    e_lst = sorted(e_lst)
                    # print(e_lst)
                    mult_lst = []
                    mult_lst.append(a)
                    mult_lst.append(b)
                    mult_lst.append(c)
                    mult_lst.append(d)
                    mult_lst = sorted(mult_lst)
                    # print(mult_lst)
                    if mult_lst == e_lst:
                        # values += e
                        print(a,b,c,d,e)
                        f_lst.append(e)


print(sum(list(set(f_lst))))