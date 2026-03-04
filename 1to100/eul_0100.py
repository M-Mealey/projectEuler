"""
Project Euler Problem 100
=========================

If a box contains twenty-one coloured discs, composed of fifteen blue
discs and six red discs, and two discs were taken at random, it can be
seen that the probability of taking two blue discs, P(BB) = (15/21) *
(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking
two blue discs at random, is a box containing eighty-five blue discs and
thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
discs in total, determine the number of blue discs that the box would
contain.
"""
import math


t_min = 1000000000000
# solve with pell equations
c,d =5,7
t = (2 + math.sqrt(8*c*c - 4))//4
while t<t_min:
    c,d = 2*d + 3*c, 3*d + 4*c
    t = (2 + math.sqrt(8 * c * c - 4)) // 4
b = (1+math.sqrt(1+2*t*t-2*t))//2

def euler_problem_100():
    print(int(b))

if __name__ == "__main__":
    euler_problem_100()