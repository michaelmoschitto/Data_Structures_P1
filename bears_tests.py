import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(192))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        self.assertTrue(bears(250))
    #
    def test_bear_06(self):
        self.assertFalse(bears(-250))

    def test_bear_07(self):
        self.assertFalse(bears(85))

    def test_bear_08(self):
        self.assertFalse(bears(297))

    # with self.assertRaises(ValueError):  # list of noneType
    #     bears(None)

    def test_bear_09(self):
        self.assertFalse(bears(3000))





if __name__ == "__main__":
    unittest.main()
