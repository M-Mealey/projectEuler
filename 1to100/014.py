"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

MAX_N = 1000000
MAX_MEM = 4000000
list = [0] * MAX_MEM
list[1] = 1

"update the list with x and its path length, then check for paths leading to x and update their path lengths"
def update_list(x,p):
    if x==1:
        return
    while x<MAX_MEM:
        list[x] = p
        if x%2==0 and (x-1)%3 == 0: # the 3n thi
            update_list(int((x-1)/3), p+1)
        x *= 2
        p += 1

"compute length of path starting at n"
def comp(n):
    if n<MAX_MEM and list[n]:
        return list[n]
    elif n%2==0:
        path_len = comp(int(n/2)) + 1
        update_list(n, path_len)
        return path_len
    else:
        path_len = comp(3*n+1) + 1
        update_list(n, path_len)
        return path_len

for n in range(2,MAX_N):
    comp(n)


def euler_problem_14():
    max_chain = max(list[:MAX_N])
    print(list.index(max_chain))


if __name__ == "__main__":
    euler_problem_14()