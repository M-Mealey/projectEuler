"""
Project Euler Problem 92
========================

A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 32 13 10 1 1
85 89 145 42 20 4 16 37 58 89

Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

goes_to_1 = set()
goes_to_1.add(1)
goes_to_89 = set()
goes_to_89.add(89)

# computes sum of squares of digits in integer x
def sum_square_digits(x):
    digits_squared = [int(c)**2 for c in str(x)]
    return sum(digits_squared)

upper_bound = 10000000
count = 0
for i in range(1, upper_bound):
    if i in goes_to_89:
        count +=1
    elif i in goes_to_1:
        continue
    else:
        chain = set()
        chain.add(i)
        current_i = i
        end = False
        while not end:
            current_i = sum_square_digits(current_i)
            chain.add(current_i)
            if current_i in goes_to_89:
                count += 1
                goes_to_89.update(chain)
                end = True
            elif current_i in goes_to_1:
                goes_to_1.update(chain)
                end = True

def euler_problem_92():
    print(count)

if __name__ == "__main__":
    euler_problem_92()