# Sampel for checking function annotation


def f(str1, str2):
    print('Annotation of f:', f.__annotations__)
    return  str1 + ' ' + str2

def f1(str1: str, str2: str) -> str:
    print('Annotation of f1:',f1.__annotations__)
    return str1 + ' ' + str2

f('abc', 'def')
f1('xyz', '123')


squares = [ x**2  for x in range(10)]
print(squares)


print(' square of odd numbers', [x**2 for x in range(10) if x%2 == 1])

squareMap = list(map(lambda x: x**2, range(10)))
print('squareMap:', squareMap)