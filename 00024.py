# Hamm 24 June 26
# Very difficult- was able to think through the logic of the first digit pretty well myself but had a hard time reasoning through the rest of this one. Thanks to chat for some assistance on the loop logic. 

# Rank is always the position you are looking for within the current set of remaining permutations. 

from math import factorial as ft

digits = list((range(0, 10,1)))
bs = len(digits) - 1
rank = 999_999
ansL = []

for n in range(1,11,1):
    block_size = ft(bs)
    index = rank // block_size # Integer division here- will round down to nearest int.
    nxt_dig = digits.pop(index)
    ansL.append(nxt_dig)

    # Set up next iteration.
    rank = rank % block_size # Modulo operator returns the remainder after division.
    bs -= 1

ansV = "".join(str(n) for n in ansL)
print(ansV)