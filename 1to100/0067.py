"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

with open("resources/triangle.txt") as f:
    pyramid_input = f.read()

# all below is copied from problem 16

# convert string to array of ints
pyramid = [[int(x) for x in row.strip().split()] for row in pyramid_input.strip().splitlines()]

sums = pyramid[0]
# Iterate over rows, tracking the largest sum up to each entry in the pyramid
for r in pyramid[1:]:
    new_sums = []
    for i in range(len(r)):
        if i==0: # first in row, can only be reached from right
            new_sums.append(sums[i] + r[i])
        elif i < len(r)-1: # entry in the middle, pick max of the two points leading there
            new_sums.append(max(sums[i-1] + r[i], sums[i] + r[i]))
        else: # last in row, can only be reached from left
            new_sums.append(sums[i-1] + r[i])
    sums = new_sums
# end with row of sums representing the maximum sum for a path ending at each index in bottom row
# print the largest sum


def euler_problem_67():
    print(max(sums))

if __name__ == "__main__":
    euler_problem_67()

