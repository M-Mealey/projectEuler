"""
Project Euler Problem 114
=========================

A row measuring seven units in length has red blocks with a minimum length
of three units placed on it, such that any two red blocks (which are
allowed to be different lengths) are separated by at least one black
square. There are exactly seventeen ways of doing this.

                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+  +------+
                       +------+  +------+
                       +------+  +------+

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility,
in general it is permitted to mix block sizes. For example, on a row
measuring eight units in length you could use red (3), black (1), and red
(4).
"""


# dynamic programming problem:
# if first square is grey, then number of ways to make 50 is num ways to make 49
# if first square is red, then it's part of red bar followed by a grey
# number of ways is 50 - (len(red bar) + 1)

def solve():
    """ solve problem 114 """
    ways = {0: 1, 1: 1, 2: 1, 3: 2, 4: 4, 5:7, 6:11}
    n = 7
    while n<51:
        ways_for_n = ways[n-1] # first block grey
        ways_for_n += 1 # one big red block
        for r in range(4, n+1): # first block red, len r-1, + next block grey
            ways_for_n += ways[n-r]
        ways[n] = ways_for_n
        n += 1
    return ways[50]

if __name__ == "__main__":
    print(solve())
