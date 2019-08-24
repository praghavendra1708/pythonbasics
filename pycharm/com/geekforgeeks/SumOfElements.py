""" Program to find the sum of list elements"""


myList = range(10)

print("mylist", myList)

import functools

sumOfElem = functools.reduce(lambda x, y: x + y, myList, 0)
print('Sum of elements is:' ,sumOfElem)

result = 0
for x in myList:
    result += x

print('Result is:', result)

