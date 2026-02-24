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
import time
import sys

MAX_N = 1000000
MAX_MEM = 4000000


def update_list(x, p, ls):
    """update the list with x and its path length, then check for paths leading to x and update their path lengths"""
    if x == 1:
        return
    while x < MAX_MEM:
        ls[x] = p
        if x % 2 == 0 and (x-1) % 3 == 0:  # the 3n thi
            update_list(int((x-1)/3), p+1, ls)
        x *= 2
        p += 1


def comp(n, ls):
    """compute length of path starting at n"""
    if n < MAX_MEM and ls[n]:
        return ls[n]
    elif n % 2 == 0:
        path_len = comp(int(n/2), ls) + 1
        update_list(n, path_len, ls)
        return path_len
    else:
        path_len = comp(3*n+1, ls) + 1
        update_list(n, path_len, ls)
        return path_len

def dict_comp(n, d):
    if n in d:
        return d[n]
    if n%2 == 0:
        path_len = dict_comp(n//2, d) + 1
        d[n] = path_len
        return path_len
    else:
        path_len = dict_comp(3*n + 1, d) + 1
        d[n] = path_len
        return path_len

def solve_with_list():
    seq_len_list = [0] * MAX_MEM
    seq_len_list[1] = 1
    for n in range(2, MAX_N):
        comp(n, seq_len_list)
    max_chain = max(seq_len_list[:MAX_N])
    return seq_len_list.index(max_chain)


def solve_with_dict():
    seq_dict = {}
    seq_dict[1] = 1
    for n in range(2, MAX_N):
        if n not in seq_dict:
            dict_comp(n, seq_dict)
    highest_value = (1,1)
    for x in seq_dict:
        if seq_dict[x] > highest_value[1]:
            highest_value = (x, seq_dict[x])
    return highest_value[0]


def euler_problem_14(timers=False):
    start_time = time.perf_counter()
    dict_result = solve_with_dict()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if timers:
        print(f"dict solve took {elapsed_time} seconds")
    print(dict_result)

    start_time = time.perf_counter()
    list_result = solve_with_list()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if timers:
        print(f"list solve took {elapsed_time} seconds")
        print(list_result)




if __name__ == "__main__":
    print_times = False
    euler_problem_14(print_times)
