# Hamm 17FEB26
# num_of_interest = 13195

# This is correct but way too inefficient and will never complete. IT works on the example number but not on the actual.

num_of_interest = 600851475143

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True

initial_list = []
prime_list = []
for i in range(1, num_of_interest):
  if num_of_interest % i == 0:
    initial_list.append(i)
  else:
    pass
#print(initial_list)

for i in initial_list:
  is_prime = True
  for j in range(2,i):
    if i % j == 0:
      is_prime = False
      break
  if is_prime and i > 1:
    prime_list.append(i)
  else:
    pass

print(f"The list of all prime factors are {prime_list}")
print(f"The largest prime in that list is {max(prime_list)}")

n = max(prime_list)
isPrime2(n)