"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

# ring 0 is 1x1, ring 1 is 3x3, ring 2 is 5x5, ring 3 is 7x7, etc.
# a 1001 by 1001 grid has 501 "rings" (inc ring 0), ring 500 is 1001x1001
# ring x is (2x+1)x(2x+1), contains 8x numbers
diagonal_sum = 1
end_of_ring = 1 # tracks end of previous ring
for r in range(1,501):
    # each corner is 2r steps up from the last corner, where r is the ring # the corner is in
    diagonal_sum += end_of_ring + 2*r
    diagonal_sum += end_of_ring + 4*r
    diagonal_sum += end_of_ring + 6*r
    diagonal_sum += end_of_ring + 8*r
    end_of_ring = end_of_ring + 8*r

def euler_problem_28():
    print(diagonal_sum)

if __name__ == "__main__":
    euler_problem_28()