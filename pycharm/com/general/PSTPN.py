# Parse Number to bunch of prime numbers


def isPrime(num):
    print(f'Inside prime : {num}')
    if num < 2:
        return False
    if num == 2:
        return True
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i = i + 1
    return True


for i in range(4, 5):
    print(f"i :{i}")

count = 0
allOutput = []


def split(start, end, output):
    global count
    print(f'inside split {start}, {end}, {output}')
    if start == end:
        return

    tempoutput = output.copy()
    for i in range(start, end):
        if isPrime(int(mystring[start:i+1])):
            output.append((start, i))
            if i + 1 == end:
                print(output)
                allOutput.append(output.copy())
                count = count + 1
            else:
                split(i+1, end, output)
            output.pop()
    output = tempoutput




#for i in range(1,25):
#    num = i
#    print(f"is Number {num} is prime {isPrime(num)}")


def split_v1(start, end, output):
    print(f'inside split {start}, {end}, {output}')
    if start + 1 == end:
        allOutput.append(output.copy())
        return
    for i in range(start, end):
        if isPrime(int(mystring[start:i+1])):
            output.append((start, i))
            split_v1(i+1, end, output)
            output.pop()


mystring = '1379'
split_v1(0, len(mystring) + 1, [])

print(f"all outputs {allOutput}")

for i in allOutput:
    outputlist = []
    for j in i:
        outputlist.append(mystring[j[0]:j[1]+1])
    print(outputlist)
