"""
Project Euler Problem 104
=========================

The Fibonacci sequence is defined by the recurrence relation:

  F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

It turns out that F[541], which contains 113 digits, is the first
Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order). And
F[2749], which contains 575 digits, is the first Fibonacci number for
which the first nine digits are 1-9 pandigital.

Given that F[k] is the first Fibonacci number for which the first nine
digits AND the last nine digits are 1-9 pandigital, find k.
"""
import math

max_k = 1000000000


def last_9_pandigital(x):
    last_9_str = str(x)[-9:]
    if set([int(ch) for ch in last_9_str]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return True
    return False

def first_9_pandigital(x):
    first_9_str = str(x)[:9]
    if set([int(ch) for ch in first_9_str]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return True
    return False

# get first 10 digits of base**exponent
def get_first_ten_digits_log(base, exponent):
    log_exp = exponent * math.log10(base)
    mantissa = log_exp - math.floor(log_exp)
    return round(10**mantissa * 10**9)

def get_fib_number_binet(n):
    phi = (1+math.sqrt(5))/2
    neg_phi = (1-math.sqrt(5))/2
    phi_n = get_first_ten_digits_log(phi, n)
    neg_phi_n = neg_phi**n
    # phi**n grows very fast, only need first 10 digits
    fib_num = round((get_first_ten_digits_log(phi, n) - neg_phi**n)/math.sqrt(5))
    return fib_num

k=50
fib_k = 12586269025 % 10**9
fib_k_old = 7778742049 % 10**9

while k<max_k:
    k += 1
    fib_k, fib_k_old = fib_k + fib_k_old % 10**9, fib_k
    if last_9_pandigital(fib_k):
        fib_num = get_fib_number_binet(k)
        if first_9_pandigital(fib_num):
            print(k)
            break

