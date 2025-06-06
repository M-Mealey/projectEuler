"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
import math

"""
Copied from problem 21
Input integer x, returns list of positive integer divisors of x
O(root(x)) time
"""
def find_divisors(x):
    divisors = [1]
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            divisors.append(i)
            if x/i != i:
                divisors.append(int(x/i))
    return divisors

"""
Checks if integer x can be created by adding 2 numbers in iterable l
"""
def can_make_sum(x, l):
    for i in l:
        if x-i in l:
            return True
    return False


abundant_numbers = set([])
number_sum = 0
for i in range(1, 28124):
    divisor_sum = sum(find_divisors(i))
    if divisor_sum > i:
        abundant_numbers.add(i)
    if not can_make_sum(i, abundant_numbers):
        number_sum += i


print(number_sum)



