# Hamm 23 MAY 26

base = 5 * 7 * 11 * 13 *17 *19

n = 1
while True:
  new = base * n
  if new % 20 == 0 and new % 16 == 0 and new % 18 == 0 and new % 19 == 0:
    print(new)
    break
  else:
    n += 1