"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
import itertools
from local_helpers import is_prime

def tuple_to_int(tup):
    total = 0
    for d in tup:
        total = total * 10
        total += d
    return total

# get all combinations of 4 digits
digits = [0,1,2,3,4,5,6,7,8,9]
combos = list(itertools.combinations_with_replacement(digits, 4))
combos.remove((1,4,7,8)) # remove solution we already know

def euler_problem_49():
    for c in combos:
        # get all prime numbers 4-digit numbers that can be made from these digits
        numbers = set(filter(lambda x: x > 1000 and is_prime(x), [tuple_to_int(p) for p in itertools.permutations(c)]))
        # take one from set, get difference between each other element of set, and check for 3rd in arithmetic sequence
        while len(numbers) > 2:
            next_num = numbers.pop()
            for n in numbers:
                g, l = max(next_num, n), min(next_num, n)
                diff = g - l
                if g + diff in numbers:
                    print(str(l) + str(g) + str(g + diff))
                if l - diff in numbers:
                    print(str(l - diff) + str(l) + str(g))

if __name__ == "__main__":
    euler_problem_49()