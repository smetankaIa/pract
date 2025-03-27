def calculate():
    num1 = 1.0  
    num2 = 2.0  

    try:
        num1_str = input("Введите первое число: ")
        num1 = float(num1_str)
    except ValueError:
        print("Неправильный формат числа!\nВ качестве значения первого числа будет 1.")

    try:
        num2_str = input("Введите второе число: ")
        num2 = float(num2_str)
    except ValueError:
        print("Неправильный формат числа!\nВ качестве значения второго числа будет 2.")

    summarize = num1 + num2
    multiply = num1 * num2
    sub = num1 - num2
    divide = 0.0 
    try:
        divide = num1 / num2
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")

    print(f"\n{num1} + {num2} = {summarize}")
    print(f"{num1} * {num2} = {multiply}")
    print(f"{num1} - {num2} = {sub}")
    print(f"{num1} / {num2} = {divide}")

    input("\nДля выхода из программы нажмите [Enter]:")


if __name__ == "__main__":
    calculate()