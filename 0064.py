"""
Project Euler Problem 64
========================

All square roots are periodic when written as continued fractions and can
be written in the form:

N = a[0] +            1
           a[1] +         1
                  a[2] +     1
                         a[3] + ...

For example, let us consider 23:

23 = 4 + 23 -- 4 = 4 +  1  = 4 +  1     1     1 +  23 - 3
                                      23--4          7

If we continue we would get the following expansion:

23 = 4 +          1
         1 +        1
             3 +      1
                 1 +    1
                     8 + ...

The process can be summarised as follows:

a[0] = 4,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[1] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[2] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[3] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7
a[4] = 8,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[5] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[6] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[7] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7

It can be seen that the sequence is repeating. For conciseness, we use the
notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square
roots are:

2=[1;(2)], period=1
3=[1;(1,2)], period=2
5=[2;(4)], period=1
6=[2;(2,4)], period=2
7=[2;(1,1,1,4)], period=4
8=[2;(1,4)], period=2
10=[3;(6)], period=1
11=[3;(3,6)], period=2
12= [3;(2,6)], period=2
13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N 13, have an odd period.

How many continued fractions for N 10000 have an odd period?
"""
from math import sqrt, floor

# n = the original number being square-rooted, a = the integer part being removed from the remainder
# r = the current remainder part represented as list of 2 integers, [r0, r1]
#     remainder corresponding with previous a-value was rationalized as (root(n) + r0) / r1
# This function returns the new remainder fraction by rationalizing 1 / [ ((root(n) + r0) / r1) - a) ]
# new remainder is returned as list of 2 numbers like input r
def rationalize_remainder(n, r, a):
    x, y = r[0], r[1]
    z = y*a - x
    return [z, int((n-z**2)/y)]

# Find a-values for fractional expansion of square root of int n
# returns a list of integers
def get_a_values(n):
    a0 = floor(sqrt(n))
    r = [a0, n-(a0**2)]
    a_values = [a0]
    while len(a_values) < 1000: # condition is just to stop infinite loop, shouldn't be false
        a_next = floor((sqrt(n)+r[0]) /r[1])
        a_values.append(a_next)
        if r[1] == 1: # cycle ends where denominator is 1
            break
        r = rationalize_remainder(n, r, a_next)
    return a_values

# main loop
total = 0
for n in range(2,10001):
    if not sqrt(n) == floor(sqrt(n)) and int(len(get_a_values(n))-1) % 2 == 1:
        total += 1
# answer
print(total)
