"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

"""
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


amicable_numbers = []
for i in range(10000):
    divisor_sum = sum(find_divisors(i))
    if divisor_sum != i and sum(find_divisors(divisor_sum)) == i:
        amicable_numbers.append(i)

print(sum(amicable_numbers))

