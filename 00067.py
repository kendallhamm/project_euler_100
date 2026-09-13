# Hamm 1 SEP 26
import time

# Start the timer
start_time = time.perf_counter()

from functions import triangle_problems

# Used Google Gemini to help with automating building the list of lists, then just reused func from 18.py
# Could have manually gone in and added the commas, removed leading zeros, and added []'s but that seemed like a poor use of time. 

# Open and read ('r') the text file
with open('67.txt', 'r') as file:
    lines = file.readlines() # readlines lets us build a list of lists, each internal list is a str of that line.

processed_lines = []

for line in lines:
    # Convert each number string to an integer (removes leading zeros), 
    number_list = [int(num) for num in line.split()]
    processed_lines.append(number_list)
 

# The meat and potatoes
print(triangle_problems(processed_lines))

# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
