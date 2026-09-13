# Hamm 14 June 2026

charlies = []
values = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
for a in range(10 , 100 , 1):
    for b in range(100 , 1000 , 1):
        c = a * b
        if len(str(c)) == 4:
            reclass_str = []
            pandigit_test = []
            a = str(a)
            b = str(b)
            c = str(c)
            reclass_str.append(a)
            reclass_str.append(b)
            reclass_str.append(c)
            for item in reclass_str:
                for char in item:
                    pandigit_test.append(int(char))
            pandigit_test = sorted(pandigit_test)
            if pandigit_test == values:
                c = int(c)
                charlies.append(c)
            a = int(a)

for a in range(1 , 10 , 1):
    for b in range(1000 , 10000 , 1):
        c = a * b
        if len(str(c)) == 4:
            reclass_str = []
            pandigit_test = []
            a = str(a)
            b = str(b)
            c = str(c)
            reclass_str.append(a)
            reclass_str.append(b)
            reclass_str.append(c)
            for item in reclass_str:
                for char in item:
                    pandigit_test.append(int(char))
            pandigit_test = sorted(pandigit_test)
            if pandigit_test == values:
                c = int(c)
                charlies.append(c)
            a = int(a)


list(set(charlies))
print(sorted(charlies))
print(sum(list(set(charlies))))