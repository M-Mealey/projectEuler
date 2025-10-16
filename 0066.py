"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
from math import sqrt, floor

# simple solution: for each D, iterate over possible values of x until you find one that works
# O(n**2) ish
# x gets too big, iterating forever
max_x, d_index = 9, 5
for d in range(2, 1001):
    if sqrt(d) == floor(sqrt(d)):
        continue # problem assumes no solutions for square D
    for x in range(2, 10001):
        y_squared = (x**2 - 1)/d
        if sqrt(y_squared) == floor(sqrt(y_squared)):
            print(f"x={x}, d={d}, y={sqrt(y_squared)}")
            if x>max_x:
                max_x = x
                d_index = d
            break
print(d_index)

#^ too inefficient, some values of x are very large

# better solution: use continuous fractions
# @TODO tomorrow :)
