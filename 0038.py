"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

# for a given int, check if a list "(1,2, ... , n) where n > 1" can be created to satisfy the problem
# Returns the pandigital 9-digit number found, or -1 if none can be created
def check_pandigital(x):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = 0
    pandigital_string = ""
    while len(digits) > 0:
        try:
            n += 1
            product_str = str(n * x)
            pandigital_string += product_str
            for digit in product_str:
                digits.remove(digit)
        except ValueError:
            return -1
    return int(pandigital_string)

# only need to check up to 4-digit numbers because n > 1, so concatenated product of 5-digit (or larger)
# number with (1, 2) would have 10-digits (or more),
solution = max([check_pandigital(i) for i in range(10000)])
print(solution)