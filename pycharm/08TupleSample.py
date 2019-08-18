import sys

print('List of functions present in sys module:', dir(sys))

mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)

print('Size of mylist is:', sys.getsizeof(mylist))
print('Size of mytuple is:', sys.getsizeof(mytuple))
