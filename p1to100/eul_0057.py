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


def get_expansion(n):
    """ calculates the nth expansion, returns float
    (not used in solution, but written to help understand concept) """
    total = 2
    for _ in range(1, n):
        total = 2 + 1/total
    return 1 + 1/total


def get_expansion_fraction(n):
    """ calculates the nth expansion as a fraction. Returns numerator, denominator """
    num = 2
    denom = 1
    for _ in range(1, n):
        num, denom = 2*num + denom, num
    return num + denom, num


def solve():
    """ solve problem 57 """
    count = 0
    for n in range(1, 1000):
        fraction = get_expansion_fraction(n)
        if len(str(fraction[0])) > len(str(fraction[1])):
            count += 1
    return count


if __name__ == "__main__":
    print(solve())
