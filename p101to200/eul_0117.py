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

    def ways(max_n, tiles):
        ways = {}
        for l in range(-max(tiles), 0):
            ways[l] = 0
        for l in range(min(tiles)+1):
            ways[l] = 1
        n = min(tiles) + 1
        while n < max_n + 1:
            ways_for_n = 0
            for t in tiles:
                ways_for_n += ways[n-t]

            ways[n] = ways_for_n
            n += 1
        return ways[max_n]

    return ways(50, (1,2,3,4))



if __name__ == "__main__":
    print(solve())
