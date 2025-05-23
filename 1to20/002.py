"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

"""
Finds sum of all even-valued fibonacci terms that don't exceed x
"""
def fib_sum_even(x):
    f0 = 1
    f1 = 2
    sum = 0
    while f1 < x:
        next = f1 + f0
        if f1 % 2 == 0:
            sum += f1
        f0 = f1
        f1 = next
    return sum

print(fib_sum_even(4000000))

