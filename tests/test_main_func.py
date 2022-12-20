import unittest
from funcy import main_func

# Юнит тест главной функции (main_func)
class TestSubFunc1(unittest.TestCase):

    def test_1(self):
        self.assertRaises(ValueError, main_func, 2)

    def test_2(self):
        self.assertRaises(ValueError, main_func, 1)

    def test_3(self):
        self.assertRaises(ValueError, main_func, 0)

    def test_4(self):
        self.assertAlmostEqual(main_func(-1), 2.109437912434)

    def test_5(self):
        self.assertAlmostEqual(main_func(-2), 2.552585092994)

if __name__ == '__main__':
    unittest.main()
