def fun() :
    global var
    print(var)
    var = 'set local'

var = 'set global'
fun()
print(var)


def f(arg=i):
    print arg

f()
f(1)
