import unittest
import math
from calculate import Calculator  # Импортируем класс Calculator из файла calculator.py


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(2.5, 3.5), 6.0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(1, -1), 2)
        self.assertEqual(self.calculator.subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(5, -1), -5)
        self.assertEqual(self.calculator.divide(7.5, 2.5), 3.0)
       

    def test_sine(self):
        self.assertAlmostEqual(self.calculator.sine(0), 0, places=7)
        self.assertAlmostEqual(self.calculator.sine(math.pi / 2), 1, places=7)
        self.assertAlmostEqual(self.calculator.sine(math.pi), 0, places=7)

    def test_cosine(self):
        self.assertAlmostEqual(self.calculator.cosine(0), 1, places=7)
        self.assertAlmostEqual(self.calculator.cosine(math.pi / 2), 0, places=7)
        self.assertAlmostEqual(self.calculator.cosine(math.pi), -1, places=7)

    def test_tangent(self):
        self.assertAlmostEqual(self.calculator.tangent(0), 0, places=7)
        self.assertAlmostEqual(self.calculator.tangent(math.pi / 4), 1, places=7)
        # self.assertIsNone(self.calculator.tangent(math.pi / 2))  # Тангенс не определен

    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(9), 3)
        self.assertEqual(self.calculator.square_root(0), 0)
        self.assertAlmostEqual(self.calculator.square_root(2), math.sqrt(2), places=7)
        self.assertIsNone(self.calculator.square_root(-1))  # Квадратный корень из отрицательного числа

    def test_power(self):
      self.assertEqual(self.calculator.power(2, 3), 8)
      self.assertEqual(self.calculator.power(5, 0), 1)
      self.assertEqual(self.calculator.power(10, -1), 0.1)
      self.assertAlmostEqual(self.calculator.power(2, 0.5), math.sqrt(2), places=7)


if __name__ == '__main__':
    unittest.main()