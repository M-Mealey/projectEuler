"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Given a and b for a pythagorean triplet, calculates c (1000-a-b) and checks if
a^2 + b^2 = c^2. Returns True or False
"""
def test_triplet(a, b):
    c = 1000 - a - b
    if c>b and a**2 + b**2 == c**2:
        return True
    else:
        return False

"""
Given a for a pythagorean triplet, iterate over the possible values of b to
find one that solves the problem. Returns 0 if no valid b is found
"""
def test_a(a):
    for b in range(a+1, 1000-a):
        if test_triplet(a,b):
            return b
    return 0

def solve():
    for a in range(1, 1000):
        b = test_a(a)
        if b:
            return a*b*(1000-a-b)


def euler_problem_9():
    print(solve())

if __name__ == "__main__":
    euler_problem_9()