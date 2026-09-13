# Hamm 23 MAY 26

numbs = []
sqr_numbs = []

for i in range(1, 101):
  numbs.append(i)
  sqr_numbs.append(i**2)

print((sum(numbs)**2) - (sum(sqr_numbs)))