"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
import itertools
# if we always write the smaller factor first, then all equations will be in the form
# 2-digit number * 3-digit = 4-digit or 1-d * 4-d = 4-d
# so solutions can be found by iterating from 1 to 99, finding possible other factors,
# then checking the product

pandigital_products = set()
all_digits = [1,2,3,4,5,6,7,8,9]

def int_to_list(x):
    return [int(ch) for ch in str(x)]

for f1 in range(1, 100):
    f1_list = int_to_list(f1)
    # check first factor
    if 0 in f1_list or len(f1_list) != len(set(f1_list)): #if digits are same or 0, skip this iteration
        continue
    # find possible digit permutations for 2nd factor
    remaining_digits = [d for d in all_digits if d not in f1_list]
    if len(f1_list) == 1:
        combo_gen = itertools.permutations(remaining_digits, 4)
    else:
        combo_gen = itertools.permutations(remaining_digits, 3)
    for c in combo_gen:
        f2 = 0
        # find digits that must appear in product
        product_digits = remaining_digits.copy()
        for x in c:
            f2 = (f2 * 10) + x
            product_digits.remove(x)
        # check product
        product = f1 * f2
        product_list = int_to_list(product)
        if len(product_list) != len(set(product_list)) or (len(product_list) != len(product_digits)): # product can't have duplicates
            continue
        diff_list = [x for x in product_digits if x not in product_list]
        if len(diff_list) == 0: #if true, equation f1 * f2 = product is pandigital
            pandigital_products.add(product)

def euler_problem_32():
    print(sum(pandigital_products))

if __name__ == "__main__":
    euler_problem_32()