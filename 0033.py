"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
import itertools
answers = []

for x in range(10, 100):
    tens_digit = x//10
    ones_digit = x%10
    if ones_digit == 0:
        continue # "cancelling" 0s is trivial, tens digit can't be "cancelled" because then numerator would be 0
    for i in range(1,10):
        # if we write x as to, where t is 10s digit and o is ones digit,
        # possible solutions are where to/ti == o/i, to/it == o/i, to/oi == t/i, to/io == t/i
        possible_solutions = [(tens_digit*10 + i, ones_digit), (i*10 + tens_digit,ones_digit), (ones_digit*10 + i, tens_digit), (i*10 + ones_digit, tens_digit)]
        for d in possible_solutions:
            if d[0]<=x:
                continue
            if x/d[0] == d[1]/i:
                answers.append((x,d[0]))

print(answers)

