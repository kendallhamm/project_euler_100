# 24 May 26 Hamm

a = 3


while a < 1000:

  b = a + 1

  while b < 1000:

    if (((a**2) + (b**2))**.5) % 1 != 0:
      b += 1
    else:
      c = int((((a**2) + (b**2))**.5))
      if a + b + c == 1000:
        break
      else:
        b += 1

  if a + b + c == 1000:
    break
  else:
    a += 1

print(f"a = {a}, b = {b}, c = {c}")
print(f"a + b + c = {a + b + c}")
print(f"abc = {a * b * c}")