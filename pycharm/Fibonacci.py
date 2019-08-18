print(' Fibonacci series as per the equation', end="\n\n")


def fibonacci(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 10):
    print(fibonacci(i))

print('Fibonacci series with out repeating the code', end="\n\n")
first = 1
second = 1


def fibonacci1(n):
    global first
    global second
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        temp = second
        second = second + first
        first = temp
        print(second)
        second = fibonacci1(n - 1)


fibonacci1(10)

print('Fibonacci series with for loop:', end="\n\n")


def funfibfor(n):
    first = 1
    second = 1
    if n == 1:
        print(first)
    elif n == 2:
        print(second)
    else:
        for i in range(2, n):
            temp = second
            second = second + first
            first = temp
            print(first)


funfibfor(10)

print('Fibonacci using local cache')
local_cache = {}  # is a empty map


def fibonacci_lc(n):
    # check cache for the nth element
    if n in local_cache:
        return local_cache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        local_cache[n] = fibonacci_lc(n - 1) + fibonacci_lc(n - 2)
        return local_cache[n]


fibonacci_lc(10)

# Using Function Cache
print('Fibonacci using functtool cache')
from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci_lru_cache(n):
    if type(n) != int:
        return TypeError("Invalid type of input")

    if n < 1:
        return ValueError("Invalid value of input")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)


print(fibonacci_lru_cache(50))

print(fibonacci_lru_cache(1.1))

print(fibonacci_lru_cache(-2))
