"""
Project Euler Problem 102
=========================

Three distinct points are plotted at random on a Cartesian plane, for
which -1000 x, y 1000, such that a triangle is formed.

Consider the following two triangles:

                  A(-340,495), B(-153,-910), C(835,-947)

                  X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle
XYZ does not.

Using triangles.txt, a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the
interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the
example given above.
"""
import math

with open("resources/triangles.txt") as f:
    data = f.read().split()



# traingle area from points, https://www.omnicalculator.com/math/area-triangle-coordinates
def calc_tri_area(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return 1/2 * abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

triangle_count = 0
for triangle in data:
    points = [int(x) for x in triangle.split(",")]
    A = (points[0], points[1])
    B = (points[2], points[3])
    C = (points[4], points[5])
    O = (0, 0)
    if calc_tri_area(A, B, C) == calc_tri_area(A, B, O) + calc_tri_area(A, O, C) + calc_tri_area(O, B, C):
        triangle_count += 1
print(triangle_count)
