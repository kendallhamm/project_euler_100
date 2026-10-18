# Hamm 18 OCT 26
import time
from functions import is_palindrome
start_time = time.perf_counter()

# Lychrel number: reverse and add process NEVER forms a palindrome. 
# Example- 196 is the smallest Lychrel number.


# Build a list (len(10000) that is all "cat". 
def longL(n):
    L = ["cat"] * n
    return L

def is_lychrel(n, masterL): 
    # Needs to return two things:
        # Whether n is a lychrel
        # all the numbers we iterated through in the process so that if it is NOT a lychrel we can then turn all the values that are in the index of non_lychrel to True.
    # masterL is the total list of the full range that we are interested in. Using it is not really necessary but by including it and then modifying it (in Main, based on what we return here) future iterations are cheaper and faster. 


    # Documentation- 
        # Started with a full algorithm I wronte and claude /learn helped by catching an infinite loop tied to the nesting of try/except logic, as well as a double negative in my main() logic (i should have stuck with whether or not something became a palindrome vs is a lychrel number because I ended up flipping true/false backwards at the end), and an error in my skip logic (I was not originally appending anything if we hit "skip" which meant numbers went untracked). I fixed these and got to 259. 

        # after getting very close (finding answer of 259) Claude /learn helped me realize that I couldn't use the tempL.append(v_rev) lines to append v_rev. I have commented them out here for history's sake to retain my original thought process.
        # Appending v_rev assumes v_rev’s next sum equals v’s next sum. That fails when v has trailing zeros.
        # Same sum example: 
            # v = 123 v_rev = 321
                # 123 + 321 = 444 (from v)
                # 321 + 123 = 444 (from v_rev)
                # since they come to the same sum their chains will be identical further on. 
        # If there is a trailing zero (v = 6940, v_rev = 496) we can't now 'recreate' v because we've lost that 0. 
            # if v = 496 v_rev = 694
            # we can never get back to the 6940 value now.
        # Example failure: for v = 6940 v_rev = 0496
            # 6940 + 0496 = 7436
            # 7436 + 6347 = 13783
            # etc.
                # assume we continue this. We'll find that in 50 iterations 6940 is lychrel: 6940 + reverse never produces a palindrome. 
            # If we append v_rev we add 496 to tempL
            # However 496 has its own chain:
                # 496 + 694 = 1190
                # 1190 + 0911 = 2101
                # 2101 + 1012 = 3113 PALINDROME!!!
                # By appending v_rev to tempL we marked 496 as a lychrel and never returned to fix it and see that 496 in fact is not a lychrel and quickly produces a palindrome.
        # appending v_rev as I was doing throws the final answer by ~10.  
    
    # turn n into a str, flip it (reverse it), and then turn back into an int and then add n_rev to n.
    non_lychrel_flag = False # will turn to true if we form a palindrome.
    counter = 0
    v = n
    tempL = []
    while non_lychrel_flag == False and counter < 50:
        # turn n into a str, flip it (reverse it), and then turn back into an int and then add n_rev to n.
        v_rev = int(str(v)[::-1])
        new_sum = v + v_rev
        try:
            if masterL[new_sum] == True:
                # this means we've already found that new_sum is NOT a Lychrel number (either is a palindrome or was in a chain that formed a palindrome) somewhere else
                # Still must make sure v gets added into the non_lychrel list correctly for future iterations. 
                tempL.append(v)
                return "skip", tempL
            elif is_palindrome(new_sum):
                tempL.append(v)
                # tempL.append(v_rev) # WRONG
                non_lychrel_flag = True
                return False, tempL # is_lychrel --> false because we formed a palindrome.
            else:
                tempL.append(v)
                # tempL.append(v_rev) # WRONG
                v = new_sum
            
        except IndexError:

            if is_palindrome(new_sum):
                tempL.append(v)
                # tempL.append(v_rev) # WRONG
                non_lychrel_flag = True
                return False, tempL # is_lychrel --> false because we formed a palindrome.
            else:
                tempL.append(v)
                v = new_sum
        counter += 1


    if non_lychrel_flag == False: # we never flipped the flag bc we never made a palindrome. The original value here (n) is a Lychrel number. We 
        return True, tempL
       
def main():
    
    # True in this list means that the value at that index is not a lychrel (eventually turns into a palindrome). False in this list means that the value at that index is a lychrel. 0 in this list means that it hasn't been checked yet.
    # If the value is False we have to check it. 
    non_lychrel = longL(10000 + 1) 

    value = 0
    while value < 10_000:
        if non_lychrel[value] == False or non_lychrel[value] == "cat":
            stem, iterated_values = is_lychrel(value, non_lychrel)
            # stem is going to return True or False or "skip", to say whether value is lychrel or not.
            # iterated_values is all the numbers we touched enroute to stem. If stem is True we can now turn all these values' indecises in non_lychrel to True as well.

            if stem == True:
                # turn all iterated values in non_lychrel to False.
                for i in iterated_values:
                    if i < 10_000:
                        non_lychrel[i] = False
            elif stem == False or stem == "skip": 
                # Turn all iterated values in non_lychrel to True
                for i in iterated_values:
                    if i < 10000:
                        non_lychrel[i] = True
            value += 1
        else:
            value += 1 

    print(non_lychrel.count(False))

main()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")