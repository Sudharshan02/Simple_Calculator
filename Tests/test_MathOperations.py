import unittest

from MathOperations.addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.division import Division


class MytestCase(unittest.TestCase):
    def test_addition(self):
        result = Addition.sum(1, 2)
        self.assertEqual(3, result)

    def test_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_multiplication(self):
        self.assertEqual(2, Multiplication.multiplication(1, 2))


    def test_division(self):
        self.assertEqual(2, Division.quotient(10, 5))


if __name__ == '__main__':
    unittest.main()