mystring = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

word = ''
spaces = ''
prevChar = ''

for c in mystring:
    if(c.isupper()):
        if (prevChar == ','):
            spaces += '\t'
            print(spaces + word)
            word = ''
            spaces = ''
        elif(prevChar == '.'):
            space = ''
            print(spaces + word)
            word = ''
    word += c
    if(c != ' '):
        prevChar = c









