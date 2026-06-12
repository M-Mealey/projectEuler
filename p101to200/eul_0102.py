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


def calc_tri_area(a, b, c):
    """ calculate the area of a triangle from points representing vertices
    from: https://www.omnicalculator.com/math/area-triangle-coordinates"""
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return 1/2 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))


def solve(input_files=("resources/triangles.txt",)):
    """ solve problem 102 """
    with open(input_files[0], 'r', encoding='utf-8') as f:
        data = f.read().split()

    triangle_count = 0
    for triangle in data:
        points = [int(x) for x in triangle.split(",")]
        a = (points[0], points[1])
        b = (points[2], points[3])
        c = (points[4], points[5])
        o = (0, 0)
        if (calc_tri_area(a, b, c) == calc_tri_area(a, b, o) + calc_tri_area(a, o, c)
                + calc_tri_area(o, b, c)):
            triangle_count += 1
    return triangle_count


if __name__ == "__main__":
    print(solve())
