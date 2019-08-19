# Example for  sorting it can be done in two ways
# list.sort
# Sorted() -> list

myList = [('Kurnool', 32), ('Hyderabad', 28), ('Banglore', 20)]
print('sorted list based on temperature', sorted(myList, key=lambda x: x[1], reverse=False))

print('sorting tuple', sorted(('Kurnool', 'Hyderabad', 'Banglore')))