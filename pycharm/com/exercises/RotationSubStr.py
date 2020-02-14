import unittest


def is_rotation_of_string(my_string1, my_string2):
    if my_string1 is None and my_string2 is None:
        return True

    if my_string1 is None or my_string2 is None:
        return False

    if len(my_string1) != len(my_string2):
        return False

    if (my_string1 + '' + my_string1).find(my_string2) == -1:
        return False
    else:
        return True


class UnitTestCaseClass(unittest.TestCase):
    def test_is_rotation_of_string(self):
        true_cases = [
            ('abcdef', 'cdefab'),
            ('12345', '51234')
        ]

        false_cases = [
            ('abcdef', 'cedfab'),
            ('12345', '15234'),
            (None, '')
        ]

        for my_string1, my_string2 in true_cases:
            self.assertTrue(is_rotation_of_string(my_string1, my_string2))

        for my_string1, my_string2 in false_cases:
            self.assertFalse(is_rotation_of_string(my_string1, my_string2))


if __name__ == '__main__':
    unittest.main()