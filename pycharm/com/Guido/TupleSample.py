""" This a module for testing tuple in pyton"""


empty_tuple = ()
single_elem_tuple = 'one',

print(f'Type of empty_tuple is {type(empty_tuple)}')
print(f'Type of single_elem_tuple is {type(single_elem_tuple)}')


# Packing into a tuple
t = 123, 345, 'myworld'

# Unpacking tuple
x, y, z = t

print(f'x values is {x}')

# Packing and unpacking in sinle step
x, y, z = 123, 456, 'myworld'


print(f'x={x}, y={y}, z={z}')


mydict = {"India": "Delhi", "ap": "Unknown", "telangana": "Hyderabad"}

#creating dictinoary using lists
mydict_lt = dict([("India", "Delhi"), ("AP", "Unknown"), ("Telangana", "Hyderabad")])
print(*mydict_lt.items(), sep='\n')
