"""
Project Euler Problem 90
========================

Each of the six faces on a cube has a different digit (0 to 9) written on
it; the same is done to a second cube. By placing the two cubes
side-by-side in different positions we can form a variety of 2-digit
numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to
display all of the square numbers below one-hundred: 01, 04, 09, 16, 25,
36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9}
on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned
upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3,
4, 6, 7} allows for all nine square numbers to be displayed; otherwise it
would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on
each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets
in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the
square numbers to be displayed?
"""
import itertools

# 2 dice, d0 and d1
# d0 is whichever has the lower first digit. if tied, then go to second digit, etc. if both dice are
# equivalent, then which is d0 is arbitrary

# a die is represented by a sorted tuple

# all digits except 7 must appear at least once
# each face has different digit, so a digit can appear twice at most
# so for all valid configurations, 3 digits appear twice, 6 appear once

# start with case where only one 0 appears? die with 0 is d0
# (1, x, x, x, x, x) + (x, x, x, x, x, x)

# checks if dieA is lower than dieB
# returns boolean, on tie returns True
def is_lower_die(dieA, dieB, index=0):
    if index > 5: #tie
        return True
    if dieA[index] != dieB[index]:
        return dieA[index] < dieB[index]
    else:
        return is_lower_die(dieA, dieB, index+1)

# adds a pair of dice to the set
def add_dice_pair_to_set(dieA, dieB, the_set):
    #determine which is d0, d1
    d0, d1 = dieA, dieB
    if is_lower_die(dieB, dieA):
        d0, d1 = dieB, dieA
    the_set.add(tuple(d0 + d1))

# checks if dice are valid and can create all squares
def check_dice(d0, d1):
    squares = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]
    if len(d0) != 6 or len(d1) != 6:
        print(f"ERR: dice wrong size ({d0}, {d1}")
        return False
    d0_numbers = list(d0)
    if 6 in d0:
        d0_numbers.append(9)
    if 9 in d0:
        d0_numbers.append(6)
    d1_numbers = list(d1)
    if 6 in d1:
        d1_numbers.append(9)
    if 9 in d1:
        d1_numbers.append(6)
    for sq in squares:
        if (sq[0] not in d0_numbers or sq[1] not in d1_numbers) and (sq[1] not in d0_numbers or sq[0] not in d1_numbers):
            return False
    return True


def simple_build_dice():
    dice_pairs = set()
    available_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_dice_0 = list(itertools.combinations(available_digits, 6))
    possible_dice_1 = list(itertools.combinations(available_digits, 6))
    for d0 in possible_dice_0:
        for d1 in possible_dice_1:
            if check_dice(d0, d1):
                add_dice_pair_to_set(d0, d1, dice_pairs)
    print(len(dice_pairs))

simple_build_dice()
