# Hamm 14 June 26

value = 0
for n in range(1000 , 354294 + 1): # 6 * 9**5 = 354294
    n_str = str(n)
    n_lst = []
    for char in n_str:
        n_lst.append(int(char))
    fifth = [x ** 5 for x in n_lst]
    if sum(fifth) == n:
        value += n
print(value)
        
