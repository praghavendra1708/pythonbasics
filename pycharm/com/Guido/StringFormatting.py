""" Controlled formatting """

my_dict = {'India': 'Delhi', 'AP': 'Unknown', 'Telengana': 'Hyderabad'}
for k, v in my_dict.items():
    print(f'{k:10} ==> {v!r:<10}')


with open('/Users/raghavendrareddy/MyWorkspace/MyPython/while_temp.py', 'r') as file_ptr:
    for line in file_ptr:
        print(line)

