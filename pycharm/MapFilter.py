import math
# Example of map function
radius_lt = [2, 3, 4, 5]

print('Output of map function:', list(map(lambda r: 2*math.pi*r**2, radius_lt)))


temp_lt = [('kurnool', 32),('Hyderabad', 28),('banglore', 20)]
print("temperature in farientheit is",
      list(map(lambda x: (x[0], (9*x[1])/5 + 32), temp_lt)))

# Example of filter funtcion
lt = list(range(1,10))
print(lt)
print("filter example", list(filter(lambda x: x > 5, lt)))


# Example of reduce function
myprimlist = [2, 3, 5, 7, 11, 13]
import functools
print('Reduce function example:', functools.reduce(lambda x, y: x * y, myprimlist))