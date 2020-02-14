

myString = 'Geeks'
allSubString = [myString[i:j] for i in range(len(myString)) for j in range(i+1, len(myString) + 1)]

print(allSubString)


def isPrime(inputStr):
    print(f'input: {inputStr}')
    inputNum = int(inputStr)
    if inputNum == 0:
        return False
    if inputStr == 1:
        return True
    if inputStr == 2:
        return False

    i = 2
    while i * i <= inputNum:
        if inputNum % i == 0:
            return False
        i = i + 1

    return True


allCombinations = []
myNumber = '2489'


def breakIntoPrime(start, end, output):
    print(f' input start: {start} end: {end} output: {output}')
    if start + 1 == end:
        allCombinations.append(output.copy())
        print(output)
        return

    for i in range(start + 1, end):
        if isPrime(myNumber[start:i]):
            output.append((start, i))
            breakIntoPrime(i, end, output)
            output.pop()


breakIntoPrime(0, len(myNumber)+1, [])
print(allCombinations)

