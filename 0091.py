"""
Project Euler Problem 91
========================

The points P (x[1], y[1]) and Q (x[2], y[2]) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form DOPQ.

There are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 x[1], y[1], x[2], y[2] 2.

Given that 0 x[1], y[1], x[2], y[2] 50, how many right triangles can be
formed?
"""
import itertools

size = 50
tol = 0.000001 # tolerance
# get all possible points (x,y) where 0 <= x,y <= 50
points = list(itertools.product([x for x in range(size+1)], [y for y in range(size+1)]))
points.remove((0,0))

def points_collinear(x, y, z):
    if x[0] == y[0] or y[0] == z[0] or x[0]==z[0]: # there's an undefined slope here
        return x[0] == y[0] == z[0] # points are collinear if all are undefined
    s0, s1, s2 = (x[1]-y[1])/(x[0]-y[0]), (y[1]-z[1])/(y[0]-z[0]), (x[1]-z[1])/(x[0]-z[0])
    return s0==s1==s2

count = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        p0 = (0,0)
        p1 = points[i]
        p2 = points[j]
        is_right=False
        if points_collinear(p0, p1, p2):
            continue
        if 0 == p1[0] or p1[0] == p2[0] or 0 == p2[0]: # there's an undefined slope
            # reassign points to a0, a1, a2 so that undefined slope is between a0 and a1
            a0, a1, a2 = p0, p1, p2
            if p1[0] == p2[0]:
                a0, a1, a2 = p1, p2, p0
            elif p0[0] == p2[0]:
                a0, a1, a2 = p0, p2, p1
            # now look for zero slope between a2 and other points OR line a0a2 perpendicular to line a1a2
            if a2[1] == a0[1] or a2[1] == a1[1]: #This is a right triangle?
                count += 1
            else:
                s1 = (a2[1]-a0[1])/(a2[0] - a0[0])
                s2 = (a2[1]-a1[1])/(a2[0] - a1[0])
                if s1 * s2 == -1:
                    count += 1
        else:
            s0, s1, s2 = (p0[1] - p1[1]) / (p0[0] - p1[0]), (p1[1] - p2[1]) / (p1[0] - p2[0]), (p0[1] - p2[1]) / (p0[0] - p2[0])
            if -1-tol <= s0 * s1 <= -1+tol or -1-tol<=s1*s2 <= -1+tol or -1-tol <= s0 * s2 <= -1+tol:
                count += 1

print(count)


