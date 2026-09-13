# Hamm 1 SEP 26
import time

# Start the timer
start_time = time.perf_counter()


# copied text straight from the problem and added the "," and [] manually. probably a way to do that programmatically but eh. 
# also must get rid of all leading zeros by hand. 
triangle = [
    [75], 
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
    ]


# for test purposes
# triangle = [
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
# ]
# answer should be 23


# Made some changes after the fact in the functions folder to assist with 67. Caught 2 bugs.
# Of note- pulling this from functions.py takes the total time to execute and 10x or more.  

from functions import triangle_problems

# Original 18 code. 
# Takes a triangle and finds the max total from top to bottom. Used in 18. Likely reqd in 67.
# def triangle_problems(triangle):
#     for row in range(len(triangle) - 2, -1, -1): # start at second row from the bottom. Not sure why it's (-2) but it works. End at 0, but bc the range is exclusive you actually have to tell it to end at -1. increm by -1.
#         collapse_row = []
#         psn = 0
#         for item in triangle[row]:
#             # try:
#             collapse_item_1 = item + triangle[row + 1][psn] # add item with the value immediately below it.
#             collapse_item_2 = item + triangle[row + 1][psn + 1] # add item with the value below and 1 spot to the right. 
#             # except IndexError:
#             #     pass # handles when we get to the end of a row and get indexerror cleanly.
#             collapse_row.append(max(collapse_item_1, collapse_item_2))
#             psn += 1 # increm psn counter to move one more spot in that list.
#         triangle[row] = collapse_row # replace the original row with my collapsed version. 
#     print(triangle[row]) # After all iterations triangle[row] is the top-most collapsed row, and the answer to the question. 
# for test purposes
# triangle = [
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
# ]
# answer should be 23

# test:
# triangle_problems()
        
print(triangle_problems(triangle))

""" A Thought
Need to collapse this triangle onto itself. So start at the 2nd to last row. Look at each value in that row and see what value below it would make it larger.
Then collapse the bottom row into that row, and move up to the next row. Collapse that row into the next row. Work your way up. Eventually you get to that last number and you have your answer!
"""
# End the timer
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Program took {execution_time:.6f} seconds to run.")
