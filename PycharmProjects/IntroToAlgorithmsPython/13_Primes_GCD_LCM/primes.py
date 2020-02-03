import math
import time


def naive_is_prime(n):
    """ check whether n is prime or not O(n) """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime(n):
    """ check whether n is prime or not O(sqrt(n)) """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Exercise
# Generate a list of primes (from 2 to 100,000)
# [2, 3, 5, ..., 99991]
def generate_prime_list(n):
    """ generate a list of primes from 2 to n """
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


start_time = time.time()
print(generate_prime_list(1_000_000))
print(f"{time.time() - start_time} seconds")