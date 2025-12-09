"""
Project Euler Problem 86
========================

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
and a fly, F, sits in the opposite corner. By travelling on the surfaces
of the room the shortest "straight line" distance from S to F is 10 and
the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given
cuboid and the shortest route is not always integer.

By considering all cuboid rooms up to a maximum size of M by M by M, there
are exactly 2060 cuboids for which the shortest distance is integer when
M=100, and this is the least value of M for which the number of solutions
first exceeds two thousand; the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds
one million.
"""

# shortest path is found by unfolding the cuboid and drawing a straight line from
# the start to the end points. There are 3 potential end points.
#
#            +----------f <- end
#           /          /|
#          /          / |
#       + +----------+  |
#       | |          |  |
#       | |          |  + -/
#     z | |          | /  /
#       | |          |/  / y
# start-> s----------+ -/
#         \_________/
#              x
#
#
#                                +----x-----f
#                                |          |
#                                y          y
#                                |          |
#                                |          |
#            f----x-----+---y----+----x-----+---y----f
#            |          |        |          |        |
#            |          |        |          |        |
#            z          z        z          z        z
#            |          |        |          |        |
#            |          |        |          |        |
#            +----x-----+---y----s----x-----+---y----+
#                                |          |
#                                y          y
#                                |          |
#                                |          |
#                                +----x-----+
#
# path 1: s to top left f
# d = root( (x+y)**2 + z**2)
# path 2: s to top center f
# d = root( x**2 + (y+z)**2 )
# path 3: s to top right f
# d = root( (x+y)**2 + z**2 ), same as path 1
#
#
import math

def find_shortest_cuboid_path(x,y,z):
    path1 = math.sqrt((x+y)**2 + z**2)
    path2 = math.sqrt(x**2 + (y+z)**2)
    return min(path1, path2)


M = 10
int_lengths = 0
for x in range(1,M+1):
    for y in range(1,x+1):
        for z in range(1,y+1):
            path = find_shortest_cuboid_path(x,y,z)
            if path == math.floor(path):
                int_lengths += 1
#print(int_lengths)

# does restriction to x>=y>=z mean that the shortest path will always be (path2) d = root( x**2 + (y+z)**2 )
# probably b/c x is always greatest

# generalize by
solutions = 0
M = 1
max_M = 1000000
while M<max_M:
    for opp in range(1, 2*M): # opp = y + z
        hyp = math.sqrt(M**2 + opp**2)
        if hyp == math.floor(hyp):
            if opp > M+1:
                solutions += (M+M+2-opp)//2
            else: # side M must be the longest (x), opposite side is x+y
                solutions += opp//2
    if solutions > 1000000:
        break
    M += 1

print(M)