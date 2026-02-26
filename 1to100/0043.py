"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools
import math

# for a given permutations of the digits 0-9, given as a tuple, check if substring
# divisibilities above are true. Return True or False


def substrings_divisible(perm):
    if perm[3] % 2 != 0:
        return False
    if (perm[2]+perm[3]+perm[4]) % 3 != 0:
        return False
    if perm[5] != 5 and perm[5] != 0:
        return False
    if (perm[4] * 100 + perm[5] * 10 + perm[6]) % 7 != 0:
        return False
    if (perm[5] * 100 + perm[6] * 10 + perm[7]) % 11 != 0:
        return False
    if (perm[6] * 100 + perm[7] * 10 + perm[8]) % 13 != 0:
        return False
    if (perm[7] * 100 + perm[8] * 10 + perm[9]) % 17 != 0:
        return False
    return True


total = 0
perms = itertools.permutations(range(0, 10))
for p in perms:
    if substrings_divisible(p):
        x = sum(list(k * (10**(10-p.index(k)-1)) for k in p))
        total += x


def euler_problem_43():
    print(total)


if __name__ == "__main__":
    euler_problem_43()
