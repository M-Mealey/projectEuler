"""
Project Euler Problem 73
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d 12,000?
"""
import math


# from problem 33
# Find GCD of 2 integers using Euclidean algorithm
def gcd(n1, n2):
    a, b = max(n1, n2), min(n1, n2)
    r = a%b
    while r!=0:
        a, b = b, r
        r = a%b
    return b


total = 3
for d in range(9,12001):
    min_num = math.ceil(d/3.0)
    max_num = math.floor(d/2.0)
    total += len([x for x in range(min_num, max_num+1) if gcd(x,d)==1])

def euler_problem_73():
    print(int(total))

if __name__ == "__main__":
    euler_problem_73()