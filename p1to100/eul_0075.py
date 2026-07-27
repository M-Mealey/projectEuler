"""
Project Euler Problem 75
========================

It turns out that 12 cm is the smallest length of wire can be bent to form
a right angle triangle in exactly one way, but there are many more
examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form a
right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three
different right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L 2,000,000
can exactly one right angle triangle be formed?
"""
import math
# solve using Euclid's formula for generating Pythagorean triples,
# via https://en.wikipedia.org/wiki/Pythagorean_triple


def solve():
    """ solve problem 75 """
    solutions_found = {}
    for m in range(1, math.ceil(math.sqrt(2000000))):
        for n in range(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            p = a + b + c
            if p < 1500000 and a ** 2 + b ** 2 == c ** 2:
                for k in range(1, math.ceil(1500000 / p)):
                    solution_set = solutions_found.get(p * k, set())
                    solution_tuple = (min(k * a, k * b), max(k * a, k * b))
                    solution_set.add(solution_tuple)
                    solutions_found[p * k] = solution_set
    total = 0
    for k, v in solutions_found.items():
        if len(v) == 1:
            total += 1
    return total


if __name__ == "__main__":
    print(solve())
