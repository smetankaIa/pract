import math

def find_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Ошибка: Длина стороны должна быть больше 0."

    if a + b <= c or a + c <= b or b + c <= a:
        return "Ошибка: Сумма двух сторон должна быть больше третьей."

    if a == b == c:
        type_storona = "Равносторонний"
    elif a == b or a == c or b == c:
        type_storona = "Равнобедренный"
    else:
        type_storona = "Разносторонний"

    a2 = a**2
    b2 = b**2
    c2 = c**2

    if abs(a2 + b2 - c2) < 1e-6 or abs(a2 + c2 - b2) < 1e-6 or abs(b2 + c2 - a2) < 1e-6: 
        type_angle = "Прямоугольный"
    elif a2 + b2 < c2 or a2 + c2 < b2 or b2 + c2 < a2:
        type_angle = "Тупоугольный"
    else:
        type_angle = "Остроугольный"

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return f"Треугольник (стороны): {type_storona}, Треугольник (углы): {type_angle}, Площадь: {s:.2f}"


def fetch_num_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите числовое значение.")


while True:
    a = fetch_num_input("Введите длину стороны a: ")
    if a is None:
        continue  

    b = fetch_num_input("Введите длину стороны b: ")
    if b is None:
        continue

    c = fetch_num_input("Введите длину стороны c: ")
    if c is None:
        continue

    result = find_triangle(a, b, c)
    print(result)
    break 