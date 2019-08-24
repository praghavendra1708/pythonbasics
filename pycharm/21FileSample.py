# Exmaples for read and write to file

# Unsafe way of opening a file
path = './io/GitIgnore.txt'
fileio = open(path)
textInFile = fileio.read()

print("Contents of files are:",  textInFile)
fileio.close()

# Safe way of opening a file
with open(path) as fileio:
    textInFile_1 = fileio.read()

print("Contents of file: textInFile are", textInFile_1)


#Handling an exception
newPath = './io/output.txt'
try:
    with open(newPath) as fileio:
        textInFile_2 = fileio.read()
except FileNotFoundError:
    print('path', newPath, 'doesn`t exists')


#Writing to a file
myList = ['cricket', 'badminton', 'the verge']
with open(newPath, mode='w') as fileio:
    for item in myList:
        fileio.write(item)


#Writing to a file
myList = ['cricket', 'badminton', 'the verge']
with open(newPath, mode='w') as fileio:
    for item in myList:
        print(item, file=fileio)
