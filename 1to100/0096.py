"""
Project Euler Problem 96
========================

Su Doku (Japanese meaning number place) is the name given to a popular
puzzle concept. Its origin is unclear, but credit must be attributed to
Leonhard Euler who invented a similar, and much more difficult, puzzle
idea called Latin Squares. The objective of Su Doku puzzles, however, is
to replace the blanks (or zeros) in a 9 by 9 grid in such that each row,
column, and 3 by 3 box contains each of the digits 1 to 9. Below is an
example of a typical starting puzzle grid and its solution grid.

       +-----------------------+         +-----------------------+
       | 0 0 3 | 0 2 0 | 6 0 0 |         | 4 8 3 | 9 2 1 | 6 5 7 |
       | 9 0 0 | 3 0 5 | 0 0 1 |         | 9 6 7 | 3 4 5 | 8 2 1 |
       | 0 0 1 | 8 0 6 | 4 0 0 |         | 2 5 1 | 8 7 6 | 4 9 3 |
       |-------+-------+-------|         |-------+-------+-------|
       | 0 0 8 | 1 0 2 | 9 0 0 |         | 5 4 8 | 1 3 2 | 9 7 6 |
       | 7 0 0 | 0 0 0 | 0 0 8 |         | 7 2 9 | 5 6 4 | 1 3 8 |
       | 0 0 6 | 7 0 8 | 2 0 0 |         | 1 3 6 | 7 9 8 | 2 4 5 |
       |-------+-------+-------|         |-------+-------+-------|
       | 0 0 2 | 6 0 9 | 5 0 0 |         | 3 7 2 | 6 8 9 | 5 1 4 |
       | 8 0 0 | 2 0 3 | 0 0 9 |         | 8 1 4 | 2 5 3 | 7 6 9 |
       | 0 0 5 | 0 1 0 | 3 0 0 |         | 6 9 5 | 4 1 7 | 3 8 2 |
       +-----------------------+         +-----------------------+

A well constructed Su Doku puzzle has a unique solution and can be solved
by logic, although it may be necessary to employ "guess and test" methods
in order to eliminate options (there is much contested opinion over this).
The complexity of the search determines the difficulty of the puzzle; the
example above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file sudoku.txt contains fifty different Su Doku puzzles ranging
in difficulty, but all with unique solutions (the first puzzle in the file is
the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in
the top left corner of each solution grid; for example, 483 is the 3-digit
number found in the top left corner of the solution grid above.
"""

with open("resources/sudoku.txt") as f:
    data = f.read().split()

grids = []
# each grid is 11 rows, 2 with title and 9 with numbers
for g in range(len(data)//11):
    grid = data[11*g+2:11*g+11]
    grids.append(grid)


# most basic way to solve is by trying numbers and backtracking when a conflict arises
# feels inefficient but the puzzle is only 9x9

# returns coordinates of next zero in grid, two ints: row, column. zero-indexed
# returns -1, -1 if none found
def next_zero(gr):
    for r in range(len(gr)):
        if '0' in gr[r]:
            c = gr[r].index('0')
            return r, c
    return -1, -1

# recursive function, try to solve given grid by
# 1) finding next empty square (read left to right, top to bottom)
# 1.5) optional step for efficiency: check rest of row/column/square for which numbers are used, make list of candidates
# 2) copy grid, insert candidate, call self with new copy
#    if no candidates, return None (backtrack)
def try_solve(gr):
    r, c = next_zero(gr)
    if r==-1 or c==-1: # no zeros, grid is complete
        return gr
    # get possible candidates
    used_nums = set()
    for i in range(9):
        used_nums.add(gr[r][i])
        used_nums.add(gr[i][c])
        bbox_row = r - r%3 # row and column of top left corner of 3x3 box containing this square
        bbox_col = c - c%3
        used_nums.add(gr[bbox_row + i//3][bbox_col + i%3])
    candidates = {'1','2','3','4','5','6','7','8','9'} - used_nums
    # now try each candidate
    for cand in candidates:
        new_gr = gr.copy()
        new_gr[r] = gr[r][:c] + cand + gr[r][c+1:]
        sol = try_solve(new_gr)
        if sol:
            return sol
    return None

total = 0
for g in grids:
    g_solved = try_solve(g)
    total += int(g_solved[0][:3])
print(total)