import unittest


def is_anagram(my_string1, my_string2):
    if my_string1 is None and my_string2 is None:
        return True

    if len(my_string1) != len(my_string2):
        return False

    alpha_count = [0 for _ in range(0, 256)]
    for char in my_string1:
        alpha_count[ord(char)] += 1

    print(alpha_count)

    for char in my_string2:
        alpha_count[ord(char)] -= 1
        if alpha_count[ord(char)] < 0:
            return False 
    return True


class UnitTesting(unittest.TestCase):
    def test_is_anagram(self):
        arr_true = [
            ('abcdefabcdef', 'abcdeffedcba'),
            ('aaaabbbccd', 'dccbbbaaaa')
        ]
        for (value1, value2) in arr_true:
            self.assertTrue(is_anagram(value1, value2))

        arr_true = [
            ('abcdefabcdef', 'abcdeffedcbaa'),
            ('aaaabbbccd', 'ddccbbbaaaa')
        ]
        for (value1, value2) in arr_true:
            self.assertFalse(is_anagram(value1, value2))


if __name__ == '__main__':
    unittest.main()

