import re
from re import Match

print(r'\tTab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz word
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

def matchfun(mypattern):
    global text_to_search
    patInterator = mypattern.finditer(text_to_search)
    for x in patInterator:
        print(x)


pattern = re.compile(r'\b\D+?\s==')
matchfun(pattern)



# Matches phone number
phonePattern = re.compile(r'\b\d{3}[\.|-]\d{3}[\.|-]\d{4}\b')
print("Seaching for phone pattern")
matchfun(phonePattern)




# Seraching single back slash pattern
backSlashPatter = re.compile(r'\\')
backSlashPatter = re.compile('\\\\')

print(backSlashPatter.findall(r'\\\\\\'))

backSlashPatterWithRaw = re.compile(r'\\')
print(backSlashPatterWithRaw.findall('\\\\\\'))




