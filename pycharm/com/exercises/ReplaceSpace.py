# Replace space with %20
import unittest


def replace_space(my_string):
    if my_string is None or len(my_string) == 0:
        return my_string

    arr_str = []
    space_count = 0
    for char in my_string:
        arr_str.append(char)
        if char == ' ':
            space_count += 1

    len1 = len(my_string) - 1
    arr_str.extend(['' for _ in range(2*space_count)])
    print(f' arr after appending empty spaces {arr_str}')

    total_size = len(arr_str) - 1

    '''for i in range(len(arr_str)):
        if arr_str[len1-i] == ' ':
            arr_str[total_size] = '0'
            arr_str[total_size-1] = '2'
            arr_str[total_size-2] = '%'
            total_size = total_size - 3
        else:
            arr_str[total_size] = arr_str[len1-i]
            total_size = total_size - 1'''

    for i in range(len(my_string) - 1, 0, -1):
        if my_string[i] == ' ':
            arr_str[total_size] = '0'
            arr_str[total_size-1] = '2'
            arr_str[total_size-2] = '%'
            total_size -= 3
        else:
            arr_str[total_size] = arr_str[i]
            total_size -= 1

    print(arr_str)
    return ''.join(arr_str)


class Test(unittest.TestCase):
    def test_replace_space(self):
        arr_test_str = [
            ('my space', 'my%20space'),
            ('my  space', 'my%20%20space'),
            ('my  space ', 'my%20%20space%20')
        ]
        for (input1, output1) in arr_test_str:
            self.assertTrue(replace_space(input1), output1)


if __name__ == '__main__':
    unittest.main()
