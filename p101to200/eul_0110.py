"""
Project Euler Problem 110
=========================

In the following equation x, y, and n are positive integers.

                                1 + 1 = 1
                                x   y   n

It can be verified that when n = 1260 there are 113 distinct solutions and
this is the least value of n for which the total number of distinct
solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions
exceeds four million?

NOTE: This problem is a much more difficult version of problem 108 and
as it is well beyond the limitations of a brute force approach it requires
a clever implementation.
"""
from local_helpers import prime_sieve
import math
import itertools

PRIMES = prime_sieve(100)

def get_number_from_pf_array(arr):
    """ calculate an int from the array representing the powers of its prime factorization """
    return math.prod(p**e for e,p in zip(arr,PRIMES))



def solve():
    """ solve problem 110
    similar to 108, but I need to make it more efficient for this problem
    """
    target_n = 4_000_000
    target_n_sq = 2*target_n
    # start by finding factors if all primes are to first power, this creates an upper bound
    # because if any prime number was used 0 times and there was a bigger prime used x times,
    # then another number could be created by dividing by big prime x times and multiplying
    # by smaller prime x times, and it would have the same number of factors and be smaller
    upper_bound_powers = [2]
    while math.prod(x+1 for x in upper_bound_powers) < target_n_sq:
        upper_bound_powers.append(2)
    upper_bound = get_number_from_pf_array(upper_bound_powers)


    # now we know the maximum number of primes being considered here
    prime_candidates = PRIMES[:len(upper_bound_powers)]
    # get a simple upper bound on what the exponent can be: log(base prime x)upper_bound
    def build_list(primes, num_factors, max_pow, current_n):
        # for each possible power (pp): is current n_sq * primes[0]**pp > upper_bound?
        # if true, pp is too large
        # written differently, the largest possible power is min(max_pow, math.floor(log(primes[0]) upper_bound/current_n))
        if len(primes) == 0:
            return []
        max_pow = min(max_pow, math.ceil(math.log(upper_bound/current_n, primes[0])))
        if max_pow < 2:
            return []

        power_candidates = list(range(2, max_pow+1, 2))
        candidate_lists = []
        for p in power_candidates:
            if num_factors * (p+1) > target_n_sq: # list is done
                candidate_lists.append([p])
            elif len(primes) > 1:
                found_list = [p] + build_list(primes[1:], num_factors * (p+1), p, current_n * primes[0]**p)
                if num_factors * math.prod(x+1 for x in found_list) > target_n_sq:
                    candidate_lists.append(found_list)

        if len(candidate_lists) == 0:
            return []
        candidate_list_values = [math.prod(p**e for e,p in zip(arr,primes)) for arr in candidate_lists]
        min_candidate_list_value = min(candidate_list_values)
        index_of_best_candidate_list = candidate_list_values.index(min_candidate_list_value)
        best_candidate_list = candidate_lists[index_of_best_candidate_list]

        return best_candidate_list

    power_of_2_upper_bound = math.floor(math.log(upper_bound, 2))
    sol_list = build_list(prime_candidates, 1, power_of_2_upper_bound, 1)

    return int(math.sqrt(get_number_from_pf_array(sol_list)))



if __name__ == "__main__":
    print(solve())


