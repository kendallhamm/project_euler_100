# Start by looking back at problem 4. Refactor that solution into a copyable func_palindrome.py
def build_base_y(n, y):
    
    # Set the base you want the number system to be in. For problem 36 this is 2.
    # Divide the decimal (base 10) number by 2 repeatedly and record the remainders from bottom to top. 
    base_y_L = []
    val = n % y
    base_y_L.append(val)
    m , r = divmod(n, y)
    while m > 0:
        m , r = divmod(m , y)
        base_y_L.append(r)

    # Must reverse the list because right now the list is stored in the opposite order that we want. 
    # for example, build_base_two(13): base_two_L = [1, 0, 1, 1] but needs to be [1, 1, 0, 1]
    base_y_L_rev = base_y_L[::-1]
    base_y = int("".join(map(str,base_y_L_rev)))

    return base_y

print(build_base_y(13, 2))
# Expecting 1101
print(build_base_y(585, 2))
# Expecting 1001001001

def is_palindrome(n):
    n_str = str(n)
    n_str_rev = n_str[::-1]
    if int(n_str) == int(n_str_rev):
        return True
    else:
        return False
print(is_palindrome(1001))
# Expect True
print(is_palindrome(15))
# Expect False
print(is_palindrome(build_base_y(585,2)))
# Expecting 1001001001

def main():
    x = 1
    counter = 0
    base_this_prob = 2 # In problem 36 we want base of 2.
    while x < 1_000_000:
        if is_palindrome(x):
            base_two_x = build_base_y(x, base_this_prob)
            if is_palindrome(base_two_x):
                counter += x
        x += 1

    print(counter)

main()
