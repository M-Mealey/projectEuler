"""
Project Euler Problem 68
========================

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each solution
can be described uniquely. For example, the above solution can be
described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11,
and 12. There are eight solutions in total.

        Total          Solution Set
        9              4,2,3; 5,3,1; 6,1,2
        9              4,3,2; 6,2,1; 5,1,3
        10             2,3,5; 4,5,1; 6,1,3
        10             2,5,3; 6,3,1; 4,1,5
        11             1,4,6; 3,6,2; 5,2,4
        11             1,6,4; 5,4,2; 3,2,6
        12             1,5,6; 2,6,4; 3,4,5
        12             1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible
to form 16- and 17-digit strings. What is the maximum 16-digit string for
a "magic" 5-gon ring?
"""
import itertools
# given 5 for inside ring and 5 for outside, find way to determine if magic ring is possible?
#
digits = [x for x in range(1,11)]
inner_rings = itertools.permutations(digits, 5)

# test each possible ring?
# @TODO: in order to get a 16-digit answer, 10 must be in the outer ring
solution_max = 0
for r in inner_rings:
    outer_ring = [x for x in digits if x not in r]
    #print(f"inner ring: {r}")
    #print(f"outer ring: {outer_ring}")
    # smallest item in outer ring must pair with largest sum in inner ring
    # if first 2 in inner ring don't make largest sum, skip this one because
    # the orientation is defined by having the smallest number of the outer ring at the "top"
    inner_ring_sums = [r[0]+r[1], r[1]+r[2], r[2]+r[3], r[3]+r[4], r[4]+r[0]]
    if max(inner_ring_sums) != inner_ring_sums[0]:
        continue # this might be super wrong lol
    inner_ring_diffs = [max(inner_ring_sums)-x for x in inner_ring_sums]
    outer_ring_required = [x+min(outer_ring) for x in inner_ring_diffs]
    #print(outer_ring_required)
    if set(outer_ring_required) == set(outer_ring):
        #print("MATCH")
        #print(outer_ring_required)
        #print(r)
        solution = []
        for i in range(5):
            solution.append(str(outer_ring_required[i]))
            solution.append(str(r[i]))
            solution.append(str(r[(i+1)%5]))
        #print(solution)
        solution_str = "".join(solution)
        #print(solution_str)
        if len(solution_str) > 16:
            continue
        solution_max = max(solution_max, int(solution_str))

# correct answer, but inefficient

def euler_problem_68():
    print(solution_max)

if __name__ == "__main__":
    euler_problem_68()
