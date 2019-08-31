"""  different kinds of looping techniques """

# Looping through the maps

my_dict = dict([('India', 'Delhi'), ('AP', 'Unknown'), ('Telengana', 'Hyderabad')])

print(*my_dict, sep='\n')

for k, v in my_dict.items():
    print(f'Key:{k} value:{v}')

print()
# looping through list and getting the position with item
my_list = ['item1', 'item2', 'item3']
for i, item in enumerate(my_list):
    print(f'position:{i} item:{item}')


# looping overing two list at a same time
metadate_lt = ['name', 'job', 'game']
details_lt = ['jnon', 'SoftEngg', 'Cricket']

for item1, item2 in zip(metadate_lt, details_lt):
    print(f'item1: {item1} item2: {item2}')

# sorting the list 
for item in sorted(metadate_lt):
    print(f'item:{item}')

