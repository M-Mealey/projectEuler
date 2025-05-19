"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import math

# copied from problem 3 solution, checks if x is prime
def is_prime(x):
    result = True
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            result = False
            break
    return result


def find_prime(x):
    i = 0
    num = 1
    while i<x:
        i += 1
        num += 1
        while not is_prime(num):
            num += 1
    return num

print(find_prime(10001))

