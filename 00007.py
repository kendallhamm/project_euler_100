# Hamm 23 MAY 26
primes = [2]
n = 3

while len(primes) < 10001:
  if all(
      n % i != 0
      for i in primes if i <= n**0.5
      ):
    primes.append(n)
    # print(primes)

  n += 2
print(primes)
print(primes[-1])