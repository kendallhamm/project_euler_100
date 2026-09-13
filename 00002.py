# Hamm 15FEB26

x = 0
y = 1
z = 0
even_fib = 0

limit = int(input("What's the upper limit? "))

while z < limit:
  z = y + x
  if z % 2 == 0: # z / 2 has no remainder, must be even
    even_fib += z
  else:
    pass

  # Shift each variable in the sequence
  z = x + y
  x = y
  y = z

print(f"sum of even-values is {even_fib}")