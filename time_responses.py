from p1to100 import eul_0044
from p1to100 import eul_0001, eul_0002, eul_0003, eul_0004, eul_0005, eul_0006, eul_0007, eul_0008, eul_0009, eul_0010
import time


def run_first_10():
    functions = {1: eul_0001.euler_problem_1, 2: eul_0002.euler_problem_2, 3: eul_0003.euler_problem_3, 4: eul_0004.euler_problem_4,
                 5: eul_0005.euler_problem_5, 6: eul_0006.euler_problem_6, 7: eul_0007.euler_problem_7, 8: eul_0008.euler_problem_8,
                 9: eul_0009.euler_problem_9, 10: eul_0010.euler_problem_10}
    for k in functions:
        f = functions[k]
        start_time = time.perf_counter()
        f()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"problem {k}: {elapsed_time} seconds")

run_first_10()

# this only runs problem 44, update in future to run problem x for given x


def run_problem(x):
    f = eul_0044.euler_problem_44
    start_time = time.perf_counter()
    f()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"problem {44}: {elapsed_time} seconds")


run_problem(44)

# @TODO: want to run all the problems and flag any that take more than 10 seconds
