# Hamm 11 June 2026

largest_count = 0
count = 0

for i in range(1, 1000000 , 1):
  n = i
  while n != 1:
    if n % 2 == 0:
      n = n / 2
    elif n % 2 != 0:
      n = (3 * n) + 1
    count += 1
  if count > largest_count:
    largest_count = count
    print(f"Length of chain: {largest_count} for starting number: {i}")
  count = 0
