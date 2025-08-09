import unittest
from Factorial import fact

class Test_Factorial(unittest.TestCase):

    def test_factorial(self):
        test_cases = [
            (5, 120),
            (0, 1),
            (-5, None)
        ]
        print()
        print("URK23CS1185 - M Durai Murugan")
        for i, (input_val, expected) in enumerate(test_cases):
            with self.subTest(test=i+1):
                result = fact(input_val)
                status = 'passed' if result == expected else 'failed'
                print(f"Test {i+1}: input={input_val}, output={result} ({status})")
                self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main(verbosity=0)