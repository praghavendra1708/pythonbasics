""" Interpolate variable in string """

# For version 3.7
x = 10
formatedString3_7 = f"Variable x value is {x}. Check out"
print(formatedString3_7)

# Tried and tested way in 3.5 is
formatedString3_5 = "Variable x value is {}. Check out".format(x)
print('Using format method x:{} '.format(formatedString3_7))

""" These are different way of interpolating the variable with string """
x = 1
y = 2
z = x + y

# Used in 3.7
print(f'sum of {x} + {y} is {z}')

# Used in 3.5
print('sum of {} + {} is {}'. format(x, y, z))

# Used in 2.xx
print('sum of %d + %d is %d' %(x, y, z))
