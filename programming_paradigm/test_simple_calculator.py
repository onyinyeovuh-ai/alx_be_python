import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----- Addition Tests -----
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    # ----- Subtraction Tests -----
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-2, 3), -5)

    # ----- Multiplication Tests -----
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    # ----- Division Tests -----
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_float_result(self):
        # Ensure floating-point division works
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()