import unittest
from Factorial import fact

class Test_Factorial(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(fact(5),120)

    def test_negative(self):
        self.assertEqual(fact(-5),None)
        # with self.assertRaises(TypeError):
        #     fact(-5)

    def test_zero(self):
        self.assertEqual(fact(0),1)

if __name__ == '__main__':
    unittest.main()