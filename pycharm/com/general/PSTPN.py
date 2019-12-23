# Parse Number to bunch of prime numbers

def isPrime( num ):
    if(num == 1):
        return True

    if(num == 2):
        return False
    i = 2
    while(i*i <= num):
        if(num%i == 0):
            return False
        i = i + 1
    return True


for i in range(1,25):
    num = i
    print(f"is Number {num} is prime {isPrime(num)}")


