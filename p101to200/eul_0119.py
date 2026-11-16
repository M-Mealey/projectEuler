"""
Project Euler Problem 119
=========================

The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a
number with this property is 614656 = 28^4.

We shall define a[n] to be the nth term of this sequence and insist that a
number must contain at least two digits to have a sum.

You are given that a[2] = 512 and a[10] = 614656.

Find a[30].
"""
import math

def solve():
    """ solve problem 119 """
    max_search = 100_000_000_000
    found = set()
    for i in range(2, int(math.sqrt(max_search))):
        c = i * i
        while c < max_search:
            digit_sum = sum(int(digit) for digit in str(c))
            if digit_sum == i:
                found.add(c)
            c *= i
    print(found)
    return -1

if __name__ == "__main__":
    print(solve())
