"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
# powers of single-digit numbers

def check_powers(p):
    matches = 0
    for i in range(1,10):
        if len(str(i**p)) == p:
            matches += 1
    return matches

match_count = 0
for x in range(1, 100):
    match_count += check_powers(x)

def euler_problem_63():
    print(match_count)

if __name__ == "__main__":
    euler_problem_63()
