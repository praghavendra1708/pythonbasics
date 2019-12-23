import re

myString = 'Cell: 415-555-9999 Work: 212-555-0000'

myregex = re.compile(r'\d{3}-\d{3}-\d{4}')
mymatch = myregex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(f'finding format {mymatch.group()}')

myregex_1 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mymatch_1 = myregex_1.search('Cell: 415-555-9999 Work: 212-555-0000')
print(f'finding format {mymatch_1.group(2)}')


mymatch_2 = myregex_1.findall(myString)
print(f'list of matching {mymatch_2}')


mymatch_3 = myregex.findall(myString)
print(f'list of matching {mymatch_3}')