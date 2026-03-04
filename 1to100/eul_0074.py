"""
Project Euler Problem 74
========================

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 363601 1454 169
871 45361 871
872 45362 872

It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop. For example,

69 363600 1454 169 363601 ( 1454)
78 45360 871 45361 ( 871)
540 145 ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?
"""
import math


def digit_factorial_sum(x):
    return sum([math.factorial(int(c)) for c in str(x)])


total = 0
for x in range(2, 1000000):
    seen = set()
    seen.add(x)
    next = digit_factorial_sum(x)
    while next not in seen and len(seen) < 60:
        seen.add(next)
        next = digit_factorial_sum(next)
    if len(seen) == 60 and next in seen:
        total += 1


def euler_problem_74():
    print(total)


if __name__ == "__main__":
    euler_problem_74()
