#Remove duplicate chars in place
import unittest


def remove_duplicates():
    global my_num_arr
    if len(my_num_arr) == 1 or not my_num_arr:
        print(f'Array is empty or just has one element')
        return
    point = 1
    for i in range(1, len(my_num_arr)):
        found = False
        for j in range(0, point):
            if my_num_arr[j] == my_num_arr[i]:
                found = True
                break
        if not found:
            my_num_arr[point] = my_num_arr[i]
            point = point + 1
    my_num_arr = my_num_arr[:point]
    print(my_num_arr)


class Test(unittest.TestCase):
    def test_remove_duplicate_v1(self):
        test_string_arr = [('abcde', 'abcde'), ('abcdefabcdef', 'abcdef')]
        for (input1, output1) in test_string_arr:
            print(f'input1 {input1} output1 {output1}')
            self.assertEqual(remove_duplicate_v1(input1), output1)


def remove_duplicate_v1(my_string):
    if my_string is None or len(my_string) == 1:
        return my_string

    arr_str = []
    for char in my_string:
        arr_str.append(char)

    point = 1
    for i in range(1, len(arr_str)):
        found = False
        for j in range(i):
            if arr_str[i] == arr_str[j]:
                found = True
        if not found:
            arr_str[point] = arr_str[i]
            point += 1
    return ''.join(arr_str[:point])


if __name__ == '__main__':
    unittest.main()



