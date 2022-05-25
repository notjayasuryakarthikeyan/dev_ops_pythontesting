import unittest
from src import calculator
class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(5, 5), 10)
        self.assertEqual(calculator.addition(-3, 3), 0)
        self.assertEqual(calculator.addition(-5,-5),-10)
    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(15, 5), 10)
        self.assertEqual(calculator.subtraction(-1, 2),-3)
        self.assertEqual(calculator.subtraction(-1,-1), 0)
    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(20, 5), 100)
        self.assertEqual(calculator.multiplication(-2, 1),-2)
        self.assertEqual(calculator.multiplication(-1,-3), 3)
    def test_division(self):
        self.assertEqual(calculator.division(10, 10), 1)
        self.assertEqual(calculator.division(-1, 1),-1)
        self.assertEqual(calculator.division(-2,-2), 1)
        self.assertEqual(calculator.division(6, 3), 2)
        
if __name__ == '__main__':
    unittest.main()