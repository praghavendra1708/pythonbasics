import sys
import os

print(f'present working directory is : {os.getcwd()}')

try:
    f = open('./myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print('I/O Error {0}'.format(err))
except ValueError:
    print('Could not convert data into integer')
except (RuntimeError, TypeError, NameError) as misc:
    pass
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



try:
    raise Exception('sunday', 'holiday')
except Exception as myExcept:
    print(f'type of object is {type(myExcept)}')
    print(f'args of myExcept is {myExcept.args}')
    print(f'calling __str__ method of myExcept is {myExcept}')

with open("myfile.txt") as f:
    for line in f:
        print(line)