import math

def is_prime(x):
    if not isinstance(x, int) or x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

"""
Input integer x, returns list of positive integer divisors of x
O(root(x)) time
"""
def find_divisors(x):
    divisors = [1]
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            divisors.append(i)
            if x/i != i:
                divisors.append(int(x/i))
    return divisors