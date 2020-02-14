import unittest


def compress_seq(my_string):
    arr_chars = []
    prev_char = ''
    count = 0
    for chars in my_string:
        print(f'char: {chars}  prev char: {prev_char}')
        if chars != prev_char and len(prev_char) == 1:
            arr_chars.append(prev_char)
            if count > 1:
                arr_chars.append(str(count))
            count = 1
            prev_char = chars
        elif len(prev_char) == 0:
            count = count + 1
            prev_char = chars
        else:
            count = count + 1

    arr_chars.append(prev_char)
    if count > 1:
        arr_chars.append(str(count))

    print(arr_chars)
    return ''.join(arr_chars)



def compress_seq_v1(my_string):
    if not my_string or len(my_string) == 1:
        return my_string
    count = 1
    arr_str = []
    for i in range(1, len(my_string)):
        if my_string[i-1] != my_string[i]:
            arr_str.append(my_string[i-1])
            if count > 1:
                arr_str.append(str(count))
            count = 1
        else:
            count = count + 1
    arr_str.append(my_string[-1])
    if count > 1:
        arr_str.append(str(count))
    print(f' output : {arr_str}')
    return ''.join(arr_str)


class Test(unittest.TestCase):
    def test_compress_seq(self):
        arr_string = [('abcdef', 'abcdef'),
                      ('aabbbeeeffeeeggg', 'a2b3e3f2e3g3'),
                      ('bcdeffflllmmm', 'bcdef3l3m3')]
        for (input1, output1) in arr_string:
            self.assertEqual(compress_seq_v1(input1), output1)


if __name__ == '__main__':
    unittest.main()
