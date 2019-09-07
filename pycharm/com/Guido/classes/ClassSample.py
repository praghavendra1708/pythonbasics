class Employee(object) :
    def __init__(self, name, age, empid):
        self.name = name
        self.age = age
        self.empid = empid


x = 5
x = True
print(f'x.__class__ is: {x.__class__}')

# Checking inheritance
print(f'is x instance of int :  {isinstance(x, float)}')
print(f'is int subtype of float: {issubclass(float, int)}')


mystrint = 'ABC'
it_obj = iter(mystrint)
print(f'it_obj type: {type(it_obj)}')
print(f'next(it_obj): {next(it_obj)}')
print(f'next(it_obj): {next(it_obj)}')
print(f'next(it_obj): {next(it_obj)}')
print(f'next(it_obj): {next(it_obj)}')