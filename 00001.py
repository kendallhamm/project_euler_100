x = 0
y = 0
z = 0
limit = int(input("What's the upper limit? "))

while x < limit:
  if x % 3 == 0:
    y += x
  elif x % 5 == 0:
    z += x
  else:
    pass
  x += 1

print(f"y + z = {y + z}")

# correct, solved 15 FEB