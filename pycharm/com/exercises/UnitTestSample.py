import unittest

class UnitTesting(unittest.TestCase):
    def test_string(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertFalse(False)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()