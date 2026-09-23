"""
Project Euler Problem 117
=========================

Using a combination of black square tiles and oblong tiles chosen from:
red tiles measuring two units, green tiles measuring three units, and blue
tiles measuring four units, it is possible to tile a row measuring five
units in length in exactly fifteen different ways.

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+
                      +----+  +----+  +----+

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to problem 116.
"""


def solve():
    """ solve problem 117 """

    def ways(max_n):
        ways = {}
        ways[0] = 1
        ways[1] = 1
        ways[2] = 2
        ways[3] = 4
        n = 4
        while n < max_n + 1:
            ways_for_n = ways[n - 1] + ways[n - 2] + ways[n - 3] + ways[n-4]

            ways[n] = ways_for_n
            n += 1
        return ways[max_n]

    return ways(50)



if __name__ == "__main__":
    print(solve())
