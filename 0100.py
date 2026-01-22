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

def is_square(x):
    rt = math.isqrt(x)
    return rt*rt == x



tol = 0
y_min = 1000000000000
#y_min = 1070379110497
i = 1414213562372
for y0 in range(100000000000):
    if y0 % 1000000 == 0:
        print(y0/100000000000)
    y = y_min + y0
    z = (y * (y-1))//2
    discriminant = 1 + 4*z
    # @TODO: try values of discriminant or something? idk this is too slow
    while i*i < discriminant:
        i += 1
    if i*i == discriminant:
    #if is_square(discriminant):
        x = int((1+math.isqrt(discriminant))/2)
        #print(f"x={x}, y={y}")
        num = x * (x-1)
        den = y * (y-1)
        print(num/den)
        if abs(num/den - 0.5) <= tol:
            print("sol?")
            print(x)



# solution: x=756872327473
# y = 1070379110497