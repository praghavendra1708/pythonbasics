# This sample code for list comprehensions

import math

print("Printing square root of first five numbers", [math.sqrt(x) for x in range(5)] )


print('Printing the square root of even number preset before 10', [math.sqrt(x) for x in range(10) if x % 2 == 0]
      )


print('Printing the square root of even number preset before 10', [(x, math.sqrt(x))  for x in range(10) if x % 2 == 0] )


# Cartation product

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

print('The cartation product of set A*B is:', [(x,y) for x in A for y in B] )