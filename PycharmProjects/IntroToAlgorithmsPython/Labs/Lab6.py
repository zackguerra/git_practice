""" Primes, GCD, LCM """


def is_prime(n):
    """ Check if n is prime """

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    """ GCD of a and b """

    while (a):
        b, a = a, b % a
    return b


def lcm(a, b):
    """ LCM of a and b """

    if a > b:
        greater = a
    else:
        greater = b
    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """

    prime = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime.append(i)
    return prime
