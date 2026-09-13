x = 0
y = 0
z = 0
limit = int(input("What's the upper limit? "))

while x <= limit:
  y = x**2
  if y % 2 != 0:
    z += y
  else:
    pass
  x += 1

print(f"Checked all through, x = {x}")
print(f"Last square checked, y = {y}")
print(f"Sum of odd squares, z = {z}")