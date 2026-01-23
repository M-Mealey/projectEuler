"""
Project Euler Problem 94
========================

It is easily proved that no equilateral triangle exists with integral
length sides and integral area. However, the almost equilateral triangle
5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which
two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of every almost equilateral triangle with
integral side lengths and area and whose perimeters do not exceed one
billion (1,000,000,000).
"""
from math import sqrt, isqrt

# 518408346
# 408855758

# 9973078


# for each side length x, check triangles with two sides x and one x-1, x+1
# get area with heron's formula: A = root(s(s-a)(s-b)(s-c))
# semiperimeter = s = a+b+c/2

max_perimeter = 1000000000
tol = 0.000000001

def calculate_tri_area_from_sides(a, b, c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

# Triangle has sides a,b,c, where a==b, perimeter = 2a + c, semiperimeter = (2a-c)/2
# by heron's formula, Area = sqrt(s(s-a)(s-b)(s-c))
# a==b so A = sqrt(s(s-a)(s-a)(s-c)) = (s-a) * sqrt(s(s-c)), is int if sqrt(s(s-c)) is int
# c must be even

perimeter_sum = 0
for c in range(2,max_perimeter//3+2,2):
    if c%1000000==0:
        print(c)
    for a in (c-1,c+1):
        A_sq = (4*a*a - c*c)//4
        A_rt = isqrt(A_sq)
        if A_rt*A_rt == A_sq:
            perimeter_sum += a+a+c
print(perimeter_sum)

