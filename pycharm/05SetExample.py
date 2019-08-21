example = {'ABC', 2, 3.14, False}

print(example)

example.discard(2)

print(example)


even = {2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}

print("union: " , even.union(odd))
print("intersection: ", even.intersection(odd))