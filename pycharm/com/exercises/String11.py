myString = "mynewstring"
my_String = "abcdefa"


def has_unique_chars(my_string):
    if my_string is None or len(my_string) == 0:
        return True
    for i in range(0, len(my_string) - 1):
        for j in range(i+1, len(my_string)):
            if my_string[i] == my_string[j]:
                print(f' {i}  is char {my_string[i]}  {j} is char {my_string[j]}')
                return False
    return True


print(f' {my_String} has unique char is {has_unique_chars(my_String)}')


def has_unique_chars_arr(my_string):
    if my_string is None or not my_string:
        return True
    arr = [False for i in range(0, 256)]
    for chars in my_string:
        if arr[ord(chars)] == True:
            print(f' already present char is : {chars}')
            return False
        else:
            arr[ord(chars)] = True
    return True


print(f'{my_String} has unique chars : {has_unique_chars_arr(my_String)}')


my_new_string = "abcda"


def had_unique_chars_arr_ver(my_string):
    if my_string is None or not my_string:
        return True
    flag_arr = [False for i in range(0, 256)]
    for char in my_string:
        if flag_arr[ord(char)]:
            print()
            return False
        else:
            flag_arr[ord(char)] = True
    return True

print(f'{my_new_string} has unique chars is {had_unique_chars_arr_ver(my_new_string)}')

