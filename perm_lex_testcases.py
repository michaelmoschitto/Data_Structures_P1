import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex3(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex0(self):
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

    def test_perm_gen_lex1(self):
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex2(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab', 'ba'])

if __name__ == "__main__":
        unittest.main()
