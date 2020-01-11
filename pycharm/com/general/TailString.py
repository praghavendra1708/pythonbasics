# Check if string ends with any string in given list

mainString = "This is my Testing"

checkString = ["ing", "sting", "is" ]

for testString in checkString:
    if mainString[::-1].find( testString[::-1]) == 0:
        print(f"'{testString}' is part of tail of '{mainString}'")

