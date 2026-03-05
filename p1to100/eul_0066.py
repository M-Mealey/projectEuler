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
"""
# simple solution: for each D, iterate over possible values of x until you find one that works
# O(n**2) ish
# x gets too big, iterating forever
max_x, d_index = 9, 5
for d in range(2, 10):
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
"""
# ^ too inefficient, some values of x are very large

# from problem 64


def rationalize_remainder(n, r, a):
    x, y = r[0], r[1]
    z = y*a - x
    return [z, int((n-z**2)/y)]


# from problem 64
def get_a_values(n):
    a0 = floor(sqrt(n))
    r = [a0, n-(a0**2)]
    a_values = [a0]
    while len(a_values) < 1000:  # condition is just to stop infinite loop, shouldn't be false
        a_next = floor((sqrt(n)+r[0]) / r[1])
        a_values.append(a_next)
        if r[1] == 1:  # cycle ends where denominator is 1
            break
        r = rationalize_remainder(n, r, a_next)
    return a_values

# from problem 65


def calculate_convergent(cf_list):
    if len(cf_list) < 1:
        return 0
    cn = cf_list.pop()  # convergent numerator
    cd = 1  # convergent denominator
    while len(cf_list) > 0:
        cn, cd = cd, cn  # 1/current fraction
        cn += cf_list.pop() * cd  # add next coefficient
    return cn, cd

# from problem 33
# Find GCD of 2 integers using Euclidean algorithm


def gcd(n1, n2):
    a, b = max(n1, n2), min(n1, n2)
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


def get_convergent_list(a_v):
    convergents = []
    if len(a_v) % 2 == 0:
        a_v = a_v + a_v[1:-1]
    for i in range(len(a_v)):
        ls = a_v[:i+1]
        convergents.append(calculate_convergent(ls))
    return convergents


# better solution: use continuous fractions
max_x, d_index = 9, 5
for d in range(2, 1000):
    if sqrt(d) == floor(sqrt(d)):
        continue  # problem assumes no solutions for square D
    a_vals = get_a_values(d)
    c_list = get_convergent_list(a_vals)
    for x, y in c_list:
        if x**2 - d*(y**2) == 1 and x > max_x:
            max_x = x
            d_index = d
# @TODO: clean


def euler_problem_66():
    print(d_index)


if __name__ == "__main__":
    euler_problem_66()
