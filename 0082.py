"""
Project Euler Problem 82
========================

   NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell
in the left column and finishing in any cell in the right column, and only
moving up, down, and right, is indicated in red; the sum is equal to 994.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the left column to the right column.
"""
import bisect

# shortest path to any square in left column = square itself
# for each of the next column, create queue of path lengths, fill with path from left to each square
#     the pop shortest path, add to shortest path matrix, add paths to each neighbor above/below,
#     repeat until every square filled in column

with open("resources/matrix_82.txt") as f:
    rows = f.read().strip().split("\n")
    data = [r.split(",") for r in rows]
    data = [[int(x) for x in r] for r in data]

# calculates minimum path from top left corner to each square in an array going only right or down
# inputs: costs, a matrix of costs for each square
#         path, a matrix the same size as costs for minimum path lengths to be written to
def calculate_min_paths(costs, path):
    # first column
    for r in range(len(costs)):
        path[r][0] = costs[r][0]
    # other columns
    for c in range(1, len(costs[0])):
        path_candidates = []
        for r in range(len(costs)):
            path_len = path[r][c-1] + costs[r][c]
            path_candidates.append((path_len, r))
        path_candidates.sort()
        squares_filled = set()
        while len(squares_filled) < len(costs) and len(path_candidates) > 0:
            next_path = path_candidates.pop(0)
            cost, row = next_path[0], next_path[1]
            if row in squares_filled:
                continue
            path[row][c] = cost
            squares_filled.add(row)
            if row > 0: # add path to square above to candidates
                path_up = (cost + costs[row-1][c], row-1)
                bisect.insort(path_candidates, path_up)
            if row < len(costs) - 1: # add path to square below to candidates
                path_down = (cost + costs[row + 1][c], row + 1)
                bisect.insort(path_candidates, path_down)


paths = [[0 for _ in range(80)] for __ in range(80)]
calculate_min_paths(data, paths)
min_path = min([r[79] for r in paths])
print(min_path)



