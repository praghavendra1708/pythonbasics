import re

myregex = re.compile(r'\d{3}-\d{3}-\d{4}')

mymatch = myregex.search('Cell: 415-555-9999 Work: 212-555-0000')

print(f'finding format {mymatch.group()}')