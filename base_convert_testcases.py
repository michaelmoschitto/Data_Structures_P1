import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):
    with self.assertRaises(ValueError):  # used to check for exception
        convert(100,1)

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base3(self):
        self.assertEqual(convert(105,3),"10220")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base162(self):
        self.assertEqual(convert(12623,16),"314F")

    def test_base12(self):
        self.assertEqual(convert(155,12), "10B")

    def test_base13(self):
        self.assertEqual(convert(181,13), "10C")

    def test_base14(self):
        self.assertEqual(convert(209,14), "10D")

    def test_base15(self):
        self.assertEqual(convert(239,15), "10E")

    def test_base16(self):
        self.assertEqual(convert(271,16),"10F")

    def test_base152(self):
        self.assertEqual(convert(13,15),"13")

    def test_base163(self):
        self.assertEqual(convert(110,16),"6E")

    def test_base11(self):
        self.assertEqual(convert(516,11),"42A")

    def test_base112(self):
        self.assertEqual(convert(219,11),"18A")

    def test_base_10(self):
        self.assertTrue(convert(100,10), "100")











if __name__ == "__main__":
        unittest.main()
