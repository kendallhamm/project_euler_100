from collections import Counter as cc

n = 1
same_digits = False
while same_digits == False:
    xL = [int(x) for x in str(n)]

    two = 2 * n
    twoL = [int(x) for x in str(two)]
    if cc(xL) == cc(twoL):
        twoL = True
    
    if twoL == True:
        three = 3 * n
        threeL = [int(x) for x in str(three)]
        if cc(xL) == cc(threeL):
            threeL = True
    
        if threeL == True:
            four = 4 * n
            fourL = [int(x) for x in str(four)]
            if cc(xL) == cc(fourL):
                fourL = True
    
            if fourL == True:
                five = 5 * n
                fiveL = [int(x) for x in str(five)]
                if cc(xL) == cc(fiveL):
                    fiveL = True
    
                if fiveL == True:
                    six = 6 * n
                    sixL = [int(x) for x in str(six)]
                    if cc(xL) == cc(sixL):
                        sixL = True

    if twoL == True and threeL == True and fourL == True and fiveL == True and sixL == True:
        same_digits = True
        print(n)
    
    n += 1
