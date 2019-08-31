""" checking the conditional operators """

string1, string2, string3 = '', 'joe', 'kindel'

non_null_string = string1 or string3 or string2
print(f'non null string: {non_null_string}')

print(f' temp: {string1 or string2 or string3}')

print(f' (1, 2) < (1, 2, -1) : {(1, 2) < (1, 2, -1) }')