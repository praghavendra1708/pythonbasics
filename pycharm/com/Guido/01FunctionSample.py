# different ways of defining function
def febnocci(n):
    """ Display the fist n febonacci numbers """

    a, b = 0, 1
    result = []
    for i in range(0, n):
        result.append(a)
        a, b = b, a + b
    return result


print(f'fibonacci series is {febnocci(10)}')


# Unpacking the tuple, lists as arguments
args = [3, 6]
for i in range(*args):
    print(i, end='-')

print()
print(1, 2, 3, sep=':', end='\n')

def ask_ok(prompt, retries=2, remainder='Please try it again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'nop', 'nope'):
            return False
        retries -= 1
        if retries == 0:
            print(remainder)


ask_ok('Do u want to delete the file\n')


# default argument value is evaluated only once
def f(a, lt=[]):
    lt.append(a)
    return lt


print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]


# Fixing the above issue
def f1(a, lt=None):
    """ Fixing the default argument value in case of muttable type"""
    if lt is None:
        lt = []
    lt.append(a)
    return lt


print(f"f1 vaule {f1(1)}")
print(f'f1 value {f1(2)}')


# converting
def bookshop(kind, *arguments, **keywords):
    print(f"is there any {kind} of book")
    print(f'No we don`t have {kind} of book')

    for args in arguments:
        print(f'args {args}')

    for key in keywords:
        print(key + ' ' + keywords[key])


bookshop('Life of pie', 'fantasy', 'psychological', Author='Unknown')

arg1 = ('fantasy', 'romance')
arg2 = {'Author':'Unknown'}
bookshop('Life of pie', arg1, arg2)


# Arbitrary arguments
def concat(*args, sep='/'):
    return sep.join(args)

print( concat('mercury', 'venus', 'earth') )


# Adding comment from windows
# Adding comment form mac desktop
# Adding comment from mac laptop