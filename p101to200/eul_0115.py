"""
Project Euler Problem 115
=========================

NOTE: This is a more difficult version of problem 114.

A row measuring n units in length has red blocks with a minimum length of
m units placed on it, such that any two red blocks (which are allowed to
be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a
row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for
which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711
and F(10, 57) = 1148904, so n = 57 is the least value for which the
fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function
first exceeds one million.
"""



def solve():
    """ solve problem 115 """
    m = 50
    ways = {}
    for i in range(m):
        ways[i] = 1
    ways[m] = 2
    ways[m+1] = 4
    n = m + 2
    while n<100000000:
        ways_for_n = ways[n-1] # first block grey
        ways_for_n += 1 # one big red block
        for r in range(m+1, n+1): # first block red, len r-1, + next block grey
            ways_for_n += ways[n-r]
        ways[n] = ways_for_n
        if ways_for_n > 1000000:
            break
        n += 1
    return n

if __name__ == "__main__":
    print(solve())
