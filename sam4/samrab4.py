def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(n):
    if not is_prime(n):
        return 0
    
    # Ищем следующее простое число
    next_num = n + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

def main():
    try:
        num_str = input("Введите натуральное число: ")
        num = int(num_str)

        if num < 0:
            print("Пожалуйста, введите натуральное (положительное) число.")
        else:
            if is_prime(num):
                print(f"Число {num} является простым.")
                next_prime = find_next_prime(num)
                print(f"Следующее простое число после {num}: {next_prime}")
            else:
                print(f"Число {num} не является простым.")
                print("Для поиска следующего простого числа введите простое число.")

    except ValueError:
        print("Ошибка: Введен некорректный формат числа. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()