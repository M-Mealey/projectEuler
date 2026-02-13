"""
Project Euler Problem 85
========================

By counting carefully it can be seen that a rectangular grid measuring 3
by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest solution.
"""

# To find number of rectanges in one square:
# iterate over different sized rectangles
# find # of 1x1 rectangles, then 1x2, 1x3, ... up to macimum width
# then increase height and iterate again: 2x1, 2x2, 2x3, etc... 3x1, 3x2, 3x3, 3x4 ...
# maybe this can be improved with recursion or a formula?

def find_rectangles(l, w):
    total = 0 #
    for l0 in range(1, l+1):
        for w0 in range(1, w+1):
            total += (l+1-l0) * (w+1-w0)
    return total


closest_rectangle_count = 0
best_solution = [0, 0]
for x in range(1, 100):
    for y in range(1, x+1):
        rec_count = find_rectangles(x,y)
        if abs(closest_rectangle_count - 2000000) > abs(rec_count - 2000000):
            closest_rectangle_count = rec_count
            best_solution = [x,y]

def euler_problem_85():
    print(best_solution[0] * best_solution[1])

if __name__ == "__main__":
    euler_problem_85()
