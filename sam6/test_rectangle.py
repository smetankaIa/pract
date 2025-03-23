import unittest
from sam6 import Rectangle  


class TestRectangle(unittest.TestCase):
    def test_positive_area(self):
#Проверяет вычисление площади для прямоугольника с положительными сторонами.
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.calculate_area(), 50)

    def test_zero_width(self):
 #Проверяет, что площадь равна None при нулевой ширине.
        rectangle = Rectangle(0, 10)
        self.assertIsNone(rectangle.calculate_area())

    def test_zero_height(self):
#Проверяет, что площадь равна None при нулевой высоте.
        rectangle = Rectangle(5, 0)
        self.assertIsNone(rectangle.calculate_area())

    def test_negative_width(self):
#Проверяет, что площадь равна None при отрицательной ширине.
        rectangle = Rectangle(-5, 10)
        self.assertIsNone(rectangle.calculate_area())

    def test_negative_height(self):
#Проверяет, что площадь равна None при отрицательной высоте.
        rectangle = Rectangle(5, -10)
        self.assertIsNone(rectangle.calculate_area())

    def test_float_values(self):
#Проверяет вычисление площади для прямоугольника с дробными сторонами.
        rectangle = Rectangle(2.5, 4.0)
        self.assertEqual(rectangle.calculate_area(), 10.0)


if __name__ == '__main__':
    unittest.main()