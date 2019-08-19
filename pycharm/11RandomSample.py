import random

""" Random number generator samples """

# Random numbers are in a uniform distribution
for i in range(10):
    print(random.random())

# printing random number between range 3,7
# scalling by 4 as the 7 -3
# readjusting the base point adding by 3

print(" Changing the range and scope")
for i in range(10):
    print(random.random()*4 + 3)


print(" Changing the range and scope with library method")
for i in range(10):
    print(random.randrange(3,7))


# Random number with Normal distribution : standard deviation, mean
print('Random numbers with standard deviation')
for i in range(10):
    print(random.normalvariate(5, 2))


# Random selection from list
print("Random selection from a list")
myList = ["mylist", 2, 3.14, False]

for i in range(10):
    print(random.choice(myList))