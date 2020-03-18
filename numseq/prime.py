import math


def is_prime(n):
    isPrime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
                break
    else:
        isPrime = False

    return isPrime


def primes(n):
    prime_list = []

    if n > 1:
        for i in range(2, n):
            if is_prime(i):
                prime_list.append(i)
    return prime_list
