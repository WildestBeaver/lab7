import unittest
from funcy import sub_func_2

# Юнит тест подфункции 2 (sub_func_2)
class TestSubFunc2(unittest.TestCase):

    def test_1(self):
        self.assertRaises(ValueError, sub_func_2, 2)

    def test_2(self):
        self.assertRaises(ValueError, sub_func_2, 1)

    def test_3(self):
        self.assertRaises(ValueError, sub_func_2, 0)

    def test_4(self):
        self.assertAlmostEqual(sub_func_2(-1), 1.609437912)

    def test_5(self):
        self.assertAlmostEqual(sub_func_2(-2), 2.302585093)

if __name__ == '__main__':
    unittest.main()
