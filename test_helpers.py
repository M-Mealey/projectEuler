from helpers import is_prime, find_divisors, prime_sieve
import pytest

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(689461) == True
    assert is_prime(1939) == False

def test_find_divisors():
    assert find_divisors(20) == [1, 2, 4, 5, 10]
    assert find_divisors(1) == [1]
    assert find_divisors(0) == [1]
    assert find_divisors(25) == [1, 5]

def test_prime_sieve():
    assert prime_sieve(5) == [2, 3]
    assert prime_sieve(15) == [2, 3, 5, 7, 11, 13]
    assert prime_sieve(66) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    assert len(prime_sieve(1000)) == 168