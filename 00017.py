# Hamm 2 Jun 2026
# %pip install num2words
from num2words import num2words

a = 1
c = 0 # Character count

while a <= 1000:
  b = num2words(a)
  for i in b:
    if i == " ":
      b = b.replace(i, "")
    elif i == "-":
      b = b.replace(i, "")
  c += len(b)
  a += 1

print(c)