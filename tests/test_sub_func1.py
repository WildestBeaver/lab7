import unittest
from funcy import sub_func_1

# Юнит тест подфункции 1 (sub_func_1)
class TestSubFunc1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sub_func_1(5), 32)

    def test_2(self):
        self.assertEqual(sub_func_1(2), 4)

    def test_3(self):
        self.assertEqual(sub_func_1(0), 1)

    def test_4(self):
        self.assertEqual(sub_func_1(-1), 0.5)

    def test_5(self):
        self.assertEqual(sub_func_1(-2), 0.25)

if __name__ == '__main__':
    unittest.main()
