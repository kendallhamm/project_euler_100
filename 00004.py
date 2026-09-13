# Hamm 23 MAY 26

# Starting from 999,999 ID palindromes.
import sys

n = 999
while n >= 100:
  n_str = str(n)
  m_str = str(n)[::-1]
  pal = int(n_str + m_str)

  i = 999
  while i >= 100:

    if pal % i == 0 and 100 <= int(pal / i) <= 999:
      print(f"Factor 1 is {i}")
      print(f"Factor 2 is {int(pal / i)}")
      print(f"The largest palindrome is {pal}")
      sys.exit()
      # break


    else:
      i -= 1

  n -= 1