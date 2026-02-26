"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

max_solutions = (0, 0)
for p in range(3, 1000):
    solutions = 0
    for a in range(1, p):
        for b in range(a, p-a):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solutions += 1
    if solutions > max_solutions[1]:
        max_solutions = (p, solutions)


def euler_problem_39():
    print(max_solutions[0])


if __name__ == "__main__":
    euler_problem_39()
