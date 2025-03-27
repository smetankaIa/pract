import unittest

class MyClass:
   # формула 3a^2 - b
    def __init__(self):
        self.result = None  

    def calculate_c(self, a, b):
        #Вычисляем параметр c по формуле 3a^2 - b. a: Параметр a (число) b: Параметр b (число).
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Параметры a и b должны быть числами.")

        self.result = 3 * (a ** 2) - b  # Сохраняем результат в атрибуте класса
        return self.result

    def prepare_data(self, a_str, b_str):
        #Подготавливаетм данные для вычисления, преобразуя строки в числа. 
        #a_str: Параметр a в виде строки. b_str: Параметр b в виде строки.
        try:
            a = float(a_str)
            b = float(b_str)
            return a, b
        except ValueError:
            print("Ошибка: Невозможно преобразовать строки в числа.")
            return None

    def process_result(self, a, b):

        #Вызываем метод calculate_c для вычисления c и возвращает отформатированную строку с результатом.
            #a: Параметр a (число).
            #b: Параметр b (число).
        try:
            self.calculate_c(a, b)  
            return f"При a = {a} и b = {b}, c = {self.result:.2f}" 
        except TypeError as e:
            return f"Ошибка: {e}"
        except Exception as e: 
            return f"Произошла ошибка: {e}"

# Тестирующий класс
class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.my_object = MyClass()

    def test_positive_values(self):
        result = self.my_object.process_result(2, 1)
        self.assertEqual(result, "При a = 2 и b = 1, c = 11.00")

    def test_negative_values(self):
        result = self.my_object.process_result(-3, -2)
        self.assertEqual(result, "При a = -3 и b = -2, c = 29.00")

    def test_zero_values(self):
        result = self.my_object.process_result(0, 0)
        self.assertEqual(result, "При a = 0 и b = 0, c = 0.00")

    def test_float_values(self):
        result = self.my_object.process_result(2.5, 1.5)
        self.assertEqual(result, "При a = 2.5 и b = 1.5, c = 17.25")

    def test_string_input(self):
        a, b = self.my_object.prepare_data("4", "2")
        result = self.my_object.process_result(a, b)
        self.assertEqual(result, "При a = 4.0 и b = 2.0, c = 46.00")

    def test_invalid_string_input(self):
        a, b = self.my_object.prepare_data("abc", "2")
        self.assertIsNone(a)

if __name__ == '__main__':
    unittest.main()