"""
Project Euler Problem 81
========================

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in red
and is equal to 2427.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
"""
# go row by row, minimal path sum for this square = min(path sum to left, path sum of square above) + square

with open("resources/matrix.txt") as f:
    rows = f.read().strip().split("\n")
    data = [r.split(",") for r in rows]
    data = [[int(x) for x in r] for r in data]

# calculates minimum path from top left corner to each square in an array going only right or down
# inputs: costs, a matrix of costs for each square
#         path, a matrix the same size as costs for minimum path lengths to be written to
def calculate_min_paths(costs, path):
    path[0][0] = data[0][0]
    # first row
    for i in range(1,len(data[0])):
        path[0][i] = data[0][i] + path[0][i-1]
    # other rows
    for r in range(1, len(data)):
        for i in range(len(data[r])):
            if i==0:
                path[r][i] = data[r][i] + path[r-1][i]
            else:
                path[r][i] = data[r][i] + min(path[r-1][i], path[r][i-1])

paths = [[0 for _ in range(80)] for __ in range(80)]
calculate_min_paths(data, paths)
print(paths[79][79])
