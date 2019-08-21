# Write a function 3x + 1
def fun1(x):
    """ function returns a 3x + 1"""
    return 3 * x + 1


print('fun1 response is', fun1(3))

# Writing the same function with lambda expression
le1 = lambda x: 3 * x + 1
print('lambda expression response is', le1(3))

mylist = ['ABC 789', 'XYZ 123', 'FGH 456']
mylist.sort(key=lambda name: name.split(' ')[-1].lower(), reverse=False)
print(mylist)


# Building functions of functions
def quad_fun(a, b, c):
    """This is a quadratic function : a*x**2 + b*x + c"""
    return lambda x: a * x ** 2 + b * x + 1


my_quad_exp = quad_fun(2, 3, 1)
print('Output of quad expression is', my_quad_exp(2))

# Other way of doing the same is
print('Anonymous function is', quad_fun(2, 3, 1)(2))
