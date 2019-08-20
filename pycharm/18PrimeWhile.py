# This is example to demonstrate if a number is prime or not


def isprime(x):
    """ Returns 'True' if x is a prime number. False otherwise"""
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


print("prime numbers between 5, 20 are:", [x for x in range(5, 21) if isprime(x)])


import math

def isprime_1(x):
    """ Returns True is the number is prime. False if not"""
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        uplimit = math.floor(math.sqrt(x)) + 1
        for i in range(3, uplimit, 2):
            if x % i == 0:
                return False
    return True

import time

upperlimit = 10000

strar_time = time.time()
print("prime numbers between 1, 10000 are:", [x for x in range(1, upperlimit) if isprime_1(x)])
print("time taken with v1 is:", (time.time() - strar_time) )


strar_time = time.time()
print("prime numbers between 1, 10000 are:", [x for x in range(1, upperlimit) if isprime(x)])
print("time taken with v1 is:", (time.time() - strar_time) )