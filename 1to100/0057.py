"""
Project Euler Problem 57
========================

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""

# calculates the nth expansion, returns float (not used in solution, but written to help understand concept)


def get_expansion(n):
    total = 2
    for i in range(1, n):
        total = 2 + 1/total
    return 1 + 1/total

# calculates the nth expansion as a fraction. Returns numerator, denominator


def get_expansion_fraction(n):
    num = 2
    denom = 1
    for i in range(1, n):
        num, denom = 2*num + denom, num
    return num + denom, num


count = 0
for n in range(1, 1000):
    fraction = get_expansion_fraction(n)
    if len(str(fraction[0])) > len(str(fraction[1])):
        count += 1


def euler_problem_57():
    print(count)


if __name__ == "__main__":
    euler_problem_57()
