"""
Project Euler Problem 83
========================

NOTE: This problem is a significantly more challenging version of
   Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in red and
is equal to 2297.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by moving left, right, up,
and down.
"""
import bisect

with open("resources/matrix.txt") as f:
    rows = f.read().strip().split("\n")
    data = [r.split(",") for r in rows]
    data = [[int(x) for x in r] for r in data]

# calculates minimum path from top left corner to each square in an array going only right or down
# inputs: costs, a matrix of costs for each square
#         path, a matrix the same size as costs for minimum path lengths to be written to
def calculate_min_paths(costs, path):
    path_candidates = []
    # first path candidate is starting point
    path_candidates.append((costs[0][0], 0))
    squares_filled = set()
    # note: squares are numbered l to r, top to bottom. eg (0 indexing) row 2, column 5 = 165
    while len(squares_filled) < len(costs) * len(costs[0]) and len(path_candidates) > 0:
        next_path = path_candidates.pop(0)
        cost, square_num, r, c = next_path[0], next_path[1], next_path[1]//80, next_path[1]%80
        if square_num in squares_filled:
            continue
        squares_filled.add(square_num)
        path[r][c] = cost
        if r>0 and square_num-80 not in squares_filled:
            path_up = (cost + costs[r - 1][c], (r-1)*80 + c)
            bisect.insort(path_candidates, path_up)
        if c>0 and square_num-1 not in squares_filled:
            path_left = (cost + costs[r][c-1], r*80 + c-1)
            bisect.insort(path_candidates, path_left)
        if r < len(costs) - 1:
            path_down = (cost + costs[r + 1][c], (r+1)*80 + c)
            bisect.insort(path_candidates, path_down)
        if c < len(costs[r]) - 1:
            path_right = (cost + costs[r][c+1], r*80 + c+1)
            bisect.insort(path_candidates, path_right)


paths = [[0 for _ in range(80)] for __ in range(80)]
calculate_min_paths(data, paths)
print(paths[79][79])

